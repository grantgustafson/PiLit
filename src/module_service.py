from flask import Blueprint, jsonify, request

from config import (
    LOGGER
)

modules = Blueprint('modules', __name__)
module_ips = {}

@modules.route('/get_modules', methods=['GET'])
def get_modules():
    modules = {'configuredModules' : [{'name' : 'Room', 'online': True},
                            {'name' : 'kitchen', 'online': False}],
               'unconfiguredModules' : [{'MAC' : 'blah blah'}]}
    return jsonify(modules)

@modules.route('/register', methods=['POST'])
def register_module():
    if 'ip' not in request.form or 'MAC' not in request.form:
        return jsonify({'success': False, 'message': 'ip or MAC not in request'})

    ip = request.form['ip']
    mac = request.form['MAC']

    if mac not in module_ips:
        LOGGER.info('Adding module {} with ip {}'.format(mac, ip))
        module_ips[mac] = ip
    elif module_ips[mac] != ip:
        LOGGER.info('Updating module {} with ip {}'.format(mac, ip))
        module_ips[mac] = ip

    d = {'success': True}
    return jsonify(d)


def get_module_ips():
    return module_ips
