from VirtualValues.ParsingStrategy import ParsingStrategy
from Utilities import *


class JsonStringMatchParsingStrategy(ParsingStrategy):
    path = ''
    expected_string = ''
    ignore_case = False

    def __init__(self, path, expected_string, ignore_case):
        self.path = path
        self.expected_string = expected_string
        self.ignore_case = ignore_case

    def parse(self, raw_payload):
        parsed_value = get_json_value(raw_payload, self.path)
        if self.ignore_case:
            return str(parsed_value).lower() == self.expected_string.lower()
        else:
            return str(parsed_value) == self.expected_string
