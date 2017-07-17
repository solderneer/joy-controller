#!/usr/bin/env python

# importing libraries and ros stuff
import rospy
import spidev
from sensor_msgs.msg import Joy

def callback(data):

    # Detect Button A
    if (data.buttons[1]):
        to_send = [129, 1]
        spi.xfer(to_send)

    # Detect Button B
    if (data.buttons[4]):
        to_send = [144, 1]
        spi.xfer(to_send)

    # Left joystick and mapping values from -1 -> 1 to 0 -> 100
    if (data.axes[1] > 0):
        temp = int((1 - data.axes[1])/0.02)
        to_send = [136, temp]
        spi.xfer(to_send)

    elif (data.axes[1] < 0):
        temp = int(((-data.axes[1])/0.02) + 50)
        to_send = [136, temp]
        spi.xfer(to_send)

    # Right joystick and mapping values from 0 -> 1 to -> 100
    to_send = [134, (data.axes[6] * 100)]
    spi.xfer(to_send)


def start():
    # Global handle for SPIdev so that callback can send data
    global spi
    spi = spidev.SpiDev()
    spi.open(bus, device) # Connects to the specified SPI device, opening /dev/spidev<bus>.<device>

    # inset more settings for spi as required here ( https://github.com/doceme/py-spidev )
    # Example code
    # spi.max_speed_hz = 5000
    # spi.mode = 0b01

    rospy.Subscriber("joy", Joy, callback) # Subscribe to the rostopic joy with the structure of sensor_msg Joy
    rospy.init_node('joy_controller') # Set name of node to be joy_controller
    rospy.spin() # Prevent end of execution until node is stopped

if __name__ == '__main__':
    start()