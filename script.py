from paramiko import SSHClient
from os import environ

IP = os.environ.get('SERVER_IP')
USER = os.environ.get('SERVER_USER')
PASSWORD = os.environ.get('SERVER_PASS')

client = SSHClient()
client.load_system_host_keys()
client.connect(IP, username=USER, password=PASSWORD)

stdin, stdout, stderr = client.exec_command(
    'cd /montana/anti_hack; chmod 000 anti_hack.txt'
    )

print(f'STDOUT: {stdout.read().decode("utf8")}')
print(f'STDERR: {stderr.read().decode("utf8")}')

stdin.close()
stdout.close()
stderr.close()

client.close()
