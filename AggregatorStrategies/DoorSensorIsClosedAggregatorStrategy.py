from AggregatorStrategy import AggregatorStrategy
from Utilities import every, is_number


class DoorSensorIsClosedAggregatorStrategy(AggregatorStrategy):

    def __init__(self):
        pass

    def parse_door_sensor_state(self, value):
        if isinstance(value, str) & (value.lower() == 'closed'):
            return True
        elif value == 1:
            return True
        elif isinstance(value, str) & (value.lower() == 'opened'):
            return False
        else:
            return False

    def aggregate(self, mappings):
        values = []
        for m in mappings:
            raw_val = m.get_value()
            values.append(self.parse_truthiness(raw_val))
        return values
