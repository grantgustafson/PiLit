from flask import Blueprint, jsonify, request
import json
from models.flash import Flash
from models.module import Module
from hosts import Hosts

from config import (
    LOGGER,
    Session
)

module_service = Blueprint('module_service', __name__)

hosts = Hosts()
session = Session()

def get_online_modules():
    h = hosts.online_hosts
    modules = []
    unconfig_hosts = [hosts.get_host_dict(k) for k in h]
    return [], unconfig_hosts


@module_service.route('/get_modules', methods=['GET'])
def get_modules():
    modules, unconfig_hosts = get_online_modules()
    data = { 'configuredModules' : modules,
             'unconfiguredModules' : unconfig_hosts }
    print data
    return jsonify(data)

@module_service.route('/get_host/<host>', methods=['GET'])
def get_host(host):
    if host in hosts.online_hosts:
        data = { 'success' : True, 'host': hosts.get_host_dict(host)}
    else:
        data = { 'success' : False }
    return jsonify(data)

def create_or_update_module(data):
    #Todo: if already exists...
    name = data['name']
    location = data['location']
    hostname = data['hostname']
    module = Module(name=name, location=location, hostname=hostname)
    session.add(module)
    session.commit()

@module_service.route('/module_setup', methods=['POST'])
def setup():
    print json.loads(request.data)
    data = json.loads(request.data)
    print data['name']
    create_or_update_module(data)
    return jsonify({'success' : True, 'message': 'Successfully updated module'})

@module_service.route('/flash_module/<hostname>')
def flash(hostname):
    h = hosts.get_online_hosts
    return jsonify({'success': True})

def get_module_ips():
    return module_ips
