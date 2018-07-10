from VirtualValues.ParsingStrategy import ParsingStrategy
from Utilities import *


class JsonParsingStrategy(ParsingStrategy):
    path = ''

    def __init__(self, path):
        self.path = path

    def parse(self, raw_payload):
        return get_json_value(raw_payload, self.path)
