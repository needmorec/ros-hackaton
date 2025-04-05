import rospy
from clover import srv
from std_srvs.srv import Trigger
import math


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

def navigate_wait(x=0, y=0, z=1.15, yaw=float('nan'),speed=0.4, frame_id='aruco_map', auto_arm=False, tolerance=0.2):
    navigate(x=x, y=y, z=z, yaw=yaw, speed=speed, frame_id=frame_id, auto_arm=auto_arm)
    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
            break
        rospy.sleep(0.2)

navigate_wait(z=1, speed=0.8, frame_id='body', auto_arm=True)
#print(get_telemetry().z)
#print(get_telemetry(frame_id='aruco_map').z)

rospy.sleep(10)
navigate_wait(z=1, x=0.0, y=-0.9)

rospy.sleep(10)

navigate_wait(z=1, x=0.0, y=0)

rospy.sleep(10)

#navigate_wait(z=0.9, x=0.0, y=-0.9)

#rospy.sleep(10)

#navigate_wait(z=0.9, x=0.0, y=0.0)

#rospy.sleep(10)

navigate_wait(x=0.0, y=0.0, z=0.5)

rospy.sleep(10)
land()


