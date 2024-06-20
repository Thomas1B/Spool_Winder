'''
This is a python script to run the 3d filament spool winder. It controls a Nema17 stepper motor with
a DVR8825 driver and a limit switch to detect the filament.
'''

import utime
from machine import Pin  # type: ignore

from DVR8825_Driver import Stepper

dir_pin = 4
step_pin = 5
enable_pin = 6


if __name__ == "__main__":
    try:
        stepper = Stepper(step_pin=7, dir_pin=6, enable_pin=8,
                          step_mode=2,
                          mode_pins=(0, None, None))

        stepper.set_speed(300)
        stepper.enable()

        stepper.move_to_abs(200)

        stepper.disable()

    except KeyboardInterrupt:
        stepper.disable()
