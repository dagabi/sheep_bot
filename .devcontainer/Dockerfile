FROM ros:humble-ros-base

ARG USERNAME=rosdev
ARG UID=1000
ARG GID=$UID

RUN apt update -q; apt install curl
RUN rm -f /usr/share/keyrings/ros2-latest-archive-keyring.gpg && curl https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros2-latest-archive-keyring.gpg

# Install some dependencies packages
RUN apt update -q \
    && apt upgrade -q -y \
    && apt install -y \
    software-properties-common \
    python3-pip \
    xauth \
    vim \
    ros-dev-tools \
    ros-humble-rviz2 \
    ros-humble-ros-gz \
    ros-humble-ros-gz-sim \
    ros-humble-gz-ros2-control \
    ros-humble-xacro \
    ros-humble-joint-state-publisher-gui \
    ros-humble-joy \
    ros-humble-joy-teleop \
    ros-humble-teleop-twist-joy \
    ros-humble-ros2-control \ 
    ros-humble-ros2-controllers \
    ros-humble-serial-driver \
    ros-humble-twist-mux \
    ros-humble-twist-stamper \
    ros-humble-rplidar-ros \
    ros-humble-teleop-twist-keyboard \	
    ros-humble-slam-toolbox \
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
#COPY ./ros_entrypoint.sh /
# ENTRYPOINT ["/ros_entrypoint.sh"]
# CMD ["bash"]
