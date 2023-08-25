import RPi.GPIO as GPIO
import time
#LedPin = 17    # pin11 --- led
BtnPin = 27    # pin13 --- button
#tutorial
# https://acoptex.com/project/4006/project-19c-raspberry-pi-zero-w-board-led-and-push-button-at-acoptexcom/
def setup():
    GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by BCM
#GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	#GPIO.output(LedPin, GPIO.LOW) # Set LedPin low to off led

boton_pulsado=False
tiempo_antes = None
tiempo_despues=None
def loop():
    boton_pulsado=False
    tiempo_antes = None
    tiempo_despues=None
    while True:
        if GPIO.input(BtnPin) == GPIO.LOW:
            if not boton_pulsado:
                print("Botón pulsado")
                boton_pulsado = True
                tiempo_antes = time.time()
                #GPIO.output(LedPin, GPIO.HIGH)  # led on
        else:
            if boton_pulsado:
                tiempo_despues = time.time()
                segundos = (tiempo_despues - tiempo_antes)
                print("El boton ha estado pulsado",str(segundos)," segundos")
                boton_pulsado = False
                        #pass
			#print("botón no pulsado")
			#GPIO.output(LedPin, GPIO.LOW) # led off

def destroy():
	#GPIO.output(LedPin, GPIO.LOW)     # led off
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
