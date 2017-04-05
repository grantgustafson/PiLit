import socket
import fcntl
import struct
import argparse
import json
import requests

PORT = 8887
RESP_PORT = 8886
IP = ''
IFACE = 'wlan0'
BUFFER_SZ = 1024
MESSAGE = "Pidentify"
ROUTE = 'http://{}:5000/register'

def parse_args():
    parser = argparse.ArgumentParser(description='Regression Fit')
    parser.add_argument('-d', action='store_true')
    return parser.parse_args()

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def get_hw_addr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ':'.join(['%02x' % ord(char) for char in info[18:24]])

if __name__ == '__main__':
    args = parse_args()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP, PORT))
    while True:
        data, addr = sock.recvfrom(BUFFER_SZ)
        print 'Recieved data from {}:'.format(addr)
        if data == MESSAGE:
            ip = addr[0]
            if args.d:
                d = {'ip': 'debug',
                     'MAC': 'debug',
                     'debug': True}
                ip = 'localhost'
            else:
                d = {'ip': get_ip_address(IFACE),
                     'MAC': get_hw_addr(IFACE)}
            url = ROUTE.format(ip)
            requests.post(url, data=d)
