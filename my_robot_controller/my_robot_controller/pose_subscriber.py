# !/usr/bin/python3
#!source ~/.bashrc
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriberNode(Node):
    def __init__(self):
        super(PoseSubscriberNode, self).__init__("pose_subscriber")
        self.pose_subscriber = self.create_subscription(
            Pose,
            "/turtle1/pose",
            self.pose_callback,
            10
        )

    def pose_callback(self, msg: Pose):
        # self.get_logger().info(str(msg))
        self.get_logger().info("(" + str(msg.x) + "," + str(msg.y) + str(msg.theta) + ")" )

def main(args=None):
    rclpy.init(args=args)
    node = PoseSubscriberNode()
    rclpy.spin(node)

    rclpy.shutdown()