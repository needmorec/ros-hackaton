import rospy
from clover import srv
from std_srvs.srv import Trigger
import math
from clover.srv import SetLEDEffect
from sensor_msgs.msg import Range

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
set_effect = rospy.ServiceProxy('led/set_effect', SetLEDEffect)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger) #для посадки

def navigate_wait(x=0, y=0, z=1.5, yaw=float('nan'),speed=0.5, frame_id='aruco_map', auto_arm=False, tolerance=0.2):
    navigate(x=x, y=y, z=z, yaw=yaw, speed=speed, frame_id=frame_id, auto_arm=auto_arm)
    print('coords: x = {} y = {}'.format(x,y))
    #if (yaw != 'nan'):
    #rospy.sleep(1)

    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
            print(z)
            print(dist)
            print(z - dist)

            break
        rospy.sleep(0.2)

def range_callback(msg):
    # Обработка новых данных с дальномера
    global dist
    dist = msg.range



def polet1(): 
    # navigate_wait(z=1.5, frame_id='body', auto_arm=True)
    navigate_wait(x=0.8, y=0.8, yaw = math.radians(90))
    navigate_wait(x=-0.5, y=0.8, yaw = math.radians(90))
    navigate_wait(x=1.6, y=0.8, yaw = math.radians(90))
    navigate_wait(x=1.6, y=0.8, z=0.5, yaw = math.radians(0))
    rospy.sleep(5)
    land()

def polet2(): 
    # navigate_wait(z=1.5, frame_id='body', auto_arm=True)
    navigate_wait(x=0.8, y=1.2, yaw = math.radians(90))
    navigate_wait(x=1.6, y=1.2, yaw = math.radians(90))
    navigate_wait(x=1.6, y=1.2, z=0.5, yaw = math.radians(0))
    rospy.sleep(5)
    land()



rospy.Subscriber('rangefinder/range', Range, range_callback)

navigate_wait(z=1.5, frame_id='body', auto_arm=True)

while  not rospy.is_shutdown():
    a = input("Enter a number 1 - clockwise 2 - counterclockwise 0 - land")
    if a == '1':
        polet2()
    elif a == '2':
        polet1()
    elif a == '0':
        land()
    else:
        land()

