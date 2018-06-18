from InputDataSource import InputDataSource


# sort of container
class VirtualDevice:
    name = 'unnamed'
    input_data_sources = []
    # virtual_values = []
    virtual_value_groups = []
    virtual_functions = []

    def __init__(self, name):
        self.name = name
        print('Virtual Device \"' + name + '\" created.')

    def start(self):
        for vvg in self.virtual_value_groups:
            vvg.start()

    def stop(self):
        for vvg in self.virtual_value_groups:
            vvg.stop()

    def handle_mqtt_message(self, topic, msg):
        for ids in self.input_data_sources:
            if ids.source_topic == topic:
                ids.handle_input_message(topic, msg)

    def add_input_data_source_raw(self, name, source_topic):
        self.input_data_sources.append(InputDataSource(name, source_topic))

    def add_input_data_source(self, input_data_sources):
        self.input_data_sources.append(input_data_sources)

    # def add_virtual_value(self, new_virtual_value):
    #    self.virtual_values.append(new_virtual_value)

    def add_virtual_value_group(self, new_virtual_value_group):
        self.virtual_value_groups.append(new_virtual_value_group)

    def add_virtual_function(self, new_virtual_function):
        self.virtual_functions.append(new_virtual_function)