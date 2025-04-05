import rospy
import math
from clover import srv
from std_srvs.srv import Trigger



rospy.init_node('flight')
get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate) # Отправиться в точку
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_altitude = rospy.ServiceProxy('set_altitude', srv.SetAltitude)
set_yaw = rospy.ServiceProxy('set_yaw', srv.SetYaw)
set_yaw_rate = rospy.ServiceProxy('set_yaw_rate', srv.SetYawRate)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger) #для посадки

def navigate_wait(x=0, y=0, z=0.8, yaw=float('nan'), speed=0.5, frame_id='aruco_map', auto_arm=False, tolerance=0.2):
    navigate(x=x, y=y, z=z, yaw=yaw, speed=speed, frame_id=frame_id, auto_arm=auto_arm)

    while not rospy.is_shutdown():
        telemetry = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telemetry.x ** 2 + telemetry.y ** 2 + telemetry.z ** 2) < tolerance:
            break
        rospy.sleep(0.2)

navigate_wait(frame_id='body', auto_arm=True)
rospy.sleep(3)
navigate_wait(frame_id='aruco_103')
rospy.sleep(3)
navigate_wait(frame_id='aruco_104')
rospy.sleep(3)
navigate_wait(frame_id='aruco_104')
rospy.sleep(3)
navigate_wait(frame_id='aruco_230')
rospy.sleep(3)
navigate_wait(frame_id='aruco_125')
rospy.sleep(3)
navigate_wait(z=0.4, frame_id='aruco_91')
rospy.sleep(3)
land()
