import dbus

# Conectar al bus de sesión de D-Bus
session_bus = dbus.SessionBus()

# Reemplaza con la dirección del dispositivo Bluetooth de la Raspberry Pi Zero
device_address = "B8:27:EB:71:60:A0"

# Obtener el proxy para el dispositivo Bluetooth
device_path = f"/org/bluez/hci0/dev_{device_address.replace(':', '_')}"
device_obj = session_bus.get_object("org.bluez", device_path)
device_intf = dbus.Interface(device_obj, "org.bluez.Device1")

# Obtener la interfaz GATT del dispositivo
gatt_manager = dbus.Interface(device_obj, "org.bluez.GattManager1")
adapters = gatt_manager.GetAdapters()
adapter_path = adapters[0]
gatt_adapter = session_bus.get_object("org.bluez", adapter_path)
gatt_manager = dbus.Interface(gatt_adapter, "org.bluez.GattManager1")

# Reemplaza con el UUID del servicio al que deseas enviar información
service_uuid = "00000001-0000-1000-8000-00805f9b34fb"

# Obtener la interfaz GATT del servicio
service_path = device_intf.FindService(service_uuid)
service_obj = session_bus.get_object("org.bluez", service_path)
service_intf = dbus.Interface(service_obj, "org.bluez.GattService1")

# Reemplaza con el UUID de la característica a la que deseas enviar información
characteristic_uuid = "00000002-0000-1000-8000-00805f9b34fb"

# Obtener la interfaz GATT de la característica
characteristic_path = service_intf.FindCharacteristic(characteristic_uuid)
characteristic_obj = session_bus.get_object("org.bluez", characteristic_path)
characteristic_intf = dbus.Interface(characteristic_obj, "org.bluez.GattCharacteristic1")

# Convertir la información a bytes y enviarla a través de WriteValue
data_to_send = "Hello, Raspberry Pi!".encode("utf-8")
characteristic_intf.WriteValue(data_to_send, {})

print("Data sent successfully.")
