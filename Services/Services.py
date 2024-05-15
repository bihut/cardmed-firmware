import os
import re
import subprocess

import netifaces as netifaces
#import pyiface as pyiface
import qrcode


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
            subprocess.run(["sudo", "nmcli", "radio","wifi", "off"])
            #print("Desconexión exitosa")
            return True
        except subprocess.CalledProcessError:
            #print("Error al desconectar del WiFi")
            return False

    @staticmethod
    def generateQRCode(texto, nombre_archivo):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,  # Aumenta el tamaño de la cuadrícula
            border=10,  # Aumenta el tamaño del borde
        )
        qr.add_data(texto)
        qr.make(fit=True)

        imagen_qr = qr.make_image(fill_color="black", back_color="white")
        imagen_qr.save(nombre_archivo)

    @staticmethod
    def turnOnWifi(iface="wlan0"):
        try:
            # Activar la interfaz de red
            subprocess.run(["sudo", "nmcli", "radio","wifi", "on"])
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
    def getConnectedNetwork():
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
    def runAndWait(command):
        try:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            #process.wait()
            #process.returncode, stdout.decode(), stderr.decode()
            var = process.returncode
            if var==0:
                return True,""
            return False,stdout.decode()+" -- "+stderr.decode()
        except Exception as e:
            return False, str(e)
    @staticmethod
    def connectWifi(ssid, password):
        state,msg=Services.runAndWait("sudo ifconfig wlan0 up")
        if state:
            state, msg = Services.runAndWait(
                "sudo raspi-config nonint do_wifi_ssid_passphrase '{}' '{}'".format(ssid, password))
            Services.runAndWait("sudo ifconfig wlan0 up")
        return state,msg
