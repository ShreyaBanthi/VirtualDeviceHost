from datetime import timedelta
from ConfigurationStrategy import ConfigurationStrategy
from VirtualValues.VirtualValue import VirtualValue
from VirtualValues.InputDataSource import InputDataSource
from VirtualDevice import VirtualDevice
from VirtualValues.VirtualValueGroup import VirtualValueGroup
from BrokerConnection import BrokerConnection
from VirtualValues.AggregatorStrategies.BasicFloatAverageAggregatorStrategy import BasicFloatAverageAggregatorStrategy
from VirtualValues.Packaging.StringReplacePackagerStrategy import StringReplacePackagerStrategy
from VirtualValues.GenerationStrategies.TimedGenerationStrategy import TimedGenerationStrategy
from VirtualValues.ParsingStrategies.JsonParsingStrategy import JsonParsingStrategy
from VirtualValues.ParsingStrategies.RawParsingStrategy import RawParsingStrategy
from VirtualValues.AggregatorStrategies.FloatMaximumAggregatorStrategy import FloatMaximumAggregatorStrategy
from VirtualValues.AggregatorStrategies.FloatMinimumAggregatorStrategy import FloatMinimumAggregatorStrategy
from VirtualValues.AggregatorStrategies.MovingAverageAggregatorStrategy import MovingAverageAggregatorStrategy


class Scenario8ConfigurationStrategy(ConfigurationStrategy):
    def create_virtual_devices(self):
        vds = []
        vd = VirtualDevice('Room 1 Temperature Monitor')

        vvg1 = VirtualValueGroup('facility-system/temperature/room-1', "output")
        vvg1.set_generation_strategy(TimedGenerationStrategy(5))
        vvg1.set_packager_strategy(StringReplacePackagerStrategy(
            '{"average_temperature":$0, "max_temperature":$1, "min_temperature":$2, "moving_average_temperature":$3}'))

        # add virtual values
        vv1 = VirtualValue('Current Temperature Value', '$0')
        vv1.add_input_data_source(InputDataSource('EnvironmentSensor1', 'input', "maproject/environment/2/updates",
                                                  JsonParsingStrategy("temperature")))
        vv1.add_input_data_source(InputDataSource("TemperatureSensor20", "input", "maproject/temperature/20/updates",
                                                  RawParsingStrategy()))
        vv1.add_input_data_source(InputDataSource("TemperatureSensor21", "input", "maproject/temperature/21/updates",
                                                  RawParsingStrategy()))
        vv1.add_input_data_source(InputDataSource("TemperatureSensor22", "input", "maproject/temperature/22/updates",
                                                  RawParsingStrategy()))
        vv1.set_aggregator_strategy(BasicFloatAverageAggregatorStrategy())
        vvg1.add_virtual_value(vv1)

        vv2 = VirtualValue('Maximum Temperature Value', '$1')
        vv2.add_input_data_source(InputDataSource('EnvironmentSensor1', 'input', "maproject/environment/2/updates",
                                                  JsonParsingStrategy("temperature")))
        vv2.add_input_data_source(InputDataSource("TemperatureSensor20", "input", "maproject/temperature/20/updates",
                                                  RawParsingStrategy()))
        vv2.add_input_data_source(InputDataSource("TemperatureSensor21", "input", "maproject/temperature/21/updates",
                                                  RawParsingStrategy()))
        vv2.add_input_data_source(InputDataSource("TemperatureSensor22", "input", "maproject/temperature/22/updates",
                                                  RawParsingStrategy()))
        vv2.set_aggregator_strategy(FloatMaximumAggregatorStrategy())
        vvg1.add_virtual_value(vv2)

        vv3 = VirtualValue('Minimum Temperature Value', '$2')
        vv3.add_input_data_source(InputDataSource('EnvironmentSensor1', 'input', "maproject/environment/2/updates",
                                                 JsonParsingStrategy("temperature")))
        vv3.add_input_data_source(InputDataSource("TemperatureSensor20", "input", "maproject/temperature/20/updates",
                                                  RawParsingStrategy()))
        vv3.add_input_data_source(InputDataSource("TemperatureSensor21", "input", "maproject/temperature/21/updates",
                                                  RawParsingStrategy()))
        vv3.add_input_data_source(InputDataSource("TemperatureSensor22", "input", "maproject/temperature/22/updates",
                                                  RawParsingStrategy()))
        vv3.set_aggregator_strategy(FloatMinimumAggregatorStrategy())
        vvg1.add_virtual_value(vv3)

        vv4 = VirtualValue('Moving Average Temperature Value', '$3')
        vv4.add_input_data_source(InputDataSource('EnvironmentSensor1', 'input', "maproject/environment/2/updates",
                                                  JsonParsingStrategy("temperature")))
        vv4.add_input_data_source(InputDataSource("TemperatureSensor20", "input", "maproject/temperature/20/updates",
                                                  RawParsingStrategy()))
        vv4.add_input_data_source(InputDataSource("TemperatureSensor21", "input", "maproject/temperature/21/updates",
                                                  RawParsingStrategy()))
        vv4.add_input_data_source(InputDataSource("TemperatureSensor22", "input", "maproject/temperature/22/updates",
                                                  RawParsingStrategy()))
        vv4.set_aggregator_strategy(MovingAverageAggregatorStrategy())
        vvg1.add_virtual_value(vv4)

        vd.add_virtual_value_group(vvg1)

        vds.append(vd)

        return vds

    def create_broker_connections(self):
        broker_connections = []

        input_connection = BrokerConnection("input", "192.168.1.100")
        broker_connections.append(input_connection)

        output_connection = BrokerConnection("output", "23.100.9.44")
        broker_connections.append(output_connection)

        return broker_connections

    def is_monitoring_enabled(self):
        return False

    def get_monitoring_grace_period_duration(self):
        return None

    def get_monitoring_broker_connection(self):
        return None

    def get_monitoring_output_topic(self):
        return None
