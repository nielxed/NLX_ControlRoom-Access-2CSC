# NLX Swrd: CRAcc2CSC (code name: Lothlorien)
# Version: Celeborn
from scrapli import Scrapli
from scrapli.exceptions import ScrapliAuthenticationFailed

# Class imports assets to verify TACACS.net credential provided by the user.
"""
The Class is of type NLXShield
"""
# The Class is of type NLXShield
class SSHVerifier:
    def __init__(self, host, username, password, port=22, timeout=10):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.timeout = timeout

    def verify_ssh_access(self):
        try:
            conn = Scrapli(
                host=self.host,
                port=self.port,
                auth_username=self.username,
                auth_password=self.password,
                auth_strict_key=False,
                timeout_socket=self.timeout,
                timeout_transport=self.timeout,
                timeout_ops=self.timeout,
                platform="cisco_iosxe",
                ssh_config_file="/etc/ssh/ssh_config"
            )
            conn.open()
            conn.close()
            return True
        except ScrapliAuthenticationFailed as e:
            print(f"Authentication failed for {self.username}@{self.host}: {e}")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

# NLXComments Post-Ver
"""
"""
