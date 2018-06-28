#!/usr/bin/python

import smbus2
import math
import time
import sys
import numpy

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

bus = smbus2.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command

if sys.argv[1] == "--help":
    print("Usage: python MPU6050_tilt_angle.py [Number of Samples] [Time Between Samples]")
    print("Ex: python MPU6050_tilt_angle.py 10 .1")
    print("This takes 10 samples .1 seconds apart, and averages them for the tilt angle")
    sys.exit()

samples = int(sys.argv[1])

# Now wake the 6050 up as it starts in sleep mode
bus.write_byte_data(address, power_mgmt_1, 0)

print("gyro data")
print("---------")

gyro_xout = read_word_2c(0x43)
gyro_yout = read_word_2c(0x45)
gyro_zout = read_word_2c(0x47)

print("gyro_xout: ", gyro_xout, " scaled: ", (gyro_xout / 131))
print("gyro_yout: ", gyro_yout, " scaled: ", (gyro_yout / 131))
print("gyro_zout: ", gyro_zout, " scaled: ", (gyro_zout / 131))

print()
print("accelerometer data")
print("------------------")

while True:
   try:
#      print("accel_xout: ", accel_xout, " scaled: ", accel_xout_scaled)
#      print("accel_yout: ", accel_yout, " scaled: ", accel_yout_scaled)
#      print("accel_zout: ", accel_zout, " scaled: ", accel_zout_scaled)
      x_accel_array = numpy.zeros(samples)
      y_accel_array = numpy.zeros(samples)


      for idx, item in enumerate(x_accel_array):
          accel_xout = read_word_2c(0x3b)
          accel_yout = read_word_2c(0x3d)
          accel_zout = read_word_2c(0x3f)

          accel_xout_scaled = accel_xout / 16384.0
          accel_yout_scaled = accel_yout / 16384.0
          accel_zout_scaled = accel_zout / 16384.0

          x_rot_angle = round(get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled), 2)
          y_rot_angle = round(get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled), 2)
          
#          print(x_rot_angle)
#          print(y_rot_angle)

          x_accel_array = numpy.append(x_accel_array, x_rot_angle)
          y_accel_array = numpy.append(y_accel_array, y_rot_angle)
#          print(x_accel_array[idx])
#          print ("x rotation: " , x_rot_angle)
#          print ("y rotation: " , y_rot_angle)
#          print ("Loop")
          time.sleep(float(sys.argv[2]))


      print("X Tilt Angle=", round((x_accel_array.sum()/samples), 2))
      print("Y Tilt Angle=", round((y_accel_array.sum()/samples), 2))
      
   except(KeyboardInterrupt, SystemExit):
      sys.exit()
