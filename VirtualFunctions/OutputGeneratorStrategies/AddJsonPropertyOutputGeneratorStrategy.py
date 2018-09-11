from VirtualFunctions.OutputGeneratorStrategy import OutputGeneratorStrategy
from Utilities import load_dirty_json
import json


class AddJsonPropertyOutputGeneratorStrategy(OutputGeneratorStrategy):
    property_name = ''
    property_value = ''

    def __init__(self, property_name, property_value):
        self.property_name = property_name
        self.property_value = property_value

    def generate(self, source_message):
        json_msg = load_dirty_json(source_message)
        json_msg[self.property_name] = self.property_value
        return json.dumps(json_msg)
