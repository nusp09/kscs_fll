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

motor uses an input for whether 'input' (the first parameter) is calculated as rotations or as cm. at the begining of the program the relative motor position of both of the motors is set to 0 so that we can actually tell how far the robot has moved. then if rotations was chosen we add the relative positions together and divide them by 720.

the reason for this is that usually for 1 motor you would divide the mean by 360 but to remove a step instead of dividing by 2 and then by 360 we just divided it by 720.

whereas if we wanted to move a certian amount of cm first we had to find the circumference of our wheels then divide the 720 by that to get the amount of cm moved.
