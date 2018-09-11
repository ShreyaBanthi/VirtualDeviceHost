from VirtualDeviceHost import VirtualDeviceHost
import logging


class TestApp:
    def __init__(self):

        # assuming loglevel is bound to the string value obtained from the
        # command line argument. Convert to upper case to allow the user to
        # specify --log=DEBUG or --log=debug
        # numeric_level = getattr(logging, loglevel.upper(), None)
        # if not isinstance(numeric_level, int):
        #     raise ValueError('Invalid log level: %s' % loglevel)
        # logging.basicConfig(level=numeric_level, ...)

        # logging.basicConfig(level=logging.INFO)
        logging.basicConfig(level=logging.DEBUG)

        print("Started")
        virtual_device_host = VirtualDeviceHost()
        virtual_device_host.initialize('Scenario1ConfigurationStrategy')
        # virtual_device_host.initialize('Scenario2ConfigurationStrategy')
        # virtual_device_host.initialize('Scenario6ConfigurationStrategy')

        print('Now listening')

        virtual_device_host.start()

        input("Press Enter to exit...")

        virtual_device_host.stop()

        print('Exiting')


if __name__ == '__main__':
    my_TestApp = TestApp()
    print("done")
