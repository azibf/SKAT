import dronekit_sitl
from dronekit import connect, Command, LocationGlobal, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time, sys, argparse, math


class DroneLit_Base:
    vehicle = None
    sitl = None

    def __init__(self, debug=False):
        # settings
        self.is_debug = debug
        if self.is_debug:
            self.sitl = dronekit_sitl.start_default()
            connection_string = self.sitl.connection_string()

            # Connect to the Vehicle.
            print("Connecting to vehicle on: %s" % (connection_string,))
            self.vehicle = connect(connection_string, wait_ready=True)
        else:

            connectionString = '127.0.0.1:14540'  # 14540 or 14550
            self.MAV_MODE_AUTO = 4
            # Parse connection argument
            parser = argparse.ArgumentParser()
            parser.add_argument("-c", "--connect", help="connection string")
            args = parser.parse_args()
            if args.connect:
                connectionString = args.connect
            print("Connecting")
            print(connectionString)
            self.vehicle = connect(connectionString, wait_ready=True, baud=57600)\
        # Атрибуты коптера
        print("Vehicle state:")
        # Объект с координатами широты, долготы, высоты и относительной высоты.
        # Высота считается относительно уровня моря, а относительная высота применяется к стартовой позиции.
        print(" Global Location: %s" % self.vehicle.location.global_frame)
        print(" Global Location (relative altitude): %s" % self.vehicle.location.global_relative_frame)
        print(" Local Location: %s" % self.vehicle.location.local_frame)
        print(" Attitude: %s" % self.vehicle.attitude) # Позиция в кординатах pitch, yaw, roll
        print(" Battery: %s" % self.vehicle.battery) # Текущий вольтаж, ток и оставшийся уровень заряда
        print(" Last Heartbeat: %s" % self.vehicle.last_heartbeat) # Время последней удавшаяся проверки связи с коптером.
        print(" Heading: %s" % self.vehicle.heading) # Направление, в градусах относительно севера
        print(" Groundspeed: %s" % self.vehicle.groundspeed) # Скорость по земле
        print(" Airspeed: %s" % self.vehicle.airspeed) # Скорость в воздух
        print(" Is Armable?: %s" % self.vehicle.is_armable) # можем запускать двигатели или нет
        print(" Armed: %s" % self.vehicle.armed) # Запущены ли двигатели
        print(" Mode: %s" % self.vehicle.mode.name) # Режим в котором сейчас находимся

        print(self.vehicle.channels)

        return None

    def __del__(self):
        if self.vehicle:
            self.vehicle.close()
            if self.is_debug:
                self.sitl.stop()

    def PX4setMode(self, mavMode):
        self.vehicle._master.mav.command_long_send(self.vehicle._master.target_system,
                                                   self.vehicle._master.target_component,
                                                   mavutil.mavlink.MAV_CMD_DO_SET_MODE, 0,
                                                   mavMode,
                                                   0, 0, 0, 0, 0, 0)

    def enableArm(self):
        timer = 0
        self.vehicle.armed = True
        while not self.vehicle.armed and timer < 20:
            print(" Ждем моторы...")
            time.sleep(1)
        if timer >= 20:
             return False
        return True

    def disableArm(self):
        self.vehicle.armed = False
        time.sleep(1)
        return True

    def simple_start(self, height):
        print("Предполетные проверки")
        if self.enableArm():
            print("Запускаем двигатели")
            self.vehicle.mode = VehicleMode("GUIDED")
            if self.vehicle.armed:
                time.sleep(3)  # подождать!
                print("Взлет!")
                self.vehicle.simple_takeoff(height)  # взлететь!
                while self.vehicle.location.global_relative_frame.alt < height:
                    print(" Текущая высота: ", self.vehicle.location.global_relative_frame.alt)
                    # Что бы не скучно было, смотрим как высоко уже поднялись
                    time.sleep(1)
                self.simple_stop()
        print('Что-то поломалось! =(')
        return False

    def checkArrived(self, location, precision=0.3):
        veh_loc = self.vehicle.location.global_relative_frame
        d_lat = (location[0] - veh_loc.lat) * 1.113195e5
        d_lon = (location[1] - veh_loc.lon) * 1.113195e5
        d_alt = location[3] - veh_loc.alt
        if math.sqrt(d_lat ** 2 + d_lon ** 2 + d_alt ** 2) < precision:
            print("На месте")
            return True
        return False

    def goToLocation(self, location):
        relative_location = LocationGlobalRelative(location[0], location[1],location[2])
        self.vehicle.simple_goto(relative_location)
        while not self.checkArrived(location):
            time.sleep(3)
        return True

    def startMission(self):
        pass

    def simple_stop(self):
        self.vehicle.mode = "LAND"
        if self.disableArm():
            print('done!!!')
            return True
        print('Что-то поломалось! =(')
        return False

    def goHome(self):
        self.vehicle.mode = VehicleMode("RTL")
        return True


import os,sys

sys.stderr = open(os.devnull, "w")
try:
  import psutil
#except:
  #handle module not found
finally:
  sys.stderr = sys.__stderr__


drone = DroneLit_Base(True)
drone.simple_start(0.1)
drone.simple_stop()
drone.__del__()