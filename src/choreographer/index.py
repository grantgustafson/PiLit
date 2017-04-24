from flask import Blueprint, jsonify, request, render_template
import json
from os.path import join, isfile
from spotify import Spotify

index = Blueprint('index', __name__)
spotify = Spotify()
META_FILE = 'meta.json'

@index.route('/')
def home():
    tracks = load_meta()
    return render_template('index.html', tracks = tracks)

def load_meta():
    with open(META_FILE) as f:
        return json.load(f)
