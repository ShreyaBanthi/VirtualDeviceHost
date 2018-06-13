from VirtualValue import VirtualValue
from InputDataSource import InputDataSource
from VirtualDevice import VirtualDevice
from BrokerConnection import BrokerConnection
from TestConfiguration import TestConfiguration
from VirtualDeviceRepository import VirtualDeviceRepository
from DeviceHealthPublisher import DeviceHealthPublisher


class TestApp:
    broker_connection = None
    virtual_device_repository = None
    device_health_publisher = None

    def on_handle_message(self, topic, msg):
        virtual_devices = self.virtual_device_repository.get_all_virtual_devices()
        for vd in virtual_devices:
            vd.handle_mqtt_message(topic, msg)

    # create virtual device instances from ontology
    def initialize_virtual_devices(self):
        vd = TestConfiguration.create_test_virtual_device(self.broker_connection)

        self.virtual_device_repository.add_virtual_device(vd)

    def __init__(self):
        print("Started")

        self.virtual_device_repository = VirtualDeviceRepository()

        self.broker_connection = BrokerConnection("192.168.99.55", self.on_handle_message)

        self.initialize_virtual_devices();

        self.device_health_publisher = DeviceHealthPublisher(self.virtual_device_repository, self.broker_connection,
                                                             'maproject/health/device-states', 5)

        print('Now listening')

        self.broker_connection.start_receiving()


if __name__ == '__main__':
    my_TestApp = TestApp()
    print("done")
