
from VirtualValues.AggregatorStrategy import AggregatorStrategy

'''

class BooleanSnapshotAggregatorStrategy(AggregatorStrategy):

    def __init__(self):
        pass

    def parse_truthiness(self, value):
        if value:
            return True
        elif isinstance(value, basestring) & (value.lower() == 'true'):
            return True
        elif value == 1:
            return True
        elif isinstance(value, basestring) & (value.lower() == 'false'):
            return False
        elif value == 0:
            return False
        else:
            return False

    def aggregate(self, mappings):
        values = []
        for m in mappings:
            raw_val = m.get_value()
            values.append(self.parse_truthiness(raw_val))
        return values
'''
