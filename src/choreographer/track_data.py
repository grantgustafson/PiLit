from flask import Blueprint, jsonify, request, render_template
import json
from spotify import Spotify
from timing import SpotifyTime
from os.path import join, isfile
from os import listdir

ANALYSIS_DATA_PATH = 'analysis_data/'
KF_PATH = 'key_frames/'
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

@track_service.route('/track/save_kfs', methods=['POST'])
def save_kfs():
    data = json.loads(request.data)
    print data
    ikfs = sorted(data['ikfs'], key=lambda o: o['time'])
    mkfs = sorted(data['mkfs'], key=lambda o: o['time'])
    track_id = data['id']
    with open(join(KF_PATH, track_id), 'w') as f:
        json.dump({'ikfs': ikfs, 'mkfs': mkfs}, f, indent=4)
    print data

    return jsonify({'success': True})

@track_service.route('/track/get_kfs/<track_id>', methods=['GET'])
def get_kfs(track_id):
    path = join(KF_PATH, track_id)
    if isfile(path):
        with open(path) as f:
            data = json.load(f)
            return jsonify({'success': True, 'data': data})
    else:
        jsonify({'success': True, 'data': {'ikfs' : [], 'mkfs' : []}})
    return jsonify({'success': False})


if __name__ == '__main__':
    resolve_track_meta()
