from flask import Blueprint, jsonify, request, render_template
import json
from spotify import Spotify
from timing import SpotifyTime
from os.path import join, isfile
from os import listdir

ANALYSIS_DATA_PATH = 'analysis_data/'
track_service = Blueprint('track_service', __name__)

spotify = Spotify()
spotify_time = SpotifyTime()
@track_service.route('/track/data/<track_id>', methods=['GET'])
def get_data(track_id):
    return jsonify({'analysis': spotify.get_analysis(track_id)})

@track_service.route('/track/<track_id>')
def track_choreo(track_id):
    return render_template('choreo.html', track_id=track_id)

@track_service.route('/track/pos')
def get_player_pos():
    pos = spotify_time.get_player_pos()
    print pos
    return jsonify({'pos': pos})

@track_service.route('/track/add_current')
def add_current():
    track_id = spotify.get_current_track_id()
    spotify.get_analysis(track_id)
    return jsonify({'success': True})

if __name__ == '__main__':
    resolve_track_meta()
