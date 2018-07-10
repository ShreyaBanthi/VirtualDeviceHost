from datetime import datetime
import queue

from VirtualValues.InputDataSet import InputDataSet


# self updating
class InputDataSource:
    name = 'unnamed'
    broker_connection_name = ''
    source_topic = ''
    queue_size = 5
    # last_data_snapshot = None
    # last_data_snapshot_timestamp = None
    parsing_strategy = None
    data_queue = None
    last_timestamp = None

    def __init__(self, name, broker_connection_name, source_topic, queue_size, parsing_strategy):
        self.name = name
        self.broker_connection_name = broker_connection_name
        self.source_topic = source_topic
        self.queue_size = queue_size
        self.parsing_strategy = parsing_strategy
        self.data_queue = queue.Queue(queue_size)  # TODO: implement max size

    def handle_input_message(self, topic, msg):
        if self.source_topic != topic:
            print('WARNING, mismatching topic')
        print("INPUT: " + msg.topic + " " + str(msg.payload))
        timestamp = datetime.now().time()
        # self.last_data_snapshot = msg.payload
        # self.last_data_snapshot_timestamp = timestamp
        parsed_value = self.parsing_strategy.parse(msg.payload)
        data_set = InputDataSet(self, timestamp, parsed_value)
        # if full
        if self.data_queue.full():
            # remove oldest element
            self.data_queue.get()
        self.data_queue.put(data_set)
        self.last_timestamp = timestamp

    # def has_received_snapshot(self):
    #     return self.last_data_snapshot is not None

    def received_new_data(self):
        return self.data_queue.qsize() > 0

    def pop_from_queue(self):
        return self.data_queue.get()
