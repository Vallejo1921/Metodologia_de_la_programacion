from machine import Pin, PWM
from time import sleep

led = PWM(Pin(15))   # Cambia 15 por el pin que estés usando
led.freq(1000)       # Frecuencia estable de PWM

while True:
    print("Aumentar intensidad (inhalar)")
    for brillo in range(0, 65535, 500):
        led.duty_u16(brillo)
        sleep(0.01)

    print("Disminuir intensidad (exhalar)")
    for brillo in range(65535, 0, -500):
        led.duty_u16(brillo)
        sleep(0.01)