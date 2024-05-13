import RPi.GPIO as GPIO  # RPi.GPIO can be referred as GPIO from now
import time
class CardmedGPIO:
    LED_BATTERY_1=-1
    LED_BATTERY_2=-1
    LED_BATTERY_3=-1
    LED_BATTERY_4=-1
    BUTTON_REBOOT=-1
    BUTTON_TURNON_OFF=-1
    LED_STATUS=-1

    def __init__(self) -> None:
        super().__init__()




#ledPin = 11  # pin11


#def setup():
#    GPIO.setmode(GPIO.BOARD)  # GPIO Numbering of Pins
#    GPIO.setup(ledPin, GPIO.OUT)  # Set ledPin as output
#    GPIO.output(ledPin, GPIO.LOW)  # Set ledPin to LOW to turn Off the LED


'''def loop():
    while True:
        print('LED on')
        GPIO.output(ledPin, GPIO.HIGH)  # LED On
        time.sleep(1.0)  # wait 1 sec
        print('LED off')
        GPIO.output(ledPin, GPIO.LOW)  # LED Off
        time.sleep(1.0)  # wait 1 sec


def endprogram():
    GPIO.output(ledPin, GPIO.LOW)  # LED Off
    GPIO.cleanup()  # Release resources


if __name__ == '__main__':  # Program starts from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the destroy() will be  executed.
        endprogram()'''