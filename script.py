from paramiko import SSHClient
import os

IP = ''
USER = ''
PASSWORD = ''

client = SSHClient()
client.load_system_host_keys()
client.connect(IP, username=USER, password=PASSWORD)
