FROM ros:humble-ros-base

ARG USERNAME=rosdev
ARG UID=1000
ARG GID=$UID

# Install some dependencies packages
RUN apt update -q \
    && apt upgrade -q -y \
    && apt install -y \
    software-properties-common \
    python3-pip \
    xauth \
    ros-dev-tools \
    ros-humble-rviz2 \
#    ros-humble-gazebo-ros-pkgs \
#    ros-humble-gazebo-ros2-control \
    ros-humble-xacro \
    ros-humble-joint-state-publisher-gui \
    ros-humble-joy \
    ros-humble-joy-teleop \
    ros-humble-ros2-control \ 
    ros-humble-ros2-controllers \
    ros-humble-serial-driver \
    ros-humble-twist-mux \	
    && apt clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Create and switch to user
RUN groupadd -g $GID $USERNAME \
&& useradd -lm -u $UID -g $USERNAME -s /bin/bash $USERNAME \
&& echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
#RUN usermod -aG rdma $USERNAME
RUN usermod -aG dialout $USERNAME

USER $USERNAME


ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES graphics,utility,compute

# Create workspace so that user own this directory
RUN mkdir -p /home/$USERNAME/ros2_ws/src
WORKDIR /home/$USERNAME/ros2_ws

# Copy configuration files
RUN echo 'source /opt/ros/'$ROS_DISTRO'/setup.bash' >> /home/$USERNAME/.bashrc \
    && echo 'source /home/'$USERNAME'/ros2_ws/install/setup.bash' >> /home/$USERNAME/.bashrc

# Setup entrypoint
COPY ./ros_entrypoint.sh /
# ENTRYPOINT ["/ros_entrypoint.sh"]
# CMD ["bash"]
