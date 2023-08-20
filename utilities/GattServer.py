import dbus
import dbus.service
from gi.repository import GLib

class GattCharacteristic(dbus.service.Object):
    def __init__(self, bus, path, service):
        self.path = path
        self.bus = bus
        self.service = service

        dbus.service.Object.__init__(self, bus, path)

        self.value = dbus.Array([], signature='y')

    @dbus.service.method("org.bluez.GattCharacteristic1", in_signature="", out_signature="ay")
    def ReadValue(self):
        print("ReadValue called")
        return self.value

    @dbus.service.method("org.bluez.GattCharacteristic1", in_signature="ay", out_signature="")
    def WriteValue(self, new_value):
        print("WriteValue called with:", new_value)
        self.value = new_value

class GattService(dbus.service.Object):
    def __init__(self, bus, path):
        self.path = path
        self.bus = bus

        dbus.service.Object.__init__(self, bus, path)

        self.characteristic = GattCharacteristic(bus, path + "/char1", self)

    @dbus.service.method("org.bluez.GattService1", in_signature="s", out_signature="")
    def AddCharacteristic(self, characteristic_path):
        self.characteristic = GattCharacteristic(self.bus, characteristic_path, self)

class GattApplication(dbus.service.Object):
    def __init__(self, bus):
        self.path = "/"
        self.bus = bus

        dbus.service.Object.__init__(self, bus, self.path)
        self.add_service()

    def add_service(self):
        service = GattService(self.bus, self.path + "service0001")
        self.add_managed_object(service)
        service.AddCharacteristic(self.path + "service0001/char0001")

# Inicializar el bucle principal de GLib
loop = GLib.MainLoop()

# Inicializar la conexión D-Bus
system_bus = dbus.SystemBus()

# Crear la aplicación GATT
app = GattApplication(system_bus)

# Iniciar el bucle principal
loop.run()
