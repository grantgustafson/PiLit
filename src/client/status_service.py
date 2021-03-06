from flask import Blueprint, jsonify, request
from config import MOCK
import sys
sys.path.append('../util')
from net_info import get_hw_addr, get_ip_addr
import json

status_service = Blueprint('status_service', __name__)
IFACE = 'wlan0'


@status_service.route('/status', methods=['GET'])
def status():
    return jsonify({'active' : True,
                    'MAC': get_hw_addr(IFACE),
                    'ip' : get_ip_addr(IFACE)})
