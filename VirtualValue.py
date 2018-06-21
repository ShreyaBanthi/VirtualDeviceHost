from SynthesisStrategies.AverageSyntStrategy import AverageSyntStrategy
from SynthesisStrategies.AverageBooleanSyntStrategy import AverageBooleanSyntStrategy
from SynthesisStrategies.MaximumSyntStrategy import MaximumSyntStrategy
from AggregatorStrategies.SimpleFloatSnapshotAggregatorStrategy import SimpleFloatSnapshotAggregatorStrategy
from InputDataSourceMapping import InputDataSourceMapping


class VirtualValue:
    name = 'unnamed'
    message_template_symbol = ''
    mappings = []
    aggregator = None
    synthesize_strategy = None

    # used_synthetisazation_strategy, used_aggregator_strategy
    def __init__(self, name, message_template_symbol):
        self.name = name
        self.message_template_symbol = message_template_symbol
        self.aggregator = SimpleFloatSnapshotAggregatorStrategy()
        self.synthesize_strategy = AverageSyntStrategy()
        """ if used_synthetisazation_strategy == 'math-average':
            self.synthesize_strategy = AverageSyntStrategy()
        elif used_synthetisazation_strategy == 'math-max':
            self.synthesize_strategy = MaximumSyntStrategy()
        elif used_synthetisazation_strategy == 'bool-count':
            self.synthesize_strategy = AverageBooleanSyntStrategy()
        else:
            raise Exception('unknown synthesization strategy')
            """

    def add_mapping(self, input_data_source, path):
        self.mappings.append(InputDataSourceMapping(input_data_source, path))

    def set_aggregator_strategy(self, new_aggregator_strategy):
        self.aggregator = new_aggregator_strategy

    def set_synthesis_strategy(self, new_synthesis_strategy):
        self.synthesize_strategy = new_synthesis_strategy

    def aggregate_values(self):
        values = self.aggregator.aggregate(self.mappings)
        return values

    def synthesize_value(self, values):
        # strategy = AverageSyntStrategy()
        strategy = self.synthesize_strategy
        synth_value = strategy.synthesize(values)

        # TODO: get value, aggregate, synthesize
        return synth_value;


