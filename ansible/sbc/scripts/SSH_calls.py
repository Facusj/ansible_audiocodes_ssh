
#!/usr/bin/env python3

import netmiko
import os


session = netmiko.ConnectHandler(ip="ip",
                username="user",
                password="password",
                secret="Admin",
                verbose= False,
                device_type="ipinfusion_ocnos")

session.enable()
prompt=session.find_prompt()
config = session.send_command("show running-config", expect_string=prompt)
active_calls = session.send_command("show voip calls active sbc", expect_string=prompt)

results = [config,active_calls]

print(results)

session.disconnect()

