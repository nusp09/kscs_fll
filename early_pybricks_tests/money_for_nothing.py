from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, Matrix, run_task, multitask
# all angles are relative
motor_limits = [1000, 2000, 200]
hub = PrimeHub()
hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
hub.display.orientation(up=Side.LEFT)
hub.speaker.volume(100)

driveL = Motor(Port.A, Direction.COUNTERCLOCKWISE)
driveR = Motor(Port.B)
AttachmentL = Motor(Port.C)
AttachmentR = Motor(Port.D)
SensorL = ColorSensor(Port.E)
SensorR = ColorSensor(Port.F)
drive = DriveBase(driveL, driveR, wheel_diameter=62.4, axle_track=111)
drive.use_gyro(True)

bpm = 134
NotesTop = []

NotesBottom = []


async def TopNotes(notes):
    await hub.speaker.play_notes(notes, bpm)


async def BottomNotes(notes):
    await hub.speaker.play_notes(notes, bpm)


async def main():
    await multitask(TopNotes(NotesTop))

run_task(main())
