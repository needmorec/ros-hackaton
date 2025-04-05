import rospy
import math
from clover import srv
from std_srvs.srv import Trigger

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
land = rospy.ServiceProxy('land', Trigger)

def navigate_wait(x=0, y=0, z=1, yaw=float('nan'), speed=0.2, frame_id='aruco_map', auto_arm=False, tolerance=0.2):
    navigate(x=x, y=y, z=z, yaw=yaw, speed=speed, frame_id=frame_id, auto_arm=auto_arm)

    while not rospy.is_shutdown():
        telemetry = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telemetry.x ** 2 + telemetry.y ** 2 + telemetry.z ** 2) < tolerance:
            break
        rospy.sleep(0.2)

navigate_wait(frame_id='body', auto_arm=True)
rospy.sleep(5)
navigate_wait(frame_id='aruco_103')
rospy.sleep(5)
navigate_wait(z=0.3, frame_id='body')
rospy.sleep(5)
land()
