from spotify import Spotify

class TrackInfo:

    def __init__(self, track_id):
        self.sp = Spotify()
        self.data = self.sp.get_analysis(track_id)

    def get_all_beats(self):
        return [b['start'] for b in self.data['beats']]

    def get_all_bars(self):
        return [b['start'] for b in self.data['bars']]

    def get_beats(self, start_time, end_time):
        beats = self.get_all_beats()
        return filter(lambda b: b >= start_time and b <= end_time, beats)

    def get_i_beat_in_bar(self, i, start_time=0.0, end_time=99999):
        bars = set(self.get_all_bars())
        beats = self.get_all_beats()
        beat_idx = 0
        i_beats = []
        for beat in beats:
            if beat in bars:
                beat_idx = 0
            else:
                beat_idx += 1
            if beat_idx == i:
                i_beats.append(beat)
        return filter(lambda b: b >= start_time and b <= end_time, i_beats)
