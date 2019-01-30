
# coding: utf-8

# In[1]:


# Use tha Adafruit library for PCA9685 
import Adafruit_PCA9685
import time

# Note: Install with pip3 for Python 3 


# In[2]:


pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

# Note: Default address on i2c bus of
# 1. PCA9685 is 0x40
# 2. ADS1115 is 0x48
# Use 'sudo i2c detect -y 1' to check


# In[3]:


def runServo(pinNumber, shaftPosition):
    # Legacy code for standard servo motor
    pulseWidth_start = 150   # 0 degrees
    pulseWidth_finish = 650  # 180 degrees
    pulseWidth = 150 + (shaftPosition * (650 - 150) / 180) 
    pwm.set_pwm(pinNumber, 0, int(pulseWidth))
    print('Turning {} by {} degrees with {} setting.'.format(pinNumber, shaftPosition, int(pulseWidth)))

def spinServo(pinNumber, rotationSpeed):
    # Adaptation for continuous rotation servo motor
    pwm.set_pwm(pinNumber, 0, rotationSpeed)
    print('Spinning {} at {} setting.'.format(pinNumber, rotationSpeed))
    time.sleep(2)


# In[4]:


# Sweep through the servo's range of motion
# Facing the motor shaft for clockwise and anti-clockwise reference,
# imagine a control knob that turns all the way from left (0 deg) to right (180 deg) 
# through a center (90 deg). Corresponding markings are 340 (min) to 405 (max)
# through a midpoint of 370 (mid.) The mid point represents lo 
# and turning the knob left of center operates the motor clockwise at higher speed
# whereas turning the knob right of center operates the motor anti-clockwise at higher speed.


def sweepServo(pinNumber):
    [spinServo(pinNumber, x) for x in range(340, 405, 5)]
    pwm.set_pwm(pinNumber, 0, 0)

"""
sweepServo(0)
sweepServo(4)
"""

# In[5]:


# Move buggy forward
# The motor on the left side must turn anti-clockwise 
# The motor on the right side must turn clockwise 

def moveForward_maximumSpeed(leftNumber, rightNumber):
    pwm.set_pwm(leftNumber, 0, 400)
    pwm.set_pwm(rightNumber, 0, 340)
    
def moveReverse_maximumSpeed(leftNumber, rightNumber):
    pwm.set_pwm(leftNumber, 0, 340)
    pwm.set_pwm(rightNumber, 0, 400)
    
def halt(leftNumber, rightNumber):
    pwm.set_pwm(leftNumber, 0, 0)
    pwm.set_pwm(rightNumber, 0, 0)
   
"""
leftNumber = 0
rightNumber = 4
moveForward_maximumSpeed(leftNumber, rightNumber)
time.sleep(10)
halt(leftNumber, rightNumber)
time.sleep(2)
moveReverse_maximumSpeed(leftNumber, rightNumber)
time.sleep(10)
halt(leftNumber, rightNumber)
"""

# In[12]:


# Move buggy left or right
# in forward mode

def moveForward_turnRight(leftNumber, rightNumber):
    pwm.set_pwm(leftNumber, 0, 400)
    pwm.set_pwm(rightNumber, 0, 360)
    
def moveForward_turnLeft(leftNumber, rightNumber):
    pwm.set_pwm(leftNumber, 0, 385)
    pwm.set_pwm(rightNumber, 0, 340)

"""
leftNumber = 0
rightNumber = 4
print("Moving forward, full speed")
moveForward_maximumSpeed(leftNumber, rightNumber)
time.sleep(5)
print("Making a right turn")
moveForward_turnRight(leftNumber, rightNumber)
time.sleep(10)
print("Moving forward, full speed")
moveForward_maximumSpeed(leftNumber, rightNumber)
time.sleep(5)
print("Making a left turn")
moveForward_turnLeft(leftNumber, rightNumber)
time.sleep(10)
halt(leftNumber, rightNumber)


# In[13]:


halt(leftNumber, rightNumber)
"""
