## this is the place where you will understand all of the code
### ded strait
#### what all of the parameters do:
 - 1st   is the input so how many of the thing you want to do
 - teh second one is th distance selector 1 for rottions 2 for cm
 - 3rd is acceleration or how much the speed is being increased by each cycle
 - 4th is top speed ussually i like it to be at 100%
 - 5th is forwards or backwards 0 for forwards and 1 for backwards
#### the actual code:
![alt text](https://github.com/nusp09/kscs_fll/blob/main/2024-2025-submergerd/pictures/ded_strait_v2_full.png)

now lets break all of that down
first the initialisations:

![alt text](https://github.com/nusp09/kscs_fll/blob/main/2024-2025-submergerd/pictures/ded_strait_initialisation.png)

first for movement we set the movement motors relative position to 0 so we can move for a certian amount of 
rotations or cm.

then we need to know if we are moveing forwards or backwards one easy trick we found was to reverse the movement motors
so we take the input from the code and dependent on that we switch the movement motors

now for the variables:

motor - we use for calculating when to stop

now for the pid stuff

integral - set to 0 because it is used for the compound errors

kp,ki,kd - the gain variables for the pid controller

previous error - set to 0 so that if we have used it previously there are no unexpected errors

acc,decc - used for acceleration / decceleration control

calculations:


![alt text](https://github.com/nusp09/kscs_fll/blob/main/2024-2025-submergerd/pictures/motor.png)


motor uses an input for whether 'input' (the first parameter) is calculated as rotations or as cm. at the begining of the program the relative motor position of both of the motors is set to 0 so that we can actually tell how far the robot has moved. then if rotations was chosen we add the relative positions together and divide them by 720.

the reason for this is that usually for 1 motor you would divide the mean by 360 but to remove a step instead of dividing by 2 and then by 360 we just divided it by 720.

whereas if we wanted to move a certian amount of cm first we had to find the circumference of our wheels then divide the 720 by that to get the amount of cm moved.

now for the real meet of the controller, the maths, this is my favorite part of it


![alt text](https://github.com/nusp09/kscs_fll/blob/main/2024-2025-submergerd/pictures/calcs.png)


so first of all since we want to keep going straight from when we first start we and we set the yaw angle to 0 we can set our error to 0-yaw (one cool fact about gyro sensors as a whole is that they dont measure how far youve moved they measure angular velocity and time to figure out how far youve turned, dispite this you cant use the gyro's angular velocity in the spike prime blocks to accurately calculate the distance turned). next is the rerror which is purely for how far we have gone. at one point the team did try to integrate the robots acceleration to see if it would be more accurate however it wasnt so thats kinda annoying.

now for the actual pid part. first we calculate the proportional correction which is the most basic part of the pid it just turns it based off of how far off it is, so the bigger the error the bigger the correction and vice versa. next the integral, this is the sum of errors over time this helps to improve the robots accuracy over time giving it a basis for how likely it is to be wrong. and finally the derivative is what is basically trying to predict what is going to happen next we use this to help prevent overshoot of the robot and make it a smoother/ less jittery program. after all that they are all multiplied by constants that have been tuned for our robot and are finally added to give us the correction variable. hopefully if it is going completely straight the correction should be 0.


![alt text](https://github.com/nusp09/kscs_fll/blob/nusp09_docs_edits/2024-2025-submergerd/pictures/acceleration.png)


this is the acceleration portion of the code. acceleration is one of the things we have changed since regionals(the other being the ability to go backwards by flipping the movement motors around). the acceleration is increased by a set value every cycle of the program(so every 0.05 second, this time was chosen to pay homage to minecrafts tick speed) unlike the deceleration which is proportional to how far you have left. there isnt much else to say about this other than using acceleration helps more accurate measurements.

finally (i dont think we need a picture or this, if you really want to look see the top of the document for the full script) is that we start to move in the direction of 'correction' we apply a loop delay of 0.05 seconds and at the end of the script outside of the loop we set the movement motors back to normal.

