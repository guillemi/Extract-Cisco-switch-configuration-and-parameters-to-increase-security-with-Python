from netmiko import ConnectHandler
import json

import platform
import subprocess

def conect(ip,user,passw,ssh):
    if(ssh):
        device = {
        'device_type': 'cisco_ios', #  'cisco_ios' for ssh and 'cisco_ios_telnet' for telnet
        'host':   ip,
        'username': user,
        'password': passw,
        'global_delay_factor': 2
        }
    return ConnectHandler(**device)


def ping_device(current_ip_address):
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower() == "windows" else 'c', current_ip_address), shell=True, universal_newlines=True)
        if 'unreachable' in output:
            print("for", current_ip_address, " Ping is NOT OK")
            return False
        else:
            print("for", current_ip_address, " Ping is OK continuing with the config")
            return True
    except Exception:
        return False


def write_result(current_ip_address):
    dict_result = {
        'ip': current_ip_address,
        'comment': 'Comment OK'
    }
    with open('device-result.json', 'a') as f_obj:
        f_obj.write(json.dumps(dict_result, indent=4))
    return

a = conect( "10.132.21.50","netconf", "Passw0rd",1)