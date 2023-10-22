from gpiozero import LED, PWMLED
from time import sleep

# Define the GPIO pins connected to the L298N motor driver for Motor A
IN1A = LED(17)
IN2A = LED(18)
ENA = PWMLED(19)

# Define the GPIO pins connected to the L298N motor driver for Motor B
IN3B = LED(22)
IN4B = LED(23)
ENB = PWMLED(21)

# Define the function to control the motor direction and speed
def set_motor_speed(motor, direction, speed):
    # Set the motor direction
    if direction == "forward":
        motor["IN1"].on()
        motor["IN2"].off()
    elif direction == "backward":
        motor["IN1"].off()
        motor["IN2"].on()
    else:
        motor["IN1"].off()
        motor["IN2"].off()

    # Set the motor speed
    motor["EN"].value = speed

# Test the motors by running them forward and backward
while True:
    s_r = float(input("Enter speed ratio: "))
    set_motor_speed({"IN1": IN1A, "IN2": IN2A, "EN": ENA}, "forward", s_r)  # Run Motor A forward at 50% speed
    set_motor_speed({"IN1": IN3B, "IN2": IN4B, "EN": ENB}, "forward", s_r)  # Run Motor B forward at 50% speed
    sleep(5)
    set_motor_speed({"IN1": IN1A, "IN2": IN2A, "EN": ENA}, "backward", s_r)  # Run Motor A backward at 50% speed
    set_motor_speed({"IN1": IN3B, "IN2": IN4B, "EN": ENB}, "backward", s_r)  # Run Motor B forward at 50% speed
    sleep(5)
    set_motor_speed({"IN1": IN1A, "IN2": IN2A, "EN": ENA}, "stop", 0)  # Stop Motor A
    set_motor_speed({"IN1": IN3B, "IN2": IN4B, "EN": ENB}, "stop", 0)  # Stop Motor B
    # sleep(2)

