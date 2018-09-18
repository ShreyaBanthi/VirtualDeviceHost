import json
from VirtualValues.PackagerStrategy import PackagerStrategy


class JsonArrayPackagerStrategy(PackagerStrategy):

    def package(self, virtual_values, synthesized_values):
        return json.dumps(synthesized_values)
