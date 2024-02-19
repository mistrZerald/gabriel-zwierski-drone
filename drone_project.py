import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist, Pose

""" 
Wybrany znak: 'M'
Pętla: brak
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
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # Feel fre to fill with your code! Add some objects to represent a goal points to achieve
	
	self.Mx1 = 2.0
	self.My1 = 0.0
	self.Mx2 = 0.0
	self.My2 = -1.5
	
	self.Mx3 = 2.0
	self.My3 = -3.0
	
	self.Mx4 = 0.0
	self.My4 = -3.0
    
    def pose_callback(self):
        self.gt_pose = data

    
    def timer_callback(self):
        # HINT: Check a current pose. Use it to check if a drone achieved a desired pose.
        print(f"Current pose: {self.gt_pose}")
        x = self.gt.pose.position.x
        y = self.gt_pose.position.y
        # HINT: Use a self.command_pub to publish a command
        # Fill with your code!
        print("Published!")
        

                
        if abs(x - self.Mx1) > 5 and if abs(y - self.My1) > 5:
        	speed = Twist()
        	speed.linear.x = self.goalx1
        	speed.linear.y = self.goaly1
                self.command_pub.publish(speed)
        if abs(self.Mx1 - self.Mx2) > 0.1 and if abs(self.My1 - self.My2) > 0.1:
        	speed = Twist()
        	speed.linear.x = self.goalx2
        	speed.linear.y = self.goaly2
                self.command_pub.publish(speed)
        if abs(self.Mx2 - self.Mx3) > 0.1 and if abs(self.My2 - self.My3) > 0.1:
        	speed = Twist()
        	speed.linear.x = self.goalx3
        	speed.linear.y = self.goaly3
                self.command_pub.publish(speed)
        if abs(self.Mx3 - self.Mx4) > 0.1 and if abs(self.My3 - self.My4) > 0.1:
        	speed = Twist()
        	speed.linear.x = self.goalx4
        	speed.linear.y = self.goaly4
	        self.command_pub.publish(speed)
	
	




def main(args=None):
    rclpy.init(args=args)

    node = DroneController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
