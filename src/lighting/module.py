from strip import Strip

class Segment:

    def __init__(self, num_pixels):
        self._num_pixels = num_pixels
        self._strip = None

    def add_strip(self, strip, start_pixel, forwards):
        self._strip = strip
        self._strip_start = start_pixel
        self._forwards = forwards
        self._direction = 1
        if not forwards:
            self._direction = -1
        self._create_mapping(self._direction)

    def _create_mapping(self, direction):
        self._mapping = [i for i in range(self._strip_start,
                                          self._strip_start + self._num_pixels,
                                          direction)]

    def _get_from_strip(self, idx):
        return self._strip[self._mapping[idx]]

    def render(self):
        if self._strip is None:
            return [(0,0,0)] * self._num_pixels
        if self._forwards:
            start = self._strip_start
            end = self._strip_start + self._num_pixels
        else:
            start = self._strip_start + self._num_pixels
            end = self._strip_start - 1
        if end == 0:
            return self._strip.get_rgb()[start : : self._direction]
        else:
            return self._strip.get_rgb()[start : end : self._direction]

        return data


class Module:

    def __init__(self):
        self._segments = []

    def add_segment(self, segment, start_pixel):
        self._segments.append((start_pixel, segment))
        self._segments = sorted(self._segments, key=lambda o: o[0])

    def render(self):
        data = []
        for start, segment in self._segments:
            data += [(0,0,0)] * (start - len(data))
            data += segment.render()
        return data
