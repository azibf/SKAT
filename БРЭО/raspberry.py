import RPi.GPIO as GPIO
import os
import time

P7 = 7 # Открыть закрыть задвижку
P9 = 9 # ground

class Robot:
    def __init__(self, db, mediator, pins):
        self.db = db
        self.mediator = mediator
        self.TYPES = mediator.getTypes()
        self.PINS = pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PINS['DROP'], GPIO.OUT)
        GPIO.output(self.PINS['DROP'], False)

        print('start work! GPIO.VERSION=' + GPIO.VERSION)

        # подписки на события
        self.mediator.subscribe(self.TYPES['SHUTDOWN'], self.shutdown)
        self.mediator.subscribe(self.TYPES['REBOOT'], self.reboot)
        self.mediator.subscribe(self.TYPES['FIRE_DROP'], self.dropPresent)

    def __del__(self):
        GPIO.cleanup()
        print('GPIO cleanup')

    # выключиться
    def shutdown(self, options=None):
        print('shutdown')
        os.system("poweroff")
        return True

    def reboot(self, options=None):
        print('reboot')
        os.system('reboot')
        return True

    def drop(self, options=None):
        print('dropPresent')
        GPIO.output(self.PINS['DROP'], True)
        return True


