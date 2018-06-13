class VirtualDeviceRepository:
    _virtual_devices = []

    def __init__(self):
        pass

    def get_all_virtual_devices(self):
        return self._virtual_devices

    def add_virtual_device(self, new_virtual_device):
        self._virtual_devices.append(new_virtual_device)
