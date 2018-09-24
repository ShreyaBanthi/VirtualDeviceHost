import queue
import logging
from datetime import datetime

from VirtualValues.InputDataSet import InputDataSet


class InputDataSource:
    name = 'unnamed'
    broker_connection_name = ''
    source_topic = ''
    queue_size = 5
    parsing_strategy = None
    data_queue = None
    last_timestamp = None
    max_age_in_seconds = 0

    def __init__(self, name, broker_connection_name, source_topic, parsing_strategy, queue_size=0, max_age_in_seconds=0):
        self.name = name
        self.broker_connection_name = broker_connection_name
        self.source_topic = source_topic
        self.queue_size = queue_size
        self.max_age_in_seconds = max_age_in_seconds
        self.parsing_strategy = parsing_strategy
        self.data_queue = queue.Queue(queue_size)

    def handle_input_message(self, topic, msg):
        if self.source_topic != topic:
            logging.warning('WARNING, mismatching topic')
        timestamp = datetime.now()
        parsed_value = self.parsing_strategy.parse(msg.payload)
        data_set = InputDataSet(self, timestamp, parsed_value)
        # if full ..
        if self.data_queue.full():
            # .. remove oldest element
            self.data_queue.get()
        self.data_queue.put(data_set)
        self.last_timestamp = timestamp
        logging.debug('INPUT: ' + str(msg.payload))

    def received_new_data(self):
        return self.data_queue.qsize() > 0

    def pop_from_queue(self):
        return self.data_queue.get()
