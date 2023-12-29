import csv
from netmiko import ConnectHandler


def mikrott():
    file = 'mikrotik\\ntest.csv'
    with open(file) as f:
        reader = csv.reader(f)

        for row in reader:
            ip = str(row[1])
            passw = str(row[4])

            mk = {
                'device_type': 'mikrotik_routeros',
                'host': ip,
                'port': '22',
                'username': 'sysadm',
                'password': passw
            }

            sshCli = ConnectHandler(**mk)
            sshCli.enable()

            # commands = ['/user add name=test group=read password=brosco.net.ua disabled=no']
            output = sshCli.send_command(
                "/user add name=test group=read password=Qwerty-123 disabled=no")
            sshCli.disconnect()


mikrott()
