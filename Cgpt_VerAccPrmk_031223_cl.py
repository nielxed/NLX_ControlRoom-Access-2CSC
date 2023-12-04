# NLX Swrd: CRAcc2CSC (code name: Lothlorien)
# Version: Celeborn
import paramiko
import socket
import time
"""
As taken and mod to need from ChatGPT:
The class takes the following ingected values and verifies access to ESX assets:
- Hostname
- Username
- Password
"""
class CiscoSSHTester:
    def __init__(self, hostname, username, password, port=22, timeout=5):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port
        self.timeout = timeout
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def test_connectivity(self):
        try:
            self.client.connect(
                self.hostname,
                port=self.port,
                username=self.username,
                password=self.password,
                timeout=self.timeout
            )
            return True
        except paramiko.AuthenticationException as auth_error:
            print(f"Authentication failed: {auth_error}")
            print(f"Authentication failed for {self.username}@{self.host}: {e}")
        except paramiko.SSHException as ssh_error:
            print(f"Unable to establish SSH connection: {ssh_error}")
            print(f"Authentication failed for {self.username}@{self.host}: {e}")
        except socket.error as socket_error:
            print(f"Unable to connect to the remote device: {socket_error}")
            print(f"Authentication failed for {self.username}@{self.host}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print(f"Authentication failed for {self.username}@{self.host}: {e}")
        finally:
            # Graceful close of the paramiko session
            self.client.close()
        return False

# Example usage:
if __name__ == "__main__":
    hostname = "your_cisco_device_ip"
    hostname = "192.168.77.10"
    # username = "your_username"
    username = "caman"
    # password = "your_password"
    password = "eC0-3521234@@"

    # Start the speed clock
    start = time.time()
    
    tester = CiscoSSHTester(hostname, username, password)

    if tester.test_connectivity():
        print(f"SSH connectivity to {hostname} is successful.")
    else:
        print(f"SSH connectivity to {hostname} failed.")

    end = time.time()
    print("Time to execute: ",
          (end-start) * 10**3, "ms")
    
# NLXComments Post-Ver
"""
Result: Good
"""
