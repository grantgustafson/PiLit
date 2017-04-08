from flask import Blueprint, jsonify, request
from jsonschema import validate
import json
from models.light_modules import Modules

from config import (
    LOGGER,
    MODULE_SCHEMA_PATH,
)

module_service = Blueprint('module_service', __name__)
module_ips = {}
modules = Modules()
unconfigured_modules = {}


@module_service.route('/get_modules', methods=['GET'])
def get_modules():
    data = { 'configuredModules' : modules.get_model_json }
    data['unconfiguredModules'] = [{'MAC' : k, 'ip' : unconfigured_modules[k] } for k in unconfigured_modules]
    return jsonify(data)

def create_or_update_module(data):
    with open(MODULE_SCHEMA_PATH) as f:
        schema = json.load(f)
    try:
        validate(data, schema)
        LOGGER.info('Module {}: new data validated').format(data['MAC'])
    except jsonschema.exceptions.ValidationError as ve:
        LOGGER.error('New Module data error: {}').format(ve)

@module_service.route('/register', methods=['POST'])
def register_module():
    if 'ip' not in request.form or 'MAC' not in request.form:
        return jsonify({'success': False, 'message': 'ip or MAC not in request'})

    ip = request.form['ip']
    mac = request.form['MAC']

    module = modules.get(MAC=mac)
    if not module:
        unconfigured_modules[mac] = ip
    else:
        module.ip = ip


    d = {'success': True}
    return jsonify(d)


def get_module_ips():
    return module_ips
