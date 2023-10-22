#!/usr/bin/python3
import rclpy
from rclpy.node import Node


class MyNode(Node):
    def __init__(self):
        super(MyNode, self).__init__("py_test")
        self.counter = 0
        self.get_logger().info("Starting ROS2 Node!...")
        self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        self.counter += 1
        self.get_logger().info("Hello BroBot! " + str(self.counter))


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
