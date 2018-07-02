import threading
import uuid

from Utilities import every, is_number


class VirtualValueGroup:
    id = ''
    output_topic = ''
    push_cycle_in_s = 0
    message_template = ''
    virtual_values = []
    broker_connection_name = None
    broker_connection_repository = None
    thread = None
    packager_strategy = None

    def __init__(self, output_topic, push_cycle_in_s, message_template, broker_connection_name):
        self.id = str(uuid.uuid4())
        self.output_topic = output_topic
        self.push_cycle_in_s = push_cycle_in_s
        self.message_template = message_template
        self.broker_connection_name = broker_connection_name
        self.thread = threading.Thread(target=lambda: every(self.push_cycle_in_s, self.generate))
        self.thread.setDaemon(True)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def set_broker_connection_repository(self, broker_connection_repository):
        self.broker_connection_repository = broker_connection_repository

    def set_packager_strategy(self, packager_strategy):
        self.packager_strategy = packager_strategy

    def start(self):
        self.thread.start()

    def stop(self):
        # self.thread.stop()
        pass

    def add_virtual_value(self, new_virtual_value):
        self.virtual_values.append(new_virtual_value)

    def generate(self):
        print('generate')
        # msg = self.message_template
        # for vv in self.virtual_values:
#             values = vv.aggregate_values()
#             synthesized_value = vv.synthesize_value(values)
#             msg = msg.replace(vv.message_template_symbol, str(synthesized_value))
        synthesized_values = {}
        for vv in self.virtual_values:
            values = vv.aggregate_values()
            synthesized_value = vv.synthesize_value(values)
            synthesized_values[vv] = synthesized_value
        msg = self.packager_strategy.package(self.virtual_values, synthesized_values)
        self.publish(msg)
        print('OUTPUT: ' + msg)

    def publish(self, message):
        broker_connection = self.broker_connection_repository.get_broker_connection(self.broker_connection_name)
        broker_connection.publish(self.output_topic, message)
