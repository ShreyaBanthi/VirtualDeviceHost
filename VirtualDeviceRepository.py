class VirtualDeviceRepository:
    """manages transiently-stored virtual devices"""
    virtual_devices = None

    def __init__(self):
        self.virtual_devices = []

    def get_all_virtual_devices(self):
        return self.virtual_devices

    def add_virtual_device(self, new_virtual_device):
        for vd in self.virtual_devices:
            if vd.name == new_virtual_device.name:
                raise Exception('duplicate virtual device name!')
        self.virtual_devices.append(new_virtual_device)
