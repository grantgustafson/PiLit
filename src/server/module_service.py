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


@module_service.route('/get_modules', methods=['GET'])
def get_modules():
    data = { 'configuredModules' : modules.get_model_json(),
             'unconfiguredModules' : modules.get_unconfigured_json() }
    return jsonify(data)

@module_service.route('/get_host/<host>', methods=['GET'])
def get_host(host):
    host = modules.get_host(host)
    if host:
        data = { 'success' : True, 'host': host}
    else:
        data = { 'success' : False }
    return jsonify(data)

def create_or_update_module(data):
    with open(MODULE_SCHEMA_PATH) as f:
        schema = json.load(f)
    try:
        validate(data, schema)
        LOGGER.info('Module {}: new data validated').format(data['MAC'])
    except jsonschema.exceptions.ValidationError as ve:
        LOGGER.error('New Module data error: {}').format(ve)

@module_service.route('/module_setup', methods=['POST'])
def setup():
    print json.loads(request.data)
    return jsonify({'success' : True})



def get_module_ips():
    return module_ips
