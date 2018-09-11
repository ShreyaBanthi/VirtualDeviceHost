from VirtualValues.PackagerStrategy import PackagerStrategy


class StringReplacePackagerStrategy(PackagerStrategy):
    message_template = ''

    def __init__(self, message_template):
        self.message_template = message_template

    def package(self, virtual_values, synthesized_values):
        msg = self.message_template
        for vv in virtual_values:
            synthesized_value = synthesized_values[vv]
            msg = msg.replace(vv.message_template_symbol, str(synthesized_value))
        return msg
