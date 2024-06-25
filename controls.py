'''
This is a python script to run the 3d filament spool winder. It controls a Nema17 stepper motor with
a DVR8825 driver and a limit switch to detect the filament.
'''

import utime  # type: ignore
from machine import Pin  # type: ignore

from DVR8825_Driver import Stepper  # type: ignore


if __name__ == "__main__":

    print("Starting...")
    limit_swt = Pin(12, Pin.IN)
    btn = Pin(14, Pin.IN)
    pico_led = Pin('LED', Pin.OUT)

    led_flash_time = 500  # milliseconds

    try:

        stepper = Stepper(step_pin=1, dir_pin=0, enable_pin=2,
                          mode_pins=(3, 4, 5))
        stepper.set_step_mode(2)
        stepper.set_speed(400)
        stepper.set_direction(stepper.CCW)

        stepper.enable()

        print("Press Button to start")
        while not btn.value():
            if btn.value():
                utime.sleep(1)
                break

        last_flash = 0
        print('Starting...')
        while not limit_swt.value() or not btn.value():
            if utime.ticks_ms() - last_flash >= led_flash_time:
                last_flash = utime.ticks_ms()
                pico_led.toggle()

            stepper.one_step()

        print("Finished!")
        pico_led.off()
        stepper.disable()

    except KeyboardInterrupt:
        stepper.disable()
        pico_led.off()
        print("Force Stop")
