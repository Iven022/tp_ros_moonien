
### Square Trajectory using PoseStamped

## Description

This package contains a node publisher.py that will calculate the coordinates of x and y in order to follow the trajectory of a square. The package also contains a launch file which will automatically open the rviz software alongside a toggle button. The button will have the functionality of controlling the movement of the square.


## To install this package 

1) First you need to install the toggle button package made by https://github.com/Kramoth.

Clone it into the src folder in your catkin workspace 

```sh
cd ~/catkin_ws/src
git clone https://github.com/Kramoth/button_gui.git
catkin build
source ~/catkin_ws/devel/setup.bash
```

2) Then repeat the same process with the tp_ros_moonien package:

```sh
cd ~/catkin_ws/src
git clone https://github.com/Iven022/tp_ros_moonien.git
catkin build
source ~/catkin_ws/devel/setup.bash
```

## To run this node
After following the installation process, run the following code in the catkin workspace

```sh
roslaunch tp_ros_moonien carer.launch
```

You can also run the nodes separately with

```sh
roscore
```

```sh
rosrun button_gui button_node.py
```

```sh
rosrun tp_ros_moonien sub.py
```
## Do not multi-click the toggle button, the node may crash, please wait atleast 5 seconds before pressing again.
