FROM ros:jazzy-ros-base

ARG USERNAME=ubuntu
ARG UID=1000
ARG GID=1000

# Install some dependencies packages
RUN apt update -q \
    && apt upgrade -q -y \
    && apt install -y \
    software-properties-common \
    ros-jazzy-ament-cmake-vendor-package \
    libboost-all-dev \
    python3-pip \
    cargo \
    clang \
    git \
    ros-jazzy-fastcdr \
    xauth \
    ros-dev-tools \
    ros-jazzy-rviz2 \
#    ros-jazzy-gazebo-ros-pkgs \
#    ros-jazzy-gazebo-ros2-control \
    ros-jazzy-xacro \
    ros-jazzy-joint-state-publisher-gui \
    ros-jazzy-joy \
    ros-jazzy-joy-teleop \
    ros-jazzy-ros2-control \ 
    ros-jazzy-ros2-controllers \
    ros-jazzy-serial-driver \
    ros-jazzy-twist-mux \
    ros-jazzy-rplidar-ros \
    ros-jazzy-teleop-twist-keyboard \   
    && apt clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Create and switch to user
# Check if GID exists; reuse it if it does, otherwise create the group
RUN echo "$USERNAME ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
#RUN usermod -aG rdma $USERNAME
RUN usermod -aG dialout $USERNAME
RUN echo 'root:20182018' | chpasswd

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
