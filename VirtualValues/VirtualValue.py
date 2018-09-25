

class VirtualValue:
    name = None
    message_template_symbol = None
    input_data_sources = None
    aggregator = None

    def __init__(self, name, message_template_symbol):
        self.name = name
        self.message_template_symbol = message_template_symbol
        self.input_data_sources = []
        self.aggregator = None

    def add_input_data_source(self, input_data_source):
        for ids in self.input_data_sources:
            if ids.name == input_data_source.name:
                raise Exception('duplicate input data source name!')
        self.input_data_sources.append(input_data_source)

    def set_aggregator_strategy(self, new_aggregator_strategy):
        self.aggregator = new_aggregator_strategy
        self.aggregator.prepare()

    def aggregate_values(self):
        values = self.aggregator.aggregate(self.mappings)
        return values

    def run_aggregator(self):
        if self.aggregator is None:
            raise Exception('no aggregator defined')
        self.aggregator.aggregate(self.input_data_sources)

    def synthesize_value(self):
        synth_value = self.aggregator.synthesize_value()

        return synth_value


