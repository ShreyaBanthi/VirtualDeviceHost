from ConfigurationStrategy import ConfigurationStrategy
from VirtualValues.VirtualValue import VirtualValue
from VirtualValues.InputDataSource import InputDataSource
from VirtualDevice import VirtualDevice
from VirtualValues.VirtualValueGroup import VirtualValueGroup
from BrokerConnection import BrokerConnection
from VirtualValues.GenerationStrategies.TimedGenerationStrategy import TimedGenerationStrategy
from VirtualValues.ParsingStrategies.JsonParsingStrategy import JsonParsingStrategy
from VirtualValues.AggregatorStrategies.AllBooleanValuesEqualValueAggregatorStrategy import \
    AllBooleanValuesEqualValueAggregatorStrategy
from VirtualValues.Packaging.StringReplacePackagerStrategy import StringReplacePackagerStrategy


class Scenario2ConfigurationStrategy(ConfigurationStrategy):
    def create_virtual_devices(self):
        vds = []

        vd = VirtualDevice('Building 1')

        vvg1 = VirtualValueGroup('facility-system/buildings/building/1', "output")
        vvg1.set_generation_strategy(TimedGenerationStrategy(5 * 60))
        vvg1.set_packager_strategy(StringReplacePackagerStrategy(
            '{all_doors_closed:$0, all_windows_closed:$1}'))

        # add virtual values
        vv1 = VirtualValue('All Doors Closed', '$0')
        vv1.add_input_data_source(InputDataSource('DoorSensor1', 'input', "jarvis/door/1/changes", 0,
                                                  JsonParsingStrategy('newState')))
        vv1.add_input_data_source(InputDataSource('DoorSensor2', 'input', "jarvis/door/2/changes", 0,
                                                  JsonParsingStrategy('newState')))
        vv1.set_aggregator_strategy(AllBooleanValuesEqualValueAggregatorStrategy('closed'))
        vvg1.add_virtual_value(vv1)

        vv2 = VirtualValue('All Windows Closed', '$1')
        vv2.add_input_data_source(InputDataSource('WindowSensor1', 'input', "jarvis/window/1/changes", 0,
                                                  JsonParsingStrategy('newState')))
        vv2.add_input_data_source(InputDataSource('WindowSensor2', 'input', "jarvis/window/2/changes", 0,
                                                  JsonParsingStrategy('newState')))
        vv2.add_input_data_source(InputDataSource('WindowSensor3', 'input', "jarvis/window/3/changes", 0,
                                                  JsonParsingStrategy('newState')))
        vv2.set_aggregator_strategy(AllBooleanValuesEqualValueAggregatorStrategy('closed'))
        vvg1.add_virtual_value(vv2)

        vd.add_virtual_value_group(vvg1)

        vds.append(vd)

        return vds

    def create_broker_connections(self):
        broker_connections = []

        input_connection = BrokerConnection("input", "192.168.99.55")
        broker_connections.append(input_connection)

        output_connection = BrokerConnection("output", "192.168.1.100")
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
