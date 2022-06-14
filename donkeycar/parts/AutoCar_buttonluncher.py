import RPi.GPIO as GPIO

class AC_buttonreader(object):
    def __init__(self):
        print(' ----- AutoCar : Starting button reader part.')

        self.btn_pin = 12
        self.state=False


    def run(self,mode):
                GPIO.setwarnings(False) # Ignore warning for now
                GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
                GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

                if GPIO.input(12) == GPIO.HIGH:
                    print("Button was pushed!")
                    print(GPIO.input(self.btn_pin))
                    if self.state is True:
                       self.state=False
                       print("stop mod auto")
                       mode ='user'
                    else:
                        self.state=True
                        print("Start")
                        mode= 'local'
                GPIO.cleanup()
                return mode
