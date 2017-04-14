
class Strip:

    def __init__(self, mapping):
        self._create_mapping(mapping)


    '''
    mapping: [{startpixel : int, numpixels : int, forwards : boolean}]
    '''
    def _create_mapping(self, map_data):
        mapping = {}
        pixel = 0
        for map_datum in map_data:
            start_pixel = map_datum['startpixel']
            num_pixels = map_datum['numpixels']
            direction = 1
            if not map_datum['forwards']:
                direction = -1
            end_pixel = start_pixel + num_pixels * direction
            for i in range(start_pixel, end_pixel, direction):
                mapping[pixel] = i
                pixel += 1
        self.mapping = mapping
