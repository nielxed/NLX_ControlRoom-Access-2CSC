from scrapli import Scrapli
from scrapli.exceptions import ScrapliAuthenticationFailed

def verify_ssh_access(host, username, password, port=22, timeout=10):
    try:
        conn = Scrapli(
            host=host,
            port=port,
            auth_username=username,
            auth_password=password,
            auth_strict_key=False,
            timeout_socket=timeout,
            timeout_transport=timeout,
            timeout_ops=timeout,
        )
        conn.open()
        conn.close()
        return True
    except ScrapliAuthenticationFailed as e:
        print(f"Authentication failed for {username}@{host}: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Replace these with your own values
host = "your_host_ip_or_hostname"
username = "your_username"
password = "your_password"
port = 22  # or the port you use for SSH
timeout = 10  # you can adjust the timeout value if necessary

if verify_ssh_access(host, username, password, port, timeout):
    print(f"SSH access to {host} is verified.")
else:
    print(f"SSH access to {host} failed.")