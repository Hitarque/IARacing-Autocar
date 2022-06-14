import RPi.GPIO as GPIO

class AC_buttonreader(object):
    def __init__(self):
        print(' ----- AutoCar : Starting button reader part.')

        self.btn_pin = 16
        self.state=False


    def run(self):
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(self.btn_pin, GPIO.IN)
                if GPIO.input(self.btn_pin):
                    print(GPIO.input(self.btn_pin))
                    if self.state is True:
                       self.state=False
                       print("stop mod auto")
                    else:
                        self.state=True
                        print("Start")
                    #mode= 'local'
                print('on')
                mode ='user'
                GPIO.cleanup()
                return mode
