#ExecStart=/usr/lib/bluetooth/bluetoothd --noplugin=sap
#ŋet bluez https://learn.adafruit.com/install-bluez-on-the-raspberry-pi/installation
#la siguiente linea por si no detecta el dispositivo
#systemctl status hciuart.service
#el código bueno está en la carpeta /bluetooth/pi-ble-uart-server (hay que tocar el código para hacer pruebas de servicios)
#! /bin/bash

#sudo hciconfig hci0 leadv 0
#---------
#0 - opcional-) instalar librerías (sudo apt-get install libbluetooth-dev libboost-python-dev libboost-thread-dev libglib2.0-dev python-dev
#sudo pip install gattlib)
#1) sudo nano /etc/systemd/system/dbus-org.bluez.service --> ExecStart=/usr/lib/bluetooth/bluetoothd -E
#2) Descargar github.com/mengguang/pi-ble-uart-server
#3) Hacer el dispositivo discoverable --> sudo hciconfig hciX piscan


#sudo apt install sqlite3