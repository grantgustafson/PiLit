from flask import Blueprint, jsonify, request
from config import MOCK
import sys
sys.path.append('../util')
from net_info import _get_hw_addr, _get_ip_addr
import json

status_service = Blueprint('status_service', __name__)
IFACE = 'eth0'

def get_hw_addr(IFACE):
    if MOCK:
        return 'de:ad:be:ef:00'
    return _get_hw_addr(IFACE)

def get_ip_addr(IFACE):
    if MOCK:
        return '10.0.0.5'
    return _get_ip_addr(IFACE)

@status_service.route('/status', methods=['GET'])
def status():
    return jsonify({'active' : True,
                    'MAC': get_hw_addr(IFACE),
                    'ip' : get_ip_addr(IFACE)})
