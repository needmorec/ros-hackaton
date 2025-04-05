FROM osrf/ros:noetic-desktop-full

RUN apt update && \
    apt install -y python3-catkin-tools
