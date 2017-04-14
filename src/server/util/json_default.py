
class JSONDefault:

    _defaults = {'string': '',
                 'number' : 0,
                 'boolean' : False}

    def __init__(self, schema):
        self._schema = schema

    def default(self):
        d = {}
        for k in self._schema:
            d[k] = self._defaults[self._schema[k]['type']]
        return d
