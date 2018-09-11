from VirtualValues.AggregatorStrategy import AggregatorStrategy


class AllBooleanValuesEqualValueAggregatorStrategy(AggregatorStrategy):
    last_values = {}
    expected_value = False

    def __init__(self, expected_value):
        self.expected_value = expected_value

    def prepare(self):
        pass

    def aggregate(self, input_data_sources):
        for ids in input_data_sources:
            if ids.received_new_data():
                data_set = ids.pop_from_queue()
                self.last_values[ids.name] = str(data_set.parsed_data)

    def synthesize_value(self):
        values = self.last_values.values()
        if len(values) == 0:
            return 'true'
        for value in values:
            if value != self.expected_value:
                return 'false'
        return 'true'
