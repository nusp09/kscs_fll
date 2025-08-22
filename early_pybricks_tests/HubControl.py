from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, Matrix

hub = PrimeHub()
hub = PrimeHub(top_side=Axis.Y, front_side=-Axis.Z)
hub.display.orientation(up=Side.LEFT)


# Configure the stop button combination. Now, your program stops
# if you press the center and Bluetooth buttons simultaneously.
hub.system.set_stop_button((Button.CENTER, Button.BLUETOOTH))

# Now we can use the center button as a normal button.
while True:

    # Play a sound if the center button is pressed.
    if Button.CENTER in hub.buttons.pressed():
        hub.speaker.beep()

# Say goodbye and give some time to send it.
print("Goodbye!")
wait(100)

# Shut the hub down.
hub.system.shutdown()
