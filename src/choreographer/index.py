from flask import Blueprint, jsonify, request, render_template
import json
from os.path import join, isfile
from spotify import Spotify

index = Blueprint('index', __name__)
spotify = Spotify()

@index.route('/')
def home():
    tracks = spotify.get_all_analysis_meta()
    return render_template('index.html', tracks = tracks)
