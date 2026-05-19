from netmiko import ConnectHandler

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",
        "username": "student",
        "password": "Meilab123",
        "port": "22"
    }
]

commands = [
    "show interface description",
    "show ip interface brief",
    "show version"
]

for device in devices:

    print("\n" + "=" * 80)
    print(f"Connecting to {device['ip']}")

    net_connect = ConnectHandler(**device)

    for cmd in commands:
        print("\n" + "-" * 40)
        print(f"Command: {cmd}")
        print("-" * 40)

        output = net_connect.send_command(cmd)
        print(output)

    net_connect.disconnect()
