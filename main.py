# main.py
from time import sleep
import focar

try:
    focar.set_led(0, 255, 0)

    # Drive forward approximately one meter.
    focar.move_forward(50)
    sleep(2)  # Adjust this duration for your car's speed.
    focar.stop()
    sleep(0.5)

    # Perform a three-point turn.
    focar.turn_left(50)
    sleep(1)
    focar.stop()
    sleep(0.3)

    focar.turn_left(50)
    sleep(1)
    focar.stop()
    sleep(0.3)

    focar.turn_left(50)
    sleep(1)
    focar.stop()
    sleep(0.3)

    # Return toward the starting point.
    focar.move_backward(50)
    sleep(2)
    focar.stop()

finally:
    focar.stop()
    focar.set_led(0, 0, 0)