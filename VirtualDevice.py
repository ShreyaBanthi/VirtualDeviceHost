from VirtualValues.InputDataSource import InputDataSource


# sort of container
class VirtualDevice:
    name = 'unnamed'
    # input_data_sources = []
    # virtual_values = []
    virtual_value_groups = []
    virtual_functions = []

    def __init__(self, name):
        self.name = name
        print('Virtual Device \"' + name + '\" created.')

    def start(self, broker_connection_repository):
        for vvg in self.virtual_value_groups:
            vvg.set_broker_connection_repository(broker_connection_repository)
            vvg.start()
        for vf in self.virtual_functions:
            vf.set_broker_connection_repository(broker_connection_repository)

    def stop(self):
        for vvg in self.virtual_value_groups:
            vvg.stop()

    def handle_mqtt_message(self, broker_connection, topic, msg):
        # for ids in self.input_data_sources:
        #     if ids.source_topic == topic and ids.broker_connection_name == broker_connection.connection_name:
        #         ids.handle_input_message(topic, msg)
        for vvg in self.virtual_value_groups:
            vvg.handle_input_message(broker_connection, topic, msg)
        for vf in self.virtual_functions:
            if vf.trigger_broker_connection_name == broker_connection.connection_name and vf.trigger_topic == topic:
                vf.handle_trigger_message(broker_connection, topic, msg)

    # def add_input_data_source_raw(self, name, source_topic):
    #     self.input_data_sources.append(InputDataSource(name, source_topic))

    # def add_input_data_source(self, input_data_sources):
    #     self.input_data_sources.append(input_data_sources)

    # def add_virtual_value(self, new_virtual_value):
    #    self.virtual_values.append(new_virtual_value)

    def add_virtual_value_group(self, new_virtual_value_group):
        self.virtual_value_groups.append(new_virtual_value_group)

    def add_virtual_function(self, new_virtual_function):
        self.virtual_functions.append(new_virtual_function)