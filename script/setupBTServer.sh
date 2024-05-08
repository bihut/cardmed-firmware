#ExecStart=/usr/lib/bluetooth/bluetoothd --noplugin=sap
#ŋet bluez https://learn.adafruit.com/install-bluez-on-the-raspberry-pi/installation
#la siguiente linea por si no detecta el dispositivo
#systemctl status hciuart.service
#el código bueno está en la carpeta /bluetooth/pi-ble-uart-server (hay que tocar el código para hacer pruebas de servicios)
#! /bin/bash
#hacer freeze en el terminal a ver las dependencias y apt list --installed
#sudo hciconfig hci0 leadv 0
#---------
#1) Descargar github.com/mengguang/pi-ble-uart-server
#2) Hacer el dispositivo discoverable --> sudo hciconfig hciX piscan
