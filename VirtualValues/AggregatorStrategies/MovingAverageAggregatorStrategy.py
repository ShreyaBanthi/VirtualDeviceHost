from VirtualValues.AggregatorStrategy import AggregatorStrategy
from functools import reduce


class MovingAverageAggregatorStrategy(AggregatorStrategy):
    last_calculated_values = []
    last_snapshot_values = {}
    data_set_size = 5

    def __init__(self, data_set_size=5):
        self.last_calculated_values = []
        self.last_snapshot_values = {}
        self.data_set_size = data_set_size

    def prepare(self):
        pass

    def aggregate(self, input_data_sources):
        for ids in input_data_sources:
            if ids.received_new_data():
                data_set = ids.pop_from_queue()
                self.last_snapshot_values[ids.name] = float(data_set.parsed_data)

    def synthesize_value(self):
        values = self.last_values.values()
        if len(values) == 0:
            return 0
        values_sum = sum(values)
        avg = round(values_sum / len(values), 2)
        self.last_calculated_values.append(avg)
        if len(self.last_calculated_values) > self.data_set_size:
            self.last_calculated_values.pop(0)
        moving_avg = reduce(lambda x, y: x + y, self.last_calculated_values) / len(self.last_calculated_values)
        return round(moving_avg, 2)
