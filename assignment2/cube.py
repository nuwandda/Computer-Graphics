# CENG 487 Assignment2 by
# Bugrahan Donmez
# March 2019


import math
from vec3d import Vec3d
from shape import Shape
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Cube(Shape):

    def __init__(self):
        """
            Constructor for Cube
        """
        Shape.__init__(self)
        self.subdivision_list = [self.vertices_list]

    def add_subdivison(self):
        """
            Function that add subdivison. Finds all the vertices of a plane
            and get middle points. Then, repeats for left points.
        """
        temp_sub_vertices = []
        for plane in (self.subdivision_list):
            temp_plane = []
            center = Vec3d((plane[0].x + plane[2].x) / 2, (plane[0].y + plane[2].y) / 2, (plane[0].z + plane[2].z) / 2,
                           1)
            for index in range(len(plane)):
                v1 = Vec3d(0, 0, 0, 0)
                v2 = Vec3d(0, 0, 0, 0)
                v3 = Vec3d(0, 0, 0, 0)
                v4 = Vec3d(0, 0, 0, 0)
                temp_index = index + 1

                if index + 1 == len(plane):
                    temp_index = 0

                v1 = plane[index]

                v2.x = (plane[index].x + plane[temp_index].x) / 2
                v2.y = (plane[index].y + plane[temp_index].y) / 2
                v2.z = (plane[index].z + plane[temp_index].z) / 2
                v2.w = plane[index].w

                v3 = center

                v4.x = (plane[index].x + plane[index - 1].x) / 2
                v4.y = (plane[index].y + plane[index - 1].y) / 2
                v4.z = (plane[index].z + plane[index - 1].z) / 2
                v4.w = plane[index].w
                temp_sub_vertices.append([v1, v2, v3, v4])

        self.subdivision_list = temp_sub_vertices

    def remove_subdivison(self):
        """
            Function that removes subdivisions. It removes by finding predecessor
            points of mid points
        """
        temp_sub_vertices = []
        for index in range(0, len(self.subdivision_list) - 1, 4):
            v1 = Vec3d(0, 0, 0, 0)
            v2 = Vec3d(0, 0, 0, 0)
            v3 = Vec3d(0, 0, 0, 0)
            v4 = Vec3d(0, 0, 0, 0)

            v1.x = self.subdivision_list[index + 0][0].x
            v1.y = self.subdivision_list[index + 0][0].y
            v1.z = self.subdivision_list[index + 0][0].z
            v1.w = self.subdivision_list[index + 0][0].w

            v2.x = self.subdivision_list[index + 1][0].x
            v2.y = self.subdivision_list[index + 1][0].y
            v2.z = self.subdivision_list[index + 1][0].z
            v2.w = self.subdivision_list[index + 1][0].w

            v3.x = self.subdivision_list[index + 2][0].x
            v3.y = self.subdivision_list[index + 2][0].y
            v3.z = self.subdivision_list[index + 2][0].z
            v3.w = self.subdivision_list[index + 2][0].w

            v4.x = self.subdivision_list[index + 3][0].x
            v4.y = self.subdivision_list[index + 3][0].y
            v4.z = self.subdivision_list[index + 3][0].z
            v4.w = self.subdivision_list[index + 3][0].w

            temp_sub_vertices.append([v1, v2, v3, v4])
        self.subdivision_list = temp_sub_vertices

    def draw_cube(self):
        """
            Draw function to draw cube
        """
        for item in self.subdivision_list:
            glBegin(GL_QUADS)
            glColor3f(0.5, 0.5, 0.5)
            glVertex3f(item[0].x, item[0].y, item[0].z)
            glVertex3f(item[1].x, item[1].y, item[1].z)
            glVertex3f(item[2].x, item[2].y, item[2].z)
            glVertex3f(item[3].x, item[3].y, item[3].z)
            glEnd()
