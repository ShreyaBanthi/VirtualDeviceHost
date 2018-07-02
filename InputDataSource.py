from datetime import datetime


# self updating
class InputDataSource:
    name = 'unnamed'
    broker_connection_name = ''
    source_topic = ''
    data_type = 'json'  # json or raw
    ring_buffer_size = 5
    last_data_snapshot = None
    last_data_snapshot_timestamp = None

    def __init__(self, name, broker_connection_name, source_topic, data_type, ring_buffer_size):
        self.name = name
        self.broker_connection_name = broker_connection_name
        self.source_topic = source_topic
        self.data_type = data_type
        self.ring_buffer_size = ring_buffer_size

    def handle_input_message(self, topic, msg):
        if self.source_topic != topic:
            print('WARNING, mismatching topic')
        print("INPUT: " + msg.topic + " " + str(msg.payload))
        self.last_data_snapshot = msg.payload
        self.last_data_snapshot_timestamp = datetime.now().time()
        # use aggregator here?

    def has_received_snapshot(self):
        return self.last_data_snapshot is not None
