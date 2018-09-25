import logging
from datetime import datetime


class VirtualDevice:
    name = 'unnamed'
    virtual_value_groups = None
    virtual_functions = None

    def __init__(self, name):
        self.name = name
        self.virtual_value_groups = []
        self.virtual_functions = []
        logging.info('Virtual Device \"' + name + '\" created.')

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
        for vvg in self.virtual_value_groups:
            vvg.handle_input_message(broker_connection, topic, msg)

        for vf in self.virtual_functions:
            if vf.trigger_broker_connection_name == broker_connection.connection_name and vf.trigger_topic == topic:
                vf.handle_trigger_message(broker_connection, topic, msg)

    def add_virtual_value_group(self, new_virtual_value_group):
        self.virtual_value_groups.append(new_virtual_value_group)

    def add_virtual_function(self, new_virtual_function):
        self.virtual_functions.append(new_virtual_function)

    def check_if_healthy(self):
        timestamp = datetime.now()
        # loop through all virtual values in all virtual value groups
        for vvg in self.virtual_value_groups:
            for vv in vvg.virtual_values:
                for ids in vv.input_data_sources:
                    # if health monitoring disabled locally then ignore timestamps
                    if ids.max_age_in_seconds == 0:
                        continue
                    # if we never received data (since timestamp is not set) we can return unhealthy state
                    if ids.last_timestamp is None:
                        return False
                    # if timestamp of last received data is older than threshold then return unhealthy state
                    if (timestamp-ids.last_timestamp).total_seconds() > ids.max_age_in_seconds:
                        return False
        return True
