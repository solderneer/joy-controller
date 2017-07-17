import rospy
import spidev
from sensor_msgs import Joy

def callback(data):


def start():
    global spi = spidev.SpiDev()
    spi.open(bus, device) # Connects to the specified SPI device, opening /dev/spidev<bus>.<device>

    # inset more settings for spi as required here ( https://github.com/doceme/py-spidev )
    # Example code
    # spi.max_speed_hz = 5000
    # spi.mode = 0b01
    
    rospy.Subscriber("joy", Joy, callback)
    rospy.init node('joy_controller')
    rospy.spin()

if name == '__main__':
    start()