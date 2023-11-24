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

class AccMSGRep:
    def __init__(self, host, username, password, interface):
        self.host = host
        self.username = username
        self.password = password
        self.interface = interface

    
    # def Reload_CSC(self):
    #     a_device = {
    #         "host": self.host,
    #         "auth_username": self.username,
    #         "auth_password": self.password,
    #         "port": 22,
    #         "auth_strict_key": False,
    #         "ssh_config_file": "/etc/ssh/ssh_config",
    #     }