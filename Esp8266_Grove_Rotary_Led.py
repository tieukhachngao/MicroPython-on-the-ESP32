from machine import Pin, PWM, ADC
import time
def run():
    led = Pin(13, Pin.OUT)
    led_pwm = PWM(led)
    rotary = ADC(0)

    led_pwm.freq(500)
    while 1:
        led_pwm.duty(rotary.read())
        print(rotary.read())
        time.sleep(1)






