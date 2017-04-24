from spotipy import oauth2
from os.path import join, isfile
from subprocess import Popen, PIPE
from os import listdir
import requests
import json

CLIENTID='e20406e401e1456b920f6c18e2b7d0b1'
CLIENTSECRET='9041f1578718450b9cf327fb4a24545d'
CURR_TRACK_SCRIPT='scripts/current_track.scpt'
CURR_POS_SCRIPT='scripts/current_pos.scpt'
ANALYSIS_DATA_PATH = 'analysis_data/'
MY_ID = '12140715906'
LIT_ID = '6qG0tzNkyfvP5IVvRRuc7b'
META_FILE = 'meta.json'

class Spotify:

    _instantiated = False
    _shared_state = {}
    def __init__(self):
        self.__dict__ = self._shared_state
        if not self._instantiated:
            auth = oauth2.SpotifyClientCredentials(client_id=CLIENTID, client_secret=CLIENTSECRET)
            self._auth = auth.get_access_token()
            self.prefix = 'https://api.spotify.com/v1/'
            self._instantiated = True

    def _auth_headers(self):
        return {'Authorization': 'Bearer {0}'.format(self._auth)}

    def my_get(self, url):
        headers = self._auth_headers()
        headers['Content-Type'] = 'application/json'
        for i in range(5):
            r = requests.get(url, headers=headers)
            if r.status_code != 200:
                print r.text
                print r.status_code
                time.sleep(1)
            else:
                print 'Sucessful Request!'
                return r.json()
        exit()

    def fetch_analysis(self, track_id):
        return self.my_get(self.prefix + 'audio-analysis/' + track_id)

    def fetch_track(self, track_id):
        return self.my_get(self.prefix + 'tracks/' + track_id)

    def get_analysis(self, track_id):
        path = ANALYSIS_DATA_PATH + track_id
        if isfile(path):
            with open(path) as d:
                return json.load(d)
        else:
            print 'fetching data'
        data = self.fetch_analysis(track_id)
        track_meta = self.fetch_track(track_id)
        name = track_meta['name']
        artists = [a['name'] for a in track_meta['artists']]
        data['track']['name'] = name
        data['track']['artists'] = ', '.join(artists)
        self.write_analysis_file(track_id, data)
        return data

    def resolve_track_meta(self):
        tracks = self.get_anaysis_tracks_ids()
        for track in tracks:
            data = self.load_analysis_file(track)
            if 'name' not in data['track']:
                print 'track meta not in {}'.format(track)
                track_meta = self.fetch_track(track)
                name = track_meta['name']
                artists = [a['name'] for a in track_meta['artists']]
                data['track']['name'] = name
                data['track']['artists'] = ', '.join(artists)
                self.write_analysis_file(track, data)
            else:
                print '{} has track meta'.format(track)

    def write_analysis_file(self, track_id, data):
        with open(ANALYSIS_DATA_PATH + track_id, 'w') as f:
            json.dump(data, f)

    def load_analysis_file(self, track_id):
        path = ANALYSIS_DATA_PATH + track_id
        assert isfile(path)
        with open(path) as f:
            data = json.load(f)
        return data

    def get_all_analysis_meta(self):
        meta = []
        for track_id in self.get_anaysis_tracks_ids():
            data = self.load_analysis_file(track_id)
            t = data['track']
            meta.append({'name': t['name'],
                        'artists': t['artists'],
                        'id': track_id})
        return meta

    def get_anaysis_tracks_ids(self):
        files = [f for f in listdir(ANALYSIS_DATA_PATH) if isfile(join(ANALYSIS_DATA_PATH, f))]
        files = filter(lambda t: not t.startswith('.'), files)
        return files

    def get_current_track_id(self):
        proc = Popen([CURR_TRACK_SCRIPT], stdout=PIPE, stderr=PIPE)
        track_id, _ = proc.communicate()
        return track_id.strip().split(':')[-1]

    def print_playlists(self):
        path = self.prefix + 'users/{}/playlists'.format(MY_ID)
        data = self.my_get(path)
        playlists = [(i['name'], i['id']) for i in data['items']]
        print

    def get_tracks_in_playlist(self):
        url = self.prefix + 'users/{}/playlists/{}'.format(MY_ID, LIT_ID)
        data = self.my_get(url)
        tracks_data = data['tracks']['items']
        tracks = [{'name': t['track']['name'],
                   'id' : t['track']['id'],
                   'artists' : ', '.join([a['name'] for a in t['track']['artists']])} for t in tracks_data]
        return tracks

    def write_track_meta(self):
        tracks = self.get_tracks_in_playlist()
        with open(META_FILE, 'w') as f:
            json.dump(tracks, f, indent=4)


if __name__ == '__main__':
    s = Spotify()
    print s.write_track_meta()
