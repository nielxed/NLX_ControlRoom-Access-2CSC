# NLX Swrd: CRAcc2CSC (code name: Lothlorien)
# Version: Celeborn
import paramiko
import time
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
            # return True
            return (f"Successfully connected to asset {self.host}")
        else:
            print(f"Failed to connect to asset {self.host}")
            # return False
            return (f"Failed to connect to asset {self.host}")

    def reload_port(self):
        if self.connect():
            try:
                # Create an interactive shell
                shell = self.client.invoke_shell()
                time.sleep(1)

                # Send enable command
                shell.send("conf t\n")
                time.sleep(1)

                # Wait for the reload confirmation prompt (customize this based on your switch)
                confirmation_prompt = f"The command 'configure terminal <cr>' is not authorized for user testapp and client {self.host}"
                output = shell.recv(65535).decode("utf-8")

                if confirmation_prompt in output:
                    print(f"User {self.username} does not have rights to reload ports on asset {self.host}")
                    # return True
                    return (f"User {self.username} does not have rights to reload ports on asset {self.host}")
                else:
                    print(f"User {self.username} has rights to reload ports on asset {self.host}")
                    # return False
                    return (f"User {self.username} has rights to reload ports on asset {self.host}")
            except Exception as e:
                print(f"Error reloading ports on asset {self.host}: {str(e)}")
                # return False
                return (f"Error reloading ports on asset {self.host}: {str(e)}")
            finally:
                shell.close()
        else:
            # return False
            return ("General Error")

if __name__ == "__main__":
    # ---------- 
    # The following global variables already exist in "WGPtn_CRAcc2CSC_311023_102.py"
    # User defined username
    def setUserName_Global(USR):
        global inGlobal_User
        inGlobal_User = USR
    
    # User defined password
    def setPassWord_Global(PSW):
        global inGlobal_PassWord
        inGlobal_PassWord = PSW
    # Manual declaration
    setUserName_Global("testapp")
    setPassWord_Global("Wargaming!!")
    # ---------- 

    FullTestStory = ""

    # Declare text-files
    FSSCurrent_datetime = datetime.datetime.now()
    FSSFormatted_datetime = FSSCurrent_datetime.strftime("%Y%m%d_%H%M%S")
    FSSSsession_loggfile = f"SecNetCSCFTest_FullSysTest_{FSSFormatted_datetime}.txt"

    # Sec. Net. Switch tuple
    SecNetSwitches = ("192.168.77.11", "192.168.77.14", "192.168.77.13", "192.168.77.20",\
                      "192.168.201.4", "192.168.200.3", "192.168.200.40", "192.168.200.41",\
                        "192.168.200.72", "192.168.200.73", "192.168.200.74", "192.168.200.100",\
                            "192.168.200.101")

    # Replace these values with the actual credentials and IP addresses of your Cisco switches
    for SNSwitch in SecNetSwitches:
        activeSwitch = CiscoSwitchChecker(SNSwitch, inGlobal_User, inGlobal_PassWord)
        activeSwitch_result_con = activeSwitch.check_accessibility()
        activeSwitch_RLDSuccess = activeSwitch.reload_port()
        FullTestStory = (f"{FullTestStory}{activeSwitch_result_con}\n")
        FullTestStory = (f"{FullTestStory}{activeSwitch_RLDSuccess}\n")
        # print(activeSwitch_result_con)
        # print(activeSwitch_RLDSuccess)
        
    with open(FSSSsession_loggfile, "w")as FT_file:
        FT_file.write(FullTestStory)

    # if HQ11_result_con and IDF14_result_con and B113_result_con and B320_result_con and P14_result_con\
    #       and H13_result_con and H240_result_con and H241_result_con and H372_result_con and H373_result_con\
    #           and H374_result_con and H4100_result_con and H4101_result_con:
    #     print("All assets are accessible.")
    # else:
    #     print(f"Some/all switches are not accessible. Please see log for more details.")

    # if HQ11_RLDSuccess and IDF14_RLDSuccess and B113_RLDSuccess and B320_RLDSuccess and P14_RLDSuccess\
    #       and H13_RLDSuccess and H240_RLDSuccess and H241_RLDSuccess and H372_RLDSuccess and H373_RLDSuccess\
    #         and H374_RLDSuccess and H4100_RLDSuccess and H4101_RLDSuccess:
    #     print("User permissions on assets not validated.")
    # else:
    #     print("Actions permited on all switches.")
"""
State: Good
Result: Pending
"""
