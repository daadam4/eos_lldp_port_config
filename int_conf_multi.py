import pyeapi

hosts = ["192.168.1.55", "192.168.1.56"]

for ip_address in hosts:
    
    node = pyeapi.client.connect(host=ip_address, username='admin', password='admin', transport='http', return_node=True)

    for interface in range(1,49):
        # Configure interface Ethernet1
        commands = [
        f'interface Ethernet{interface}',
        'description Configured by Arista Python script',
        'no shutdown',
        ]

        node.config(commands)

    validate = [
        f'show running-config interfaces Ethernet1'
    ]

    result = node.run_commands(validate, encoding='text')

    for element in result:
        for _, m in element.items():
            print(f"command:\n{validate[0]}\nresult:\n{m}")