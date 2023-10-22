import rclpy
from rclpy.node import Node
from example_interfaces.msg import String


class SmartPhoneNode(Node):
    def __init__(self):
        super(SmartPhoneNode, self).__init__("smartphone")
        self.subscriber_ = self.create_subscription(
            String,                     # message type same as publisher
            "robot_news",               # topic name same as publisher
            self.callback_robot_news,   # callback function >> callback_topic_name <<
            10                          # queue size
        )
        self.get_logger().info("smartphone started listening ... ")

    def callback_robot_news(self, msg):
        self.get_logger().info(msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = SmartPhoneNode()
    rclpy.spin(node)
    rclpy.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
