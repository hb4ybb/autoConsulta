from paramiko import SSHClient
import os

IP = ''
USER = ''
PASSWORD = ''

client = SSHClient()
client.load_system_host_keys()
client.connect(IP, username=USER, password=PASSWORD)

stdin, stdout, stderr = client.exec_command(
    'cd /montana/anti_hack; chmod 000 anti_hack.txt'
    )
