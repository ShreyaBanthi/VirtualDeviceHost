from ConfigurationFactory import ConfigurationFactory
from VirtualValues.VirtualValue import VirtualValue
from VirtualValues.InputDataSource import InputDataSource
from VirtualDevice import VirtualDevice
from VirtualValues.VirtualValueGroup import VirtualValueGroup
from BrokerConnection import BrokerConnection
from VirtualValues.AggregatorStrategies.BasicFloatAverageAggregatorStrategy import BasicFloatAverageAggregatorStrategy
# from VirtualValues.SynthesisStrategies.MaximumSyntStrategy import MaximumSyntStrategy
# from VirtualValues.SynthesisStrategies.MovingAverageSyntStrategy import MovingAverageSyntStrategy
from VirtualValues.Packaging.StringReplacePackagerStrategy import StringReplacePackagerStrategy
# from SynthesisStrategies import *
from VirtualValues.GenerationStrategies.TimedGenerationStrategy import TimedGenerationStrategy
from VirtualValues.GenerationStrategies.OnDataReceivedGenerationStrategy import OnDataReceivedGenerationStrategy
from VirtualValues.ParsingStrategies.JsonParsingStrategy import JsonParsingStrategy
from VirtualValues.ParsingStrategies.RawParsingStrategy import RawParsingStrategy
from VirtualValues.AggregatorStrategies.FloatMaximumAggregatorStrategy import FloatMaximumAggregatorStrategy
from VirtualValues.AggregatorStrategies.FloatMinimumAggregatorStrategy import FloatMinimumAggregatorStrategy

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

        vvg1 = VirtualValueGroup('facility-system/temperature/room-1', "input")
        # vvg1.set_generation_strategy(TimedGenerationStrategy(5))
        vvg1.set_generation_strategy(OnDataReceivedGenerationStrategy())
        vvg1.set_packager_strategy(StringReplacePackagerStrategy(
            '{measured_temperature:$0, max_temperature:$1, min_temperature:$2, moving_average_temperature:$2}'))

        # add virtual values
        vv1 = VirtualValue('Current Temperature Value', '$0')
        vv1.add_input_data_source(InputDataSource('EnvironmentSensor1', 'input', "maproject/environment/2/updates",
                                                  5, JsonParsingStrategy("temperature")))
        vv1.add_input_data_source(InputDataSource("TemperatureSensor1", "input", "maproject/temperature/2/updates",
                                                  5, RawParsingStrategy()))
        vv1.set_aggregator_strategy(BasicFloatAverageAggregatorStrategy())
        vvg1.add_virtual_value(vv1)

        vv2 = VirtualValue('Maximum Temperature Value', '$1')
        vv2.add_input_data_source(InputDataSource('EnvironmentSensor1', 'input', "maproject/environment/2/updates",
                                                  5, JsonParsingStrategy("temperature")))
        vv2.add_input_data_source(InputDataSource("TemperatureSensor1", "input", "maproject/temperature/2/updates",
                                                  5, RawParsingStrategy()))
        vv2.set_synthesis_strategy(FloatMaximumAggregatorStrategy())
        vvg1.add_virtual_value(vv2)

        vv3 = VirtualValue('Minimum Temperature Value', '$2')
        vv3.add_input_data_source(InputDataSource('EnvironmentSensor1', 'input', "maproject/environment/2/updates",
                                                  5, JsonParsingStrategy("temperature")))
        vv3.add_input_data_source(InputDataSource("TemperatureSensor1", "input", "maproject/temperature/2/updates",
                                                  5, RawParsingStrategy()))
        vv3.set_synthesis_strategy(FloatMinimumAggregatorStrategy())
        vvg1.add_virtual_value(vv3)

        # vv4 = VirtualValue('Moving Average Temperature Value', '$3')
        # vv4.add_mapping(ids1, 'temperature')
        # vv4.add_mapping(ids2, '')
        # vv4.set_synthesis_strategy(MovingAverageSyntStrategy(12))
        # vvg1.add_virtual_value(vv4)

        vd.add_virtual_value_group(vvg1)

        vds.append(vd)

        return vds

    def create_broker_connections(self):
        broker_connections = []

        input_connection = BrokerConnection("input", "192.168.1.100")
        broker_connections.append(input_connection)

        output_connection = BrokerConnection("output", "192.168.1.100")
        broker_connections.append(output_connection)

        return broker_connections

    def is_device_health_monitoring_enabled(self):
        return True
