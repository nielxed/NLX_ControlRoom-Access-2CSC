# NLX Swrd: CRAcc2CSC (code name: Lothlorien)
# Version: Celeborn
import paramiko
import time
"""
As taken and mod to need from ChatGPT:
The class takes the following ingected values and runs a modified version of predefined list of commands
on a remote site that holds assets:
- Hostname
- Username
- Password
- Interface
The commands are split into single line commands that are executed with a 5 second break (readjusted from 4).
In test execution time with 5 second break: 20440.656900405884 ms
"""
class AssetRldCmdsExe:
    def __init__(self, host, username, password, port, interface):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.interface = interface
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.shell = None

    def connect(self):
        try:
            self.client.connect(self.host, port=self.port, username=self.username, password=self.password, timeout=5)
            print(f"Connected to {self.host} on port {self.port}")
        except paramiko.AuthenticationException:
            print(f"Authentication failed for {self.username}@{self.host}")
        except Exception as e:
            print(f"Error connecting to {self.host}: {str(e)}")

    # Climb to global configuration mode (configuration terminal)
    def start_config_terminal(self):
        self.shell = self.client.invoke_shell()
        time.sleep(1)
        self.shell.send("config terminal\n")
        time.sleep(2)
        output = self.shell.recv(65535).decode("utf-8")
        print(output)

    # Commands are executed one by one in definition
    def send_command(self, command):
        if not self.shell:
            print("Error: Configuration terminal not started. Call start_config_terminal first.")
            return

        self.shell.send(command + "\n")
        time.sleep(5)
        output = self.shell.recv(65535).decode("utf-8")
        print(output)

    # Get command list based on descriptions passed in Class. The definition splits list in loop and sends to "send_command" definition for execution
    def send_commands(self):
        config_command_list = [f"interface {self.interface}", "shutdown", "no shutdown"]
        self.start_config_terminal()
        for command in config_command_list:
            self.send_command(command)

    def close(self):
        if self.shell:
            self.shell.close()
        self.client.close()
        print(f"Connection to {self.host} closed.")

# Example usage:
if __name__ == "__main__":
    start = time.time()
    SSHCSCPrmk_Rldr = AssetRldCmdsExe(host="192.168.201.4", port=22, username="caman", password="eC0-35212", interface="Gi1/0/6")
    SSHCSCPrmk_Rldr.connect()
    # Send the list of configuration commands
    SSHCSCPrmk_Rldr.send_commands()
    SSHCSCPrmk_Rldr.close()
    end = time.time()
    print("Time to execute:",
        (end-start) * 10**3, "ms")

# NLXComments Post-Ver
"""
Result: Good
"""
