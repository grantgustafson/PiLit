from spotify import Spotify

class TrackInfo:

    def __init__(self, track_id):
        self.sp = Spotify()
        self.data = self.sp.get_analysis(track_id)


    def get_beats(self, start_time, end_time):
        beats = self.data['beats']
        beats = [b['start'] for b in beats]
        return filter(lambda b: b >= start_time and b <= end_time, beats)
