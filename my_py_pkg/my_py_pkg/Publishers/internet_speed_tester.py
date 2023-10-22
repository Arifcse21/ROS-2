import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
import speedtest


class InternetSpeedTesterNode(Node):
    def __init__(self):
        super(InternetSpeedTesterNode, self).__init__("internet_speed")
        self.counter = 0
        self.publisher_ = self.create_publisher(
            String,
            "speed_tester",
            10
        )
        self.timer_ = self.create_timer(1, self.calculate_speed)
        self.get_logger().info("speed tester started ...")

    def calculate_speed(self):
        st = speedtest.Speedtest()
        st.get_best_server()
        msg = String()
        upload = st.upload() / 1_000_000
        download = st.download() / 1_000_000

        msg.data = f"upload = {upload}, download = {download} [{self.counter}]"
        self.counter += 1
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = InternetSpeedTesterNode()
    rclpy.spin(node)
    rclpy.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
