import threading

from BrokerConnection import BrokerConnection
from VirtualDeviceRepository import VirtualDeviceRepository

from Utilities import every


class DeviceHealthPublisher:
    virtual_device_repository = None
    broker_connection = None
    publish_topic = ''
    publish_cycle_in_s = 60
    thread = None

    def __init__(self, virtual_device_repository, broker_connection, publish_topic, publish_cycle_in_s):
        self.virtual_device_repository = virtual_device_repository
        self.broker_connection = broker_connection
        self.publish_topic = publish_topic
        self.publish_cycle_in_s = publish_cycle_in_s
        self.thread = threading.Thread(target=lambda: every(publish_cycle_in_s, self.publish_health_state))
        self.thread.setDaemon(True)

    def start(self):
        self.thread.start()

    def stop(self):
        pass

    def publish_health_state(self):
        print('Publishing health state')
        self.broker_connection.publish(self.publish_topic, '{}')
