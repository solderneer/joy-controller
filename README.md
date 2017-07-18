# joy_controller

joy_controller is a ROS package that parses joystick information and sends respective SPI commands which allows for control over certain parameters. This particular implementation is written in python using rospy and spidev. The instructions to set it up are below.

# Instructions to install
Installation is pretty simple and similiar to other ROS packages. However, the spidev library for python has to be installed explicitly for the script to work.
```
pip install spidev

cd ~/catkin_ws/src
git clone https://github.com/solderneer/joy_controller.git
cd ~/catkin_ws
catkin_make
```
# Instructions to run
To run the script just start the respective rosnode. Bear in mind that the spi device and bus settings have to be set it the `/script/joy_controller.py` before the node can be run. Else an error will be thrown.

 ```
 rosrun joy_controller joy_controller.py
 ```
