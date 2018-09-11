class VirtualDeviceRepository:
    _virtual_devices = []

    def __init__(self):
        pass

    def get_all_virtual_devices(self):
        return self._virtual_devices

    def add_virtual_device(self, new_virtual_device):
        for vd in self._virtual_devices:
            if vd.name == new_virtual_device.name:
                raise Exception('duplicate virtual device name!')
        self._virtual_devices.append(new_virtual_device)
