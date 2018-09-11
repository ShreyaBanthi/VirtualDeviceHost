import threading
import uuid
import logging


from Utilities import every, is_number


class VirtualValueGroup:
    id = ''
    output_topic = ''
    virtual_values = None
    broker_connection_name = None
    broker_connection_repository = None
    worker_thread = None
    generation_strategy = None
    packager_strategy = None
    is_active = False
    wait_event = None
    qos_level = 0

    def __init__(self, output_topic, broker_connection_name, qos_level):
        self.id = str(uuid.uuid4())
        self.qos_level = qos_level
        self.output_topic = output_topic
        self.broker_connection_name = broker_connection_name
        self.virtual_values = []
        self.worker_thread = threading.Thread(target=lambda: self.handle_work())
        self.worker_thread.setDaemon(True)  # no longer necessary because of is_active
        self.wait_event = threading.Event()

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def set_broker_connection_repository(self, broker_connection_repository):
        self.broker_connection_repository = broker_connection_repository

    def set_generation_strategy(self, generation_strategy):
        self.generation_strategy = generation_strategy
        self.generation_strategy.set_virtual_value_group(self)

    def set_packager_strategy(self, packager_strategy):
        self.packager_strategy = packager_strategy

    def start(self):
        if self.packager_strategy is None:
            raise Exception('no packager strategy defined!')

        self.is_active = True
        self.worker_thread.start()
        self.generation_strategy.start()

    def stop(self):
        self.is_active = False
        self.wait_event.set()  # so thread can stop gracefully

    def add_virtual_value(self, new_virtual_value):
        self.virtual_values.append(new_virtual_value)

    def generate(self):
        logging.info('generating virtual value group')
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
        # TODO: ggf. deduplicaten? if same as before, maybe not publish
        self.publish(msg)
        logging.info('OUTPUT: ' + msg)

    def set_wait_event(self):
        self.wait_event.set()

    def publish(self, message):
        logging.info('OUTPUT: ' + message)
        broker_connection = self.broker_connection_repository.get_broker_connection(self.broker_connection_name)
        broker_connection.publish(self.output_topic, message, self.qos_level)

    def handle_input_message(self, broker_connection, topic, msg):
        # if self.trigger_broker_connection_name != broker_connection.connection_name or self.trigger_topic != topic:
        #     return
        # self.execute(msg)
        new_data_received = False
        for vv in self.virtual_values:
            for ids in vv.input_data_sources:
                if ids.broker_connection_name == broker_connection.connection_name and ids.source_topic == topic:
                    ids.handle_input_message(topic, msg)
                    new_data_received = True
        # TODO: check if  data input sources need data
        # TODO: if yes, then: self.wait_event.set()
        if new_data_received:
            self.wait_event.set()

    def handle_work(self):
        while self.is_active:
            # print('handle_work for ' + self.output_topic)
            # aggregate values
            for vv in self.virtual_values:
                vv.run_aggregator()
            if self.generation_strategy.should_generate():
                synthesized_values = {}
                for vv in self.virtual_values:
                    synthesized_value = vv.synthesize_value()
                    synthesized_values[vv] = synthesized_value
                msg = self.packager_strategy.package(self.virtual_values, synthesized_values)
                self.publish(msg)
            self.wait_event.wait()
            self.wait_event.clear()
