class InputDataSet:
    input_data_source = None
    receive_timestamp = None
    parsed_data = ''

    def __init__(self, input_data_source, receive_timestamp, parsed_data):
        self.input_data_source = input_data_source
        self.receive_timestamp = receive_timestamp
        self.parsed_data = parsed_data
