from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, Matrix
# all angles are relative
motor_limits = [1000,2000,200]
hub = PrimeHub()
hub = PrimeHub(top_side=Axis.Z, front_side=Axis.X)
hub.display.orientation(up=Side.LEFT)

AttachmentLeft = Motor(Port.C)
AttachmentLeft.control.limits(1000,2000,200)
Attachmentright = Motor(Port.D)
AttachmentLeft.hold()
Attachmentright.hold()
#run motors at a set speed forever until told otherwise
Attachmentright.run(500)
wait(3000)
Attachmentright.run(-500)
wait(3000)
AttachmentLeft.run(500)
wait(3000)
AttachmentLeft.run(-500)
wait(3000)
Attachmentright.hold()
AttachmentLeft.hold()

#run motors at a duty cycle/power -100/100
#Attachmentright.dc(100)
#AttachmentLeft.dc(-100)
#wait(3000)
#Attachmentright.hold
#AttachmentLeft.hold

wait(3000)

#running by a fixed amount
#              run_time(speed,time,stop,wait)
AttachmentLeft.run_time(500,3000,Stop.HOLD,True)

wait(3000)

Attachmentright.hold()
AttachmentLeft.hold()


wait(3000)

#              run.angle(speed,relative_angle,stop,wait)
AttachmentLeft.run_angle(500,4*360,Stop.HOLD,True)
Attachmentright.run_angle(500,4*-360,Stop.HOLD,True)

wait(3000)


#              run_target(speed,target angle,stop,wait)
AttachmentLeft.run_target(100,360,Stop.HOLD,True)

Attachmentright.track_target(360)
while Attachmentright.done() == False:
    print("false")
    wait(10)
    print(Attachmentright.angle())
