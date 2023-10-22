import rclpy
from rclpy.node import Node
from text_to_speech import save


class SpeakerNode(Node):
    def __init__(self):
        super(SpeakerNode, self).__init__("speaker")
        self.create_timer(2, self.speaker_callback)

    def speaker_callback(self):
        self.get_logger().info("Speaker Node Initialized. Ami ekhon kotha bolbo ...")
        save("Speaker Node Initialized. I will speak now", "en", slow=True, file="pls_delete_me.mp3")
        self.get_logger().info("Hello Abdullah Al Arif ...")
        save("Hello Abdullah Al Arif", "bn", slow=True, file="pls_delete_me.mp3")


def main(args=None):
    rclpy.init(args=args)
    node = SpeakerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()

