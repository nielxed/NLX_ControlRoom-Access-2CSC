import paramiko
import time

class CiscoSSHClient:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        try:
            self.client.connect(self.host, port=self.port, username=self.username, password=self.password, timeout=5)
            print(f"Connected to {self.host} on port {self.port}")
        except paramiko.AuthenticationException:
            print(f"Authentication failed for {self.username}@{self.host}")
        except Exception as e:
            print(f"Error connecting to {self.host}: {str(e)}")

    def send_command(self, command):
        try:
            stdin, stdout, stderr = self.client.exec_command(command, timeout=10)
            output = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')
            
            if output:
                print(f"Command Output:\n{output}")
            if error:
                print(f"Command Error:\n{error}")
        except Exception as e:
            print(f"Error executing command '{command}': {str(e)}")

    def send_commands(self, commands):
        for command in commands:
            self.send_command(command)
            # Add a small delay if needed
            time.sleep(1)

    def close(self):
        self.client.close()
        print(f"Connection to {self.host} closed.")

# Example usage:
if __name__ == "__main__":
    cisco_device = CiscoSSHClient(host='your_cisco_device_ip', port=22, username='your_username', password='your_password')

    cisco_device.connect()

    # Specify a set of commands to send
    command_list = ['show version', 'show interfaces', 'show running-config']

    # Send the list of commands
    cisco_device.send_commands(command_list)

    cisco_device.close()
