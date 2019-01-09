import evdev
import Swerve_Servos
from evdev import InputDevice, categorize, ecodes

wiimote = InputDevice('/dev/input/event5')
print(wiimote)

keyStroke_1 = 257
keyStroke_2 = 258
keyStroke_upArrow = 103
keyStroke_dnArrow = 108
keyStroke_ltArrow = 105
keyStroke_rtArrow = 106

class servoDetails():
  def __init__(self):
    self.servo_num = 0
    self.shaft_position = 0
    self.step_size = 15
    Swerve_Servos.swerve(self.servo_num,0)

  def set_servo_num(self, num):
    self.servo_num = num
    Swerve_Servos.swerve(self.servo_num,0)

  def set_step_size(self,num):
    self.step_size = num

  def get_servo_num(self):
    return self.servo_num

  def get_shaft_position(self):
    return self.shaft_position

  def get_step_size(self):
    return self.step_size
  
  def update_step_size(self, direction):
    """
    Updating the step size from the keypress of wiimote
    Left key is mapped to decrement step size by 5 degrees
    Right key is mapped to increment step size by 5 degrees
    Net step size is constrained between 5 to 30 degrees
    """
    if(direction):#for decrement
        if(self.step_size <= 5):
            pass
        else:
            self.step_size -= 5
    else:#for increment
        if(self.step_size >= 30):
            pass
        else:
            self.step_size += 5
            
    print("Updated step size: ",self.step_size)
        
  def swerve_servos(self, direction):
    """
    Updating the shaft position of the selected servo motor by shaft rotation
    Up key is mapped to anti-clock wise rotation in increments of step size
    Dow key is mapped to clock wise direction in decrements of step size
    Rotation is constrained between 0 and 180, 0 for clockwise and 180 for anti-clock wise
    """
    if(direction):#for clock direction
        if(self.shaft_position <= 0):
            pass
        else:
            self.shaft_position -= self.step_size
            Swerve_Servos.swerve(self.servo_num,self.shaft_position)
    else:#for anti-clockwise direction
        if(self.shaft_position >= 180):
            pass
        else:
            self.shaft_position += self.step_size
            Swerve_Servos.swerve(self.servo_num,self.shaft_position)
            
def wiimoteApp():
  s = servoDetails()
  for wiievent in wiimote.read_loop():
    # Exit gracefully when '+' key is pressed
    if wiievent.code == 407 and wiievent.value == 1:
        break
    # Filter for events of type "key pressed"
    if wiievent.type == ecodes.EV_KEY:
        print(wiievent)
        if wiievent.value == 1:
            if wiievent.code == keyStroke_1:
                print("Switched to mode 1.")
                s.set_servo_num(0)
            elif wiievent.code == keyStroke_2:
                print("Switched to mode 2.")
                s.set_servo_num(4)
            elif wiievent.code == keyStroke_upArrow:
                print("Going anti-clock wise")
                s.swerve_servos(False)#True indicates left rotation
            elif wiievent.code == keyStroke_dnArrow:
                print("Going clock wise")
                s.swerve_servos(True)#False right rotation
            elif wiievent.code == keyStroke_ltArrow:
                print("Decrement Step Size")
                s.update_step_size(True)
            elif wiievent.code == keyStroke_rtArrow:
                print("Incrementing Step Size")
                s.update_step_size(False)
            else:
                print("No action.")

if __name__ == "__main__":
    wiimoteApp()