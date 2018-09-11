from VirtualValues.AggregatorStrategy import AggregatorStrategy


class FloatMaximumAggregatorStrategy(AggregatorStrategy):
    last_values = {}

    def __init__(self):
        pass

    def prepare(self):
        pass

    def aggregate(self, input_data_sources):
        for ids in input_data_sources:
            if ids.received_new_data():
                data_set = ids.pop_from_queue()
                self.last_values[ids.name] = float(data_set.parsed_data)

    def synthesize_value(self):
        values = self.last_values.values()
        if len(values) == 0:
            return 0
        return max(values)
