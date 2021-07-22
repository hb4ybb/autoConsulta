from paramiko import SSHClient
import os

IP = '127.0.0.1'
USER = 'montana'
PASSWORD = 'kCk7b5SaBPUkibDzcDa8bcKvb'

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
