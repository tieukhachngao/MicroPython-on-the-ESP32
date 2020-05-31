from machine import Pin
def run():
    pin = Pin(13, Pin.OUT)
    button = Pin(4, Pin.IN)
    while 1:
        state = button.value()
        if state > 0:
            pin.off()
        else:
            pin.on()