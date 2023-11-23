from gpiozero import Servo
from gpiozero import AngularServo

#servo = Servo(13)
s = AngularServo(13)

def turn(direction):

	initial_value = 6
	angle = 60	

	if direction == "right":
		#servo.value = -1
		s.angle = initial_value - angle		

	if direction == "left":
		#servo.value = 1
		s.angle = initial_value + angle

	if direction == "initial":
		#servo.value = 0
		s.angle = initial_value
