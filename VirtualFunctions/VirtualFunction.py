class VirtualFunction:
    name = 'unnamed'
    trigger_broker_connection_name = ''
    trigger_topic = ''
    output_targets = []

    def __init__(self, name, trigger_broker_connection_name, trigger_topic):
        self.name = name
        self.trigger_broker_connection_name = trigger_broker_connection_name
        self.trigger_topic = trigger_topic

    def add_output_target(self, new_output_target):
        self.output_targets.append(new_output_target)

    def handle_trigger_message(self, broker_connection, topic, msg):
        if self.trigger_broker_connection_name != broker_connection or self.trigger_topic == topic:
            return
        self.execute(msg)

    def execute(self, msg):
        for ot in self.output_targets:
            ot.generator_strategy.generate(msg)
