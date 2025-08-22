from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, Matrix

hub = PrimeHub()
# Rotate the display. Now right is up.
hub.display.orientation(up=Side.LEFT)
#numbers
hub.display.number(1)

#letters/characters
hub.display.char("A")
hub.display.text("cheese")


#individual pixels
#row col brightness
hub.display.pixel(1,1,50)
wait(3000)


#full on diplays
# Make a square that is bright on the outside and faint in the middle.
SQUARE = Matrix(
    [
        [100, 100, 100, 100, 100],
        [100, 50, 50, 50, 100],
        [100, 50, 0, 50, 100],
        [100, 50, 50, 50, 100],
        [100, 100, 100, 100, 100],
    ]
)

# Display the square.
hub.display.icon(SQUARE)
wait(3000)

# Make an image using a Python list comprehension. In this image, the
# brightness of each pixel is the sum of the row and column index. So the
# light is faint in the top left and bright in the bottom right.
GRADIENT = Matrix([[(r + c) for c in range(5)] for r in range(5)]) * 12.5

# Display the generated gradient.
hub.display.icon(GRADIENT)
wait(3000)
