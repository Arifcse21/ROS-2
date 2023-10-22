#!/usr/bin/python
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class DrawCircle(Node):
    def __init__(self):
        super(DrawCircle, self).__init__("draw_circle")
        self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer = self.create_timer(0.5, self.send_velocity_command)
        # Twist=message_dtype, /turtle1/cmd_vel=topic_name, 10=buffer/queue size
        self.get_logger().info("draw_circle node has been started! ")

    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0

        self.cmd_vel_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = DrawCircle()
    rclpy.spin(node)

    rclpy.shutdown()
