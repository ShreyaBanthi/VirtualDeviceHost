import sys
import logging
from VirtualDeviceHost import VirtualDeviceHost


class VDHApp:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        # logging.basicConfig(level=logging.DEBUG)

        if len(sys.argv) != 2:
            print('ERROR: Invalid configuration. Enter active configuration as command line argument.')
            return

        print("Started")
        virtual_device_host = VirtualDeviceHost()
        print("Configuration: " + sys.argv[1])
        virtual_device_host.initialize(sys.argv[1])

        print('Now listening')

        virtual_device_host.start()

        input("Press Enter to exit...")

        virtual_device_host.stop()

        print('Exiting')


if __name__ == '__main__':
    app = VDHApp()
    print("done")
