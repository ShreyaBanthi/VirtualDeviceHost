class OutputTarget:
    name = ''
    output_broker_connection_name = ''
    output_topic = ''
    generator_strategy = None

    def __init__(self, name, output_broker_connection_name, output_topic, generator_strategy):
        self.name = name
        self.output_broker_connection_name = output_broker_connection_name
        self.output_topic = output_topic
        self.generator_strategy = generator_strategy
