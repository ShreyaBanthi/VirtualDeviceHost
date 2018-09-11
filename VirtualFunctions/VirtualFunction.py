import threading
import logging
import queue


class VirtualFunction:
    name = 'unnamed'
    trigger_broker_connection_name = ''
    trigger_topic = ''
    output_targets = None
    broker_connection_repository = None
    queue = None
    worker_thread = None

    def __init__(self, name, trigger_broker_connection_name, trigger_topic):
        self.name = name
        self.output_targets = []
        self.trigger_broker_connection_name = trigger_broker_connection_name
        self.trigger_topic = trigger_topic
        self.queue = queue.Queue()
        self.worker_thread = threading.Thread(target=lambda: self.handle_work())
        self.worker_thread.setDaemon(True)  # no longer necessary because of is_active

    def add_output_target(self, new_output_target):
        self.output_targets.append(new_output_target)

    def handle_trigger_message(self, broker_connection, topic, msg):
        if self.trigger_broker_connection_name != broker_connection.connection_name or self.trigger_topic != topic:
            return
        self.queue.put(msg)

    def set_broker_connection_repository(self, broker_connection_repository):
        self.broker_connection_repository = broker_connection_repository

    def handle_work(self):
        while True:
            try:
                msg = self.queue.get(block=True, timeout=5)
                if msg is not None:
                    self.execute(msg)
            except queue.Queue.Empty:
                pass

    def execute(self, msg):
        logging.info('executing virtual function')
        msg_string = str(msg.payload)
        logging.info('INPUT: ' + msg_string)
        for ot in self.output_targets:
            output_message = ot.generator_strategy.generate(msg_string)
            if ot is not None:
                broker_connection = self.broker_connection_repository.get_broker_connection(ot.output_broker_connection_name)
                broker_connection.publish(ot.output_topic, output_message)
                logging.info('OUTPUT: ' + output_message)
