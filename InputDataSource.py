# self updating
class InputDataSource:
    name = 'unnamed'
    source_topic = ''
    data_type = 'json'  # json or raw
    ring_buffer_size = 5
    last_data_snapshot = '';

    def __init__(self, name, source_topic, data_type, ring_buffer_size):
        self.name = name
        self.source_topic = source_topic
        self.data_type = data_type
        self.ring_buffer_size = ring_buffer_size

    def handle_input_message(self, topic, msg):
        print(msg.topic + " " + str(msg.payload))
        self.last_data_snapshot = msg.payload;