import json


class MonitoringOutputMessage:
    states = None

    def __init__(self):
        self.states = {}
        pass

    def to_json(self):
        return '{"states": %s}' % json.dumps(self.states)