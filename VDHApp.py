import sys
import logging
from VirtualDeviceHost import VirtualDeviceHost


class VDHApp:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        # logging.basicConfig(level=logging.DEBUG)

        if len(sys.argv) != 2:
            logging.error('ERROR: Invalid configuration. Enter active configuration as command line argument.')
            return

        virtual_device_host = VirtualDeviceHost()
        logging.info('active configuration: ' + sys.argv[1])
        virtual_device_host.initialize(sys.argv[1])
        # virtual_device_host.initialize('Scenario5ConfigurationStrategy')

        virtual_device_host.start()

        logging.info('VirtualDeviceHost now running')
        logging.info('Press ENTER to exit...')
        input()

        virtual_device_host.stop()

        logging.info('Exiting')


if __name__ == '__main__':
    app = VDHApp()
