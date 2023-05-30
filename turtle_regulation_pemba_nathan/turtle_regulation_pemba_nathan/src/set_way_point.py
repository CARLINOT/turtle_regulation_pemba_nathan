#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from math import atan2

# Variable globale pour stocker la pose de la tortue
current_pose = Pose()

# Callback appelée lorsqu'un message est reçu sur le topic "pose"
def pose_callback(msg):
    global current_pose
    current_pose = msg

# Initialisation du nœud ROS
rospy.init_node('turtle_regulation_nom1_nom2')

# Souscription au topic "pose" avec la fonction de rappel pose_callback
rospy.Subscriber('pose', Pose, pose_callback)

# Définition du waypoint avec les coordonnées (7, 7)
waypoint = (7, 7)

# Calcul de l'angle désiré
desired_angle = atan2(waypoint[1] - current_pose.y, waypoint[0] - current_pose.x)

# Calcul de l'erreur
error = atan2(atan2(waypoint[1] - current_pose.y, waypoint[0] - current_pose.x) - current_pose.theta)

# Calcul de la commande en cap du robot
command = error

# Utilisation de la commande pour piloter le robot

# ...

# Boucle principale ROS
rospy.spin()
