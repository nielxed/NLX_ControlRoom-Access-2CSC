# NLX Swrd: CRAcc2CSC (code name: Lothlorien)
# Version: Celeborn
import paramiko
import socket
import time
import re
import datetime
"""
As taken and mod to need from ChatGPT:
The class takes the following is injected with access details:
- Username
- Password
"""
# The Class is of type NLXShield

class CiscoSwitchChecker:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.enable_password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        try:
            self.client.connect(self.host, username=self.username, password=self.password)
            return True
        except paramiko.AuthenticationException:
            print(f"Authentication failed for {self.host}")
            return False
        except paramiko.SSHException as e:
            print(f"Unable to establish SSH connection to asset {self.host}: {str(e)}")
            return False

    def check_accessibility(self):
        if self.connect():
            print(f"Successfully connected to asset {self.host}")
            self.client.close()
            return True
        else:
            print(f"Failed to connect to asset {self.host}")
            return False

    def reload_port(self):
        if self.connect():
            try:
                # Create an interactive shell
                shell = self.client.invoke_shell()
                time.sleep(1)

                # Send enable command
                shell.send("conf t\n")
                time.sleep(1)
                # shell.send(f"interface {port}")
                # time.sleep(1)

                # Send the command to reload the specified port
                # shell.send(f"reload interface {port}\n")
                # time.sleep(1)

                # Wait for the reload confirmation prompt (customize this based on your switch)
                confirmation_prompt = f"The command 'configure terminal <cr>' is not authorized for user testapp and client {self.host}"
                output = shell.recv(65535).decode("utf-8")
                # print(confirmation_prompt)
                # print(output)

                if confirmation_prompt in output:
                    print(f"User {self.username} does not have rights to reload ports on asset {self.host}")
                    return True
                else:
                    print(f"User {self.username} has rights to reload ports on asset {self.host}")
                    return False
            except Exception as e:
                print(f"Error reloading ports on asset {self.host}: {str(e)}")
                return False
            finally:
                shell.close()
        else:
            return False

if __name__ == "__main__":
    
    # Replace these values with the actual credentials and IP addresses of your Cisco switches
    HQ11 = CiscoSwitchChecker("192.168.77.11", "testapp", "Wargaming!!")
    HQ11_result_con = HQ11.check_accessibility()
    HQ11_RLDSuccess = HQ11.reload_port()
    IDF14 = CiscoSwitchChecker("192.168.77.14", "testapp", "Wargaming!!")
    IDF14_result_con = IDF14.check_accessibility()
    IDF14_RLDSuccess = IDF14.reload_port()
    B113 = CiscoSwitchChecker("192.168.77.13", "testapp", "Wargaming!!")
    B113_result_con = B113.check_accessibility()
    B113_RLDSuccess = B113.reload_port()
    B320 = CiscoSwitchChecker("192.168.77.20", "testapp", "Wargaming!!")
    B320_result_con = B320.check_accessibility()
    B320_RLDSuccess = B320.reload_port()
    P14 = CiscoSwitchChecker("192.168.201.4", "testapp", "Wargaming!!")
    P14_result_con = P14.check_accessibility()
    P14_RLDSuccess = P14.reload_port()
    H13 = CiscoSwitchChecker("192.168.200.3", "testapp", "Wargaming!!")
    H13_result_con = H13.check_accessibility()
    H13_RLDSuccess = H13.reload_port()
    H240 = CiscoSwitchChecker("192.168.200.40", "testapp", "Wargaming!!")
    H240_result_con = H240.check_accessibility()
    H240_RLDSuccess = H240.reload_port()
    H241 = CiscoSwitchChecker("192.168.200.41", "testapp", "Wargaming!!")
    H241_result_con = H241.check_accessibility()
    H241_RLDSuccess = H241.reload_port()
    H372 = CiscoSwitchChecker("192.168.200.72", "testapp", "Wargaming!!")
    H372_result_con = H372.check_accessibility()
    H372_RLDSuccess = H372.reload_port()
    H373 = CiscoSwitchChecker("192.168.200.73", "testapp", "Wargaming!!")
    H373_result_con = H373.check_accessibility()
    H373_RLDSuccess = H373.reload_port()
    H374 = CiscoSwitchChecker("192.168.200.74", "testapp", "Wargaming!!")
    H374_result_con = H374.check_accessibility()
    H374_RLDSuccess = H374.reload_port()
    H4100 = CiscoSwitchChecker("192.168.200.100", "testapp", "Wargaming!!")
    H4100_result_con = H4100.check_accessibility()
    H4100_RLDSuccess = H4100.reload_port()
    H4101 = CiscoSwitchChecker("192.168.200.101", "testapp", "Wargaming!!")
    H4101_result_con = H4101.check_accessibility()
    H4101_RLDSuccess = H4101.reload_port()

    if HQ11_result_con and IDF14_result_con and B113_result_con and B320_result_con and P14_result_con\
          and H13_result_con and H240_result_con and H241_result_con and H372_result_con and H373_result_con\
              and H374_result_con and H4100_result_con and H4101_result_con:
        print("All assets are accessible.")
    else:
        print(f"Some/all switches are not accessible. Please see log for more details.")

    if HQ11_RLDSuccess and IDF14_RLDSuccess and B113_RLDSuccess and B320_RLDSuccess and P14_RLDSuccess\
          and H13_RLDSuccess and H240_RLDSuccess and H241_RLDSuccess and H372_RLDSuccess and H373_RLDSuccess\
            and H374_RLDSuccess and H4100_RLDSuccess and H4101_RLDSuccess:
        print("User permissions on assets not validated.")
    else:
        print("Actions permited on all switches.")
"""
Status: In composition
Result: Pending
"""
