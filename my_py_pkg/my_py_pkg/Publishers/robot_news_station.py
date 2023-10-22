#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class RobotNewsStationNode(Node):
    def __init__(self):
        super(RobotNewsStationNode, self).__init__("robot_news_station")
        self.counter = 0
        self.publisher_ = self.create_publisher(
            String,         # Message type
            "robot_news",   # Topic name it publishes
            10              # queue size
        )
        self.timer_ = self.create_timer(0.5, self.publish_news, )
        self.get_logger().info(f"Robot news station has been started")

    def publish_news(self):
        msg = String()
        self.get_logger().info(f"Hello from robot news station  [{self.counter}]")
        msg.data = f"Hello from robot news station  [{self.counter}]"
        self.counter += 1
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
