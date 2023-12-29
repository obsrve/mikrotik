from netmiko import ConnectHandler

ip = input("Enter ip: ")


def mikrott():
    mk = {
        'device_type': 'mikrotik_routeros',
        'host': '10.10.4.1',
        'port': '22',
        'username': 'sysadm',
        'password': 'brosco.net.ua'
    }

    sshCli = ConnectHandler(**mk)
    sshCli.enable()

    commands = ['/ip/dhcp-server/lease/make-static numbers=[/ip/dhcp-server/lease/find address='+ip+']',
                '/ip/dhcp-server/lease/set address=dhcp number=[/ip/dhcp-server/lease/find address='+ip+']']
    for x in commands:
        output = sshCli.send_command(x)

    sshCli.disconnect()


mikrott()
