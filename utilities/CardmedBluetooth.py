
import subprocess
from getpass import getpass
import re
from utils.Utils import Utils


class CardmedBluetooth:
    def __init__(self) -> None:
        super().__init__()
        self.bluetoothState=True
        self.isOnCarmed = Utils.checkIfCardmedDevice()
    def turnOnBluetooth(self):
        try:
            # Run the bluetoothctl command to turn on Bluetooth
            #subprocess.run(["sudo","-A", "bluetoothctl", "power", "on"], check=True)
            if not self.isOnCarmed:
                password = getpass("Please enter your password: ")
                proc = subprocess.Popen("sudo -S bluetoothctl power on".split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                proc.communicate(password.encode())
            else:
                subprocess.run(["bluetoothctl", "power", "on"], check=True)
            print("Bluetooth turned on.")
            self.bluetoothState = True
        except subprocess.CalledProcessError as e:
            print("Error turning on Bluetooth:", e)
    def turnOffBluetooth(self):
        try:
            # Run the bluetoothctl command to turn on Bluetooth
            #password = getpass("Please enter your password: ")
            #subprocess.run(["sudo","-A", "bluetoothctl", "power", "off"], check=True)
            if not self.isOnCarmed:
                password = getpass("Please enter your password: ")
                proc = subprocess.Popen("sudo -S bluetoothctl power off".split(), stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                proc.communicate(password.encode())
            else:
                subprocess.run(["bluetoothctl", "power", "off"], check=True)
            self.bluetoothState = False
        except subprocess.CalledProcessError as e:
            print("Error turning off Bluetooth:", e)
    def listDevices(self):
        '''self.devices = bluetooth.discover_devices(duration=1, lookup_names=True, lookup_class=True)

        # Print discovered devices
        for addr, name, _ in self.devices:
            print(f"Device: {name} ({addr})")'''
        p = subprocess.Popen(["bluetoothctl", "devices"], stdout=subprocess.PIPE)
        out, err = p.communicate()
        p = re.compile(r'(?:[0-9a-fA-F]:?){12}')
        lines=out.decode("utf-8").split("\n")
        devices = []
        for line in lines:
            try:
                aux = line.replace("Device","")
                mac = re.findall(p, aux)[0]
                name = aux.replace(mac,"")
                device = {}
                device['name']=name.strip()
                device['mac']=mac.strip()
                devices.append(device)
            except:
                pass
        return devices

