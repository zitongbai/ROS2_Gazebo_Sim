import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    # urdf file
    urdf_file_name = 'robot.urdf'
    urdf_file_path = os.path.join(get_package_share_directory('ipc_model_description'), 'urdf', urdf_file_name)
    robot_description_raw = open(urdf_file_path).read()
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        parameters=[{'robot_description': robot_description_raw}],
        output='screen'
    )

    # launch rviz2 with config file
    node_viz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', os.path.join(get_package_share_directory('ipc_model_description'), 'rviz', 'viz.rviz')],
        # parameters=[{'robot_description': robot_description_raw}],
        output='screen'
    )


    return LaunchDescription([
        node_viz,
        node_robot_state_publisher
    ])