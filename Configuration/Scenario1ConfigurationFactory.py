from ConfigurationFactory import ConfigurationFactory
from VirtualValue import VirtualValue
from InputDataSource import InputDataSource
from VirtualDevice import VirtualDevice
from VirtualValueGroup import VirtualValueGroup
from BrokerConnection import BrokerConnection
from SynthesisStrategies.MaximumSyntStrategy import MaximumSyntStrategy
from SynthesisStrategies.MovingAverageSyntStrategy import MovingAverageSyntStrategy
from VirtualValues.Packaging.StringReplacePackagerStrategy import StringReplacePackagerStrategy
# from SynthesisStrategies import *

# import SynthesisStrategies
# import VirtualValues.Packaging


class Scenario1ConfigurationFactory(ConfigurationFactory):
    def get_device_health_broker_connection(self):
        return 'output'

    def get_device_health_topic(self):
        return 'maproject/health/device-states'

    def create_virtual_devices(self):
        vds = []
        vd = VirtualDevice('Room 12')

        # generate input data sources
        ids1 = InputDataSource('EnvironmentSensor1', 'input', "maproject/environment/2/updates", "json", 1)
        vd.add_input_data_source(ids1)
        ids2 = InputDataSource('TemperatureSensor1', 'input', "maproject/temperature/2/updates", "raw", 1)
        vd.add_input_data_source(ids2)

        vvg1 = VirtualValueGroup('facility-system/temperature/room-1', 5,
                                 '{measured_temperature:$0, max_temperature:$1, moving_average_temperature:$2}', "input")
        vvg1.set_packager_strategy(StringReplacePackagerStrategy(
            '{measured_temperature:$0, max_temperature:$1, moving_average_temperature:$2}'))

        # add virtual values
        vv1 = VirtualValue('Current Temperature Value', '$0')
        vv1.add_mapping(ids1, 'temperature')
        vv1.add_mapping(ids2, '')
        vvg1.add_virtual_value(vv1)

        vv2 = VirtualValue('Maximum Temperature Value', '$1')
        vv2.add_mapping(ids1, 'temperature')
        vv2.add_mapping(ids2, '')
        vv2.set_synthesis_strategy(MaximumSyntStrategy())
        vvg1.add_virtual_value(vv2)

        vv3 = VirtualValue('Moving Average Temperature Value', '$2')
        vv3.add_mapping(ids1, 'temperature')
        vv3.add_mapping(ids2, '')
        vv3.set_synthesis_strategy(MovingAverageSyntStrategy(12))
        vvg1.add_virtual_value(vv3)

        vd.add_virtual_value_group(vvg1)

        vds.append(vd)

        return vds

    def create_broker_connections(self):
        broker_connections = []

        input_connection = BrokerConnection("input", "192.168.1.3")
        broker_connections.append(input_connection)

        output_connection = BrokerConnection("output", "192.168.1.3")
        broker_connections.append(output_connection)

        return broker_connections

    def is_device_health_monitoring_enabled(self):
        return True
