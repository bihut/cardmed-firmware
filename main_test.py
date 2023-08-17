from utilities.CardmedBluetooth import CardmedBluetooth

bt = CardmedBluetooth()
devices=bt.listDevices()
print(devices)