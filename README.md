# ROS2_Gazebo_Sim
Use ROS2 and Gazebo to simulate a inverted pendulum

## URDF
Our robot is available in [Onshape](https://cad.onshape.com/documents/bdab1611a3eab19e5396d226/w/19445b51027e00211a809da2/e/15daaa00878ae93e9c4f4117?renderMode=0&uiState=64098bb731dacb56d46fb628)

Firstly, we should export the urdf file by the tool [Onshape-to-robot](https://onshape-to-robot.readthedocs.io/en/latest/), you can refer to their [documentation](https://onshape-to-robot.readthedocs.io/en/latest/) or [youtube](https://www.youtube.com/watch?v=C8oK4uUmbRw) tutorial. 

### Export URDF

In our project, we generate the urdf in the following step. 

```sh
ros2 pkg create --build-type  ament_cmake ipc_model_description
cd ipc_model_description
mkdir urdf
gedit urdf/config.json
```
after finishing `config.json`: 
```sh
cd ..
onshape-to-robot urdf/
```

Then you would get the urdf file and corresponding stl files. What's more, we should replace all the 'revolute' by 'continuous' in the urdf file because joints in our robot do not have limits. It seems that onshape-to-robot cannot export continuous joints so we have to do it manually. 

