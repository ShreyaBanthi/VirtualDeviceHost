import threading

from Utilities import every, is_number


class VirtualValueGroup:
    output_topic = ''
    push_cycle_in_s = 0
    message_template = ''
    virtual_values = []
    broker_connection_name = None
    broker_connection_repository = None
    thread = None

    def __init__(self, output_topic, push_cycle_in_s, message_template, broker_connection_name):
        self.output_topic = output_topic
        self.push_cycle_in_s = push_cycle_in_s
        self.message_template = message_template
        self.broker_connection_name = broker_connection_name
        self.thread = threading.Thread(target=lambda: every(self.push_cycle_in_s, self.generate))
        self.thread.setDaemon(True)

    def set_broker_connection_repository(self, broker_connection_repository):
        self.broker_connection_repository = broker_connection_repository

    def start(self):
        self.thread.start()

    def stop(self):
        # self.thread.stop()
        pass

    def add_virtual_value(self, new_virtual_value):
        self.virtual_values.append(new_virtual_value)

    def generate(self):
        print('generate');
        msg = self.message_template
        for vv in self.virtual_values:
            values = vv.aggregate_values()
            synthesized_value = vv.synthesize_value(values);
            msg = msg.replace(vv.message_template_symbol, str(synthesized_value))
        self.publish(msg);
        print('generated message sent: ' + msg)

    def publish(self, message):
        broker_connection = self.broker_connection_repository.get_broker_connection(self.broker_connection_name)
        broker_connection.publish(self.output_topic, message)
