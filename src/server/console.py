from flask import Blueprint, jsonify, request, render_template
import os
from config import (
    LOGGER,
    rel_path
)
TEMPLATE_PATH = 'index.html'
console_service = Blueprint('console', __name__)

@console_service.route('/', methods=['GET'])
def main():
    return render_template(TEMPLATE_PATH)
