# CENG 487 Assignment2 by
# Bugrahan Donmez
# March 2019

from mat3d import Mat3d
from vec3d import Vec3d
import numpy as np


class Camera:
    def __init__(self, camera_pos, camera_target, up):
        """
        Constructor class for camera

        :param Vec3d camera_pos: The desired position of the camera
        :param Vec3d camera_target: The target point
        :param Vec3d up: Up vector that points towards the
        """
        self.camera_pos = camera_pos
        temp_dir = Vec3d(0, 0, 0, 0)
        temp_dir.vector = list(np.array(camera_pos.vector) - np.array(camera_target.vector))
        self.camera_dir = Vec3d(temp_dir.vector[0] / temp_dir.norm(), temp_dir.vector[1] / temp_dir.norm(),
                                temp_dir.vector[2] / temp_dir.norm(), 0)
        temp_right_axis = Vec3d(0, 0, 0, 0)
        temp_right_axis.vector = (up.cross_product(self.camera_dir))
        self.camera_right = Vec3d(temp_right_axis.vector[0] / temp_right_axis.norm(),
                                  temp_right_axis.vector[1] / temp_right_axis.norm(),
                                  temp_right_axis.vector[2] / temp_right_axis.norm(), 0)
        temp_camera_up = Vec3d(0, 0, 0, 0)
        temp_camera_up.vector = self.camera_dir.cross_product(self.camera_right)
        self.camera_up = Vec3d(temp_camera_up.vector[0], temp_camera_up.vector[1], temp_camera_up.vector[2], 0)

    def model_matrix(self):
        pass

    def view_matrix(self):
        pass

    def projection_matrix(self):
        pass
