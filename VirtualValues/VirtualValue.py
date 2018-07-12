from VirtualValues.InputDataSourceMapping import InputDataSourceMapping


class VirtualValue:
    name = 'unnamed'
    message_template_symbol = ''
    mappings = []
    input_data_sources = []
    aggregator = None
    synthesize_strategy = None

    # used_synthetisazation_strategy, used_aggregator_strategy
    def __init__(self, name, message_template_symbol):
        self.name = name
        self.message_template_symbol = message_template_symbol

    # def add_mapping(self, input_data_source, path):
    #     self.mappings.append(InputDataSourceMapping(input_data_source, path))

    def add_input_data_source(self, input_data_source):
        # for ids in self.input_data_sources:
            #  if ids.name == input_data_source.name:
                # raise Exception('duplicate input data source name!')
        self.input_data_sources.append(input_data_source)

    def set_aggregator_strategy(self, new_aggregator_strategy):
        self.aggregator = new_aggregator_strategy

    def set_synthesis_strategy(self, new_synthesis_strategy):
        self.synthesize_strategy = new_synthesis_strategy

    #  in receive phase
    #  def receive_new_incoming_data(self):

    #  in worker thread handle phase
    # def handle_new_incoming_data(self):
    #    for ids in self.input_data_sources:
    #        if ids.received_new_data:

    def aggregate_values(self):
        values = self.aggregator.aggregate(self.mappings)
        return values

    def run_aggregator(self):
        self.aggregator.aggregate(self.input_data_sources)

    def synthesize_value(self):
        # strategy = AverageSyntStrategy()
        # strategy = self.synthesize_strategy
        # synth_value = strategy.synthesize(values)
        synth_value = self.aggregator.synthesize_value()

        # TODO: get value, aggregate, synthesize
        return synth_value;


