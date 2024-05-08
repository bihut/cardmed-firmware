import re
import subprocess


class Services:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


    @staticmethod
    def connect_wifi(wifi_ssid,wifi_password):
        # Crear el archivo de configuración de wpa_supplicant
        config_content = f"""
            country=US
            ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
            update_config=1

            network={{
                ssid="{wifi_ssid}"
                psk="{wifi_password}"
            }}
            """

        # Guardar el archivo de configuración
        with open("/etc/wpa_supplicant/wpa_supplicant.conf", "w") as f:
            f.write(config_content)

        # Reiniciar el servicio de wpa_supplicant para que tome la nueva configuración
        subprocess.run(["sudo", "systemctl", "restart", "wpa_supplicant"])

    @staticmethod
    def turnOffWifi(iface="wlan0"):
        try:
            # Desactivar la interfaz de red
            subprocess.run(["sudo", "ifconfig", iface, "down"])
            #print("Desconexión exitosa")
            return True
        except subprocess.CalledProcessError:
            #print("Error al desconectar del WiFi")
            return False

    @staticmethod
    def turnOnWifi(iface="wlan0"):
        try:
            # Activar la interfaz de red
            subprocess.run(["sudo", "ifconfig", iface, "up"])
            return True

        except subprocess.CalledProcessError:
            return False
    @staticmethod
    def turnOffBluetooth(iface="hci0"):
        try:
            # Apagar el adaptador Bluetooth
            subprocess.run(["sudo", "hciconfig", iface, "down"])
            print("Bluetooth apagado correctamente")
        except subprocess.CalledProcessError:
            print("Error al apagar el adaptador Bluetooth")
    @staticmethod
    def turnOnBluetooth(iface="hci0"):
        try:
            # Encender el adaptador Bluetooth
            subprocess.run(["sudo", "hciconfig", iface, "up"])
            print("Bluetooth encendido correctamente")
        except subprocess.CalledProcessError:
            print("Error al encender el adaptador Bluetooth")
    @staticmethod
    def connectedNetwork():
        try:
            # Obtener la configuración de la interfaz de red
            output = subprocess.check_output(["iwgetid", "-r"])
            ssid = output.strip().decode("utf-8")

            # Si la salida está vacía, no estás conectado a ninguna red
            if not ssid:
                return None#"No conectado a ninguna red WiFi"
            else:
                return ssid

        except subprocess.CalledProcessError:
            return None#"Error al obtener la red WiFi conectada"
    @staticmethod
    def delete_connected_network(ssid):
        # Ruta al archivo de configuración de wpa_supplicant
        config_file = "/etc/wpa_supplicant/wpa_supplicant.conf"

        try:
            # Leer el contenido del archivo de configuración
            with open(config_file, "r") as f:
                lines = f.readlines()

            # Buscar la sección de la red a eliminar
            start_idx = None
            end_idx = None
            for i, line in enumerate(lines):
                if ssid in line:
                    start_idx = i
                if start_idx is not None and "}" in line:
                    end_idx = i
                    break

            if start_idx is not None and end_idx is not None:
                # Eliminar las líneas correspondientes a la red
                del lines[start_idx:end_idx + 1]

                # Escribir el archivo actualizado
                with open(config_file, "w") as f:
                    f.writelines(lines)

                print(f"Red '{ssid}' eliminada del archivo de configuración")
            else:
                print(f"No se encontró la red '{ssid}' en el archivo de configuración")

        except FileNotFoundError:
            print("El archivo de configuración de wpa_supplicant no se encontró")