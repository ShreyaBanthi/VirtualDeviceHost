import json
import re


from SynthesisStrategies.AverageSyntStrategy import AverageSyntStrategy
from SynthesisStrategies.AverageBooleanSyntStrategy import AverageBooleanSyntStrategy
from SynthesisStrategies.MaximumSyntStrategy import MaximumSyntStrategy
from AggregatorStrategies.SimpleFloatSnapshotAggregatorStrategy import SimpleFloatSnapshotAggregatorStrategy

def load_dirty_json(dirty_json):
    regex_replace = [(r"([ \{,:\[])(u)?'([^']+)'", r'\1"\3"'), (r" False([, \}\]])", r' false\1'), (r" True([, \}\]])", r' true\1')]
    for r, s in regex_replace:
        dirty_json = re.sub(r, s, dirty_json)
    clean_json = json.loads(dirty_json)
    return clean_json

class InputDataSourceMapping:
    input_data_source = None
    path = ''

    def __init__(self, input_data_source, path):
        self.input_data_source = input_data_source
        self.path = path

    def get_value(self):
        data_type = self.input_data_source.data_type
        if data_type == 'json':
            last_snapshot = self.input_data_source.last_data_snapshot
            if last_snapshot == '':
                return 0
            fixed_last_snapshot = re.sub('([{,:])(\w+)([},:])', '\\1\"\\2\"\\3', str(last_snapshot, 'utf-8'))
            # fixed_last_snapshot = re.sub('([{,:])(\w+)([},:])','\\1\"\\2\"\\3',str(last_snapshot))
            # fixed_last_snapshot = last_snapshot
            last_snapshot_json_document = json.loads(fixed_last_snapshot)
            # fixed_last_snapshot = load_dirty_json(last_snapshot)
            # return fixed_last_snapshot
            return last_snapshot_json_document[self.path]
        elif data_type == 'raw':
            return self.input_data_source.last_data_snapshot
        else:
            print('unknown data type ' + data_type)


# output
class VirtualValue:
    name = 'unnamed'
    message_template_symbol = ''
    mappings = []
    aggregator = None
    synthesize_strategy = None

    def __init__(self, name, message_template_symbol,
                 used_synthetisazation_strategy, used_aggregator_strategy):
        self.name = name
        self.message_template_symbol = message_template_symbol
        self.aggregator = SimpleFloatSnapshotAggregatorStrategy()
        if used_synthetisazation_strategy == 'math-average':
            self.synthesize_strategy = AverageSyntStrategy()
        elif used_synthetisazation_strategy == 'math-max':
            self.synthesize_strategy = MaximumSyntStrategy()
        elif used_synthetisazation_strategy == 'bool-count':
            self.synthesize_strategy = AverageBooleanSyntStrategy()
        else:
            raise Exception('unknown synthesization strategy')

    def add_mapping(self, input_data_source, path):
        self.mappings.append(InputDataSourceMapping(input_data_source, path))

    def aggregate_values(self):
        values = self.aggregator.aggregate(self.mappings)
        return values

    def synthesize_value(self, values):
        # strategy = AverageSyntStrategy()
        strategy = self.synthesize_strategy
        synth_value = strategy.synthesize(values)

        # TODO: get value, aggregate, synthesize
        return synth_value;


