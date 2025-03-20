import RPi.GPIO as GPIO
import time

# Configuração do GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

try:
    while True:
        if GPIO.input(17):
            print("Luz detectada!")
        else:
            print("Sem luz detectada.")
        time.sleep(1)

except KeyboardInterrupt:
    print("Programa interrompido.")

finally:
    GPIO.cleanup()

