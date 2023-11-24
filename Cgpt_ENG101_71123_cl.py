"""
Install scrapli with "python3 -m pip install scrapli" (m for module)
Alternate installation with "pip3 install scrapli"
https://carlmontanari.github.io/scrapli/

Note! Code focuses on the Scrapli IOSXEDriver
from scrapli.driver.core import IOSXEDriver
"""
from scrapli.driver.core import IOSXEDriver
import time

# Class imports assets to reload CSC interfaces
"""
The Class is of type NLXShield
"""
# print(" This system is a property of WARGAMING.\n",
#       "Unauthorized access is prohibited!\n", 
#       "Disconnect, if you are not authorized to access this device.\n",
#       "Further actions can lead to criminal liability.\n",
#       "All events are logged.\n")

# Get Password inline
# print("Please use your TACAS+ credential.")
# user = input("Username: ")
# password = getpass.getpass()

# Inline IOS dictionary
# Pointes to KUBIK camera CCTV Camera KUBIC 1 BASEMENT FRONT KUBIC.25

class CSCReloader:
    def __init__(self, host, username, password, interface):
        self.host = host
        self.username = username
        self.password = password
        self.interface = interface

    def Reload_CSC(self):
        a_device = {
            "host": self.host,
            "auth_username": self.username,
            "auth_password": self.password,
            "port": 22,
            "auth_strict_key": False,
            "ssh_config_file": "/etc/ssh/ssh_config",
        }

        # record start time
        start = time.time()

        with IOSXEDriver(**a_device) as the_connection:
            my_commands_1 = the_connection.send_configs([f"interface gigabitEthernet {self.interface}", "shutdown"])
            print(my_commands_1.result, "\n")
            # Pause for 5 seconds
            time.sleep(5)
            my_command_2 = the_connection.send_config("no shutdown")
            print(my_command_2.result, "\n")
        
        # record end time
        end = time.time()
        print("Time to execute:",
            (end-start) * 10**3, "ms")

# NLXComments Post-Ver
"""
"""
