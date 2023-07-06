from dronekit import connect, VehicleMode, LocationGlobalRelative
import time, argparse


connection_string = '127.0.0.1:14540'  # 14540 or 14550
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--connect", help="connection string")
args = parser.parse_args()
if args.connect:
    connection_string = args.connect

vehicle = connect(connection_string, wait_ready=True)


def arm_and_takeoff(tgt_attitude):
    print('arming')

    while not vehicle.is_armable:
        time.sleep(1)

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    vehicle.simple_takeoff(tgt_attitude)
    while True:
        attitude = vehicle.location.global_relative_frame.alt
        if attitude >= tgt_attitude - 1:
            print('reached')
            break

arm_and_takeoff(10)
vehicle.airspeed = 7

wpl = LocationGlobalRelative(35.9835973, -95.8742309, 10)
vehicle.simple_goto(wpl)


time.sleep(5)
vehicle.mode = VehicleMode("RTL")
time.sleep(5)
vehicle.close()
