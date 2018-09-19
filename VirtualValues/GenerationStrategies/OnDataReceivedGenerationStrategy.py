from datetime import datetime
from VirtualValues.GenerationStrategy import GenerationStrategy


class OnDataReceivedGenerationStrategy(GenerationStrategy):
    last_timestamp = None

    def should_generate(self):
        if self.last_timestamp is None:
            self.last_timestamp = datetime.now()
            return True

        # loop through all InputDataSources, if timestamp newer than last_timestamp than True, else false
        for vv in self.virtual_value_group.virtual_values:
            for ids in vv.input_data_sources:
                if ids.last_timestamp is not None and ids.last_timestamp > self.last_timestamp:
                    self.last_timestamp = datetime.now()
                    return True

        return False
