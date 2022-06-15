import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    kia_cfg = os.path.join(
        get_package_share_directory('ichthus_driver'),
        'cfg',
        'kia.yaml'
    )
    mcm_cfg = os.path.join(
        get_package_share_directory('ichthus_driver'),
        'cfg',
        'mcm.yaml'
    )
    pid_cfg = os.path.join(
        get_package_share_directory('pid_control'),
        'cfg',
        'pid.yaml'
    )
    return LaunchDescription([
        Node(
            package = 'ichthus_driver',
            executable = 'mcm_management_node',
            parameters = [mcm_cfg],
            output="log",
        ),
        Node(
            package = 'ichthus_driver',
            executable = 'kia_reader_node',
            parameters = [kia_cfg],
            output="log",

        ),
        Node(
            package = 'pid_control',
            executable = 'pid_node',
            parameters = [pid_cfg,
            {
                'str_kp': 25.0, # 75.0. 125.0
                'right_thres' : 0.075,
                'left_thres' : -0.025 
            }],
            output="screen",
        )
        
    ])
