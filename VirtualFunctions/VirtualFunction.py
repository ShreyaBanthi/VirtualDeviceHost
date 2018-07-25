class VirtualFunction:
    name = 'unnamed'
    trigger_broker_connection_name = ''
    trigger_topic = ''
    output_targets = []
    broker_connection_repository = None

    def __init__(self, name, trigger_broker_connection_name, trigger_topic):
        self.name = name
        self.trigger_broker_connection_name = trigger_broker_connection_name
        self.trigger_topic = trigger_topic

    def add_output_target(self, new_output_target):
        self.output_targets.append(new_output_target)

    def handle_trigger_message(self, broker_connection, topic, msg):
        if self.trigger_broker_connection_name != broker_connection.connection_name or self.trigger_topic != topic:
            return
        self.execute(msg)  # TODO: put in queue, have handle thread

    def set_broker_connection_repository(self, broker_connection_repository):
        self.broker_connection_repository = broker_connection_repository

    def execute(self, msg):
        print('executing virtual function')
        msg_string = str(msg.payload)
        print('INPUT: ' + msg_string)
        for ot in self.output_targets:
            output_message = ot.generator_strategy.generate(msg_string)
            if ot is not None:
                broker_connection = self.broker_connection_repository.get_broker_connection(ot.output_broker_connection_name)
                broker_connection.publish(ot.output_topic, output_message)
                print('OUTPUT: ' + output_message)
