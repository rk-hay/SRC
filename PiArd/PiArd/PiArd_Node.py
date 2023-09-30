import rclpy
from rclpy.node import Node

class MyNode(Node):
	def __init__(self):
		super().__init__("PiArd")
		
	def timer_callback(self):
		self.get_logger().info(Hello ROS2)
	


def main(args=None):
    rclpy.init(args=args)
    node = MyNode('PiArd_Node')
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
