from VirtualDeviceRepository import VirtualDeviceRepository
from Monitoring.DeviceHealthPublisher import DeviceHealthPublisher
from ConfigurationManager import ConfigurationManager
from BrokerConnectionRepository import BrokerConnectionRepository


class TestApp:
    virtual_device_repository = None
    broker_connection_repository = None
    device_health_publisher = None

    def on_handle_message(self, broker_connection, topic, msg):
        virtual_devices = self.virtual_device_repository.get_all_virtual_devices()
        for vd in virtual_devices:
            vd.handle_mqtt_message(broker_connection, topic, msg)

    def __init__(self):
        print("Started")

        configuration_manager = ConfigurationManager()
        configuration = configuration_manager.find_configuration('Scenario1ConfigurationFactory')
        # configuration = TestConfigurationFactory()

        self.virtual_device_repository = VirtualDeviceRepository()
        self.broker_connection_repository = BrokerConnectionRepository()

        broker_connections = configuration.create_broker_connections()
        for bc in broker_connections:
            self.broker_connection_repository.add_broker_connection(bc)

        # self.initialize_virtual_devices()
        virtual_devices = configuration.create_virtual_devices()
        for vd in virtual_devices:
            self.virtual_device_repository.add_virtual_device(vd)

        device_health_publisher_broker_connection = self.broker_connection_repository.get_broker_connection(
            configuration.get_device_health_broker_connection())
        self.device_health_publisher = DeviceHealthPublisher(self.virtual_device_repository,
                                                             device_health_publisher_broker_connection,
                                                             configuration.get_device_health_topic(), 5)

        print('Now listening')

        # self.broker_connection.start_receiving(self.on_handle_message)
        for bc in self.broker_connection_repository.get_all_broker_connections():
            bc.start_receiving(self.on_handle_message)

        virtual_devices = self.virtual_device_repository.get_all_virtual_devices()
        for vd in virtual_devices:
            vd.start(self.broker_connection_repository)

        self.device_health_publisher.start()

        input("Press Enter to exit...")

        for vd in virtual_devices:
            vd.stop()

        self.device_health_publisher.stop()

        for bc in self.broker_connection_repository.get_all_broker_connections():
            bc.stop_receiving()

        print('Exiting')


if __name__ == '__main__':
    my_TestApp = TestApp()
    print("done")
