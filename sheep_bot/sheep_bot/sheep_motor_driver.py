#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import numpy as np
import serial


class SimpleController(Node):

    def __init__(self):
        super().__init__("sheep_simple_controller")
        self.declare_parameter("wheel_radius", 0.033)
        self.declare_parameter("wheel_separation", 0.17)

        self.get_logger().info("hello from sheep motor driver")

        self.wheel_radius_ = self.get_parameter("wheel_radius").get_parameter_value().double_value
        self.wheel_separation_ = self.get_parameter("wheel_separation").get_parameter_value().double_value

        self.get_logger().info(f"Using wheel radius {self.wheel_radius_}")
        self.get_logger().info(f"Using wheel separation {self.wheel_separation_}")

        self.vel_sub_ = self.create_subscription(Twist, "cmd_vel", self.velCallback, 10)

        self.serial_ = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)
        if(not self.serial_.is_open):
            self.get_logger().error("failed to open serial port")

        self.speed_conversion_ = np.array([[self.wheel_radius_/2, self.wheel_radius_/2],
                                           [self.wheel_radius_/self.wheel_separation_, -self.wheel_radius_/self.wheel_separation_]])
        self.get_logger().info("The conversion matrix is %s" % self.speed_conversion_)


    def velCallback(self, msg):
       # Implements the differential kinematic model
       # Given v and w, calculate the velocities of the wheels
       robot_speed = np.array([[msg.linear.x],
                               [msg.angular.z]])
       wheel_speed = np.matmul(np.linalg.inv(self.speed_conversion_), robot_speed) 

       self.get_logger().info(f"Wheel speed[1,0]: {wheel_speed[1,0]}, Wheel speed[0,0]: {wheel_speed[0,0]}")
       
       self.serial_.write(f'm {int(wheel_speed[1, 0])} {int(wheel_speed[0, 0])}\r\n'.encode('utf-8'))

       #wheel_speed_msg = Float64MultiArray()
       #wheel_speed_msg.data = [wheel_speed[1, 0], wheel_speed[0, 0]]

       #self.wheel_cmd_pub_.publish(wheel_speed_msg)


def main():
    rclpy.init()

    simple_controller = SimpleController()
    rclpy.spin(simple_controller)
    
    simple_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

