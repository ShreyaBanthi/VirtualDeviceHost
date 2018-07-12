from VirtualDeviceHost import VirtualDeviceHost


class TestApp:
    def __init__(self):
        print("Started")
        virtual_device_host = VirtualDeviceHost()
        virtual_device_host.initialize('Scenario1ConfigurationFactory')
        # virtual_device_host.initialize('Scenario2ConfigurationFactory')
        # virtual_device_host.initialize('Scenario6ConfigurationFactory')

        print('Now listening')

        virtual_device_host.start()

        input("Press Enter to exit...")

        virtual_device_host.stop()

        print('Exiting')


if __name__ == '__main__':
    my_TestApp = TestApp()
    print("done")
