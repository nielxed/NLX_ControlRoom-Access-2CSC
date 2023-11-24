from scrapli import Scrapli
# from scrapli.exceptions import ScrapliAuthenticationFailed
import Cgpt_VerAcc_31123_cl as Vrfr

host = "192.168.201.4"
username = "caman"
password = "eC0-35212"
port = 22  # or the port you use for SSH
timeout = 10  # you can adjust the timeout value if necessary

ssh_verifier = Vrfr.SSHVerifier(host, username, password, port, timeout)
if ssh_verifier.verify_ssh_access():
    print(f"SSH access to {host} is verified.")
else:
    print(f"SSH access to {host} failed.")
