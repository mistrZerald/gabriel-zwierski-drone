import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist, Pose

""" 
Wybrany znak:
Pętla:
Płaszczyzna:
"""


class DroneController(Node):
    def __init__(self):
        super().__init__('drone_controller')
        
        # Current pose subscriber
        self.gt_pose_sub = self.create_subscription(
            Pose,
            '/drone/gt_pose',
            self.pose_callback,
            1)

        self.gt_pose = None

        # Control command publisher
        self.command_pub = self.create_publisher(Twist, '/drone/cmd_vel', 10)
        
        # Callback for executing a control commands
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # Feel fre to fill with your code! Add some objects to represent a goal points to achieve

    
    def pose_callback(self, data):
        self.gt_pose = data
        print(f"{data}")

    
    def timer_callback(self):
        # HINT: Check a current pose. Use it to check if a drone achieved a desired pose.
        print(f"Current pose: {self.gt_pose}")
        
        # HINT: Use a self.command_pub to publish a command
        # Fill with your code!
        print("Published!")



def main(args=None):
    rclpy.init(args=args)

    node = DroneController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
