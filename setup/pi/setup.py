import os, platform, json

INTERFACE_TEMPLATE_PATH = '../templates/interfaces'
INTERFACE_PATH = '/etc/network/interfaces'
NET_CONFIG_PATH = '../../../PiLit_config/network.json'

def is_pi():
    return platform.uname()[1] == 'raspberrypi'

def net_file_exist():
    return os.path.isfile(INTERFACE_PATH)

def net_file_permissions():
    return os.access(INTERFACE_PATH, os.W_OK)

def setup_network():
    with open(INTERFACE_TEMPLATE_PATH, 'r') as f:
        template = f.read()
    if os.path.isfile(NET_CONFIG_PATH):
        with open(NET_CONFIG_PATH, 'r') as f:
            net_data = json.load(f)
    print 'Seting up pi network file...'
    ssid_promt = 'Enter WiFi SSID: '
    if net_data:
        ssid_promt += ' [default = {}]'.fomat(net_data['wpa-ssid'])
    ssid = input(ssid_promt)
    


if __name__ == '__main__':
    setup_network()
