
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
uptime = session.send_command("show system uptime", expect_string=prompt)
alarms = session.send_command("show system alarms", expect_string=prompt)
version = session.send_command("show system version | grep Board", expect_string=prompt)
utilization = session.send_command("show system utilization", expect_string=prompt)
jitter = session.send_command("show voip channel-stats rtt-threshold 0", expect_string=prompt)
config = session.send_command("show running-config", expect_string=prompt)
proxy_status = session.send_command("show voip proxy sets status", expect_string=prompt)
active_calls = session.send_command("show voip calls active sbc", expect_string=prompt)
calls_history = session.send_command("show voip calls history sbc first 50", expect_string=prompt)
calls_statistics = session.send_command("show voip calls statistics sbc", expect_string=prompt)

result = [uptime,alarms,version,utilization,jitter,config,proxy_status,active_calls,calls_history,calls_statistics]

print(result)

session.disconnect()

