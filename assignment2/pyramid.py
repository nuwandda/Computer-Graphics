# CENG 487 Assignment2 by
# Bugrahan Donmez
# March 2019


import math
from vec3d import Vec3d
from shape import Shape
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Pyramid(Shape):

    def __init__(self):
        """
            Constructor of Pyramid
        """
        Shape.__init__(self)
        self.subdivision_list = [self.vertices_list]

    def add_subdivision(self):
        """
            Function that adds subdivison. Finds all the vertices of a plane
            and gets middle points. Then, repeats for left points.
        """
        temp_sub_vertices = []
        for plane in (self.subdivision_list):
            current_mids = []
            mid_m_01 = Vec3d(0, 0, 0, 0)
            mid_m_12 = Vec3d(0, 0, 0, 0)
            mid_m_20 = Vec3d(0, 0, 0, 0)

            mid_m_01.x = (plane[0].x + plane[1].x) / 2
            mid_m_01.y = (plane[0].y + plane[1].y) / 2
            mid_m_01.z = (plane[0].z + plane[1].z) / 2
            mid_m_01.w = plane[0].w

            mid_m_12.x = (plane[1].x + plane[2].x) / 2
            mid_m_12.y = (plane[1].y + plane[2].y) / 2
            mid_m_12.z = (plane[1].z + plane[2].z) / 2
            mid_m_12.w = plane[1].w

            mid_m_20.x = (plane[2].x + plane[0].x) / 2
            mid_m_20.y = (plane[2].y + plane[0].y) / 2
            mid_m_20.z = (plane[2].z + plane[0].z) / 2
            mid_m_20.w = plane[2].w

            current_mids = [mid_m_01, mid_m_12, mid_m_20]
            temp_sub_vertices.append(current_mids)

            for index in range(len(current_mids)):
                v0 = Vec3d(0, 0, 0, 0)
                v1 = Vec3d(0, 0, 0, 0)
                v2 = Vec3d(0, 0, 0, 0)

                v0.x = plane[index].x
                v0.y = plane[index].y
                v0.z = plane[index].z

                v1.x = current_mids[index].x
                v1.y = current_mids[index].y
                v1.z = current_mids[index].z

                v2.x = current_mids[index - 1].x
                v2.y = current_mids[index - 1].y
                v2.z = current_mids[index - 1].z

                temp_sub_vertices.append([v0, v1, v2])

        self.subdivision_list = temp_sub_vertices

    def remove_subdivison(self):
        """
            Function that removes subdivisions. It removes by finding predecessor
            points of mid points
        """
        temp_sub_vertices = []
        for index in range(0, len(self.subdivision_list) - 1, 4):
            v0 = Vec3d(0, 0, 0, 0)
            v1 = Vec3d(0, 0, 0, 0)
            v2 = Vec3d(0, 0, 0, 0)

            v0.x = self.subdivision_list[index + 1][0].x
            v0.y = self.subdivision_list[index + 1][0].y
            v0.z = self.subdivision_list[index + 1][0].z
            v0.w = self.subdivision_list[index + 1][0].w

            v1.x = self.subdivision_list[index + 2][0].x
            v1.y = self.subdivision_list[index + 2][0].y
            v1.z = self.subdivision_list[index + 2][0].z
            v1.w = self.subdivision_list[index + 2][0].w

            v2.x = self.subdivision_list[index + 3][0].x
            v2.y = self.subdivision_list[index + 3][0].y
            v2.z = self.subdivision_list[index + 3][0].z
            v2.w = self.subdivision_list[index + 3][0].w

            temp_sub_vertices.append([v0, v1, v2])

        self.subdivision_list = temp_sub_vertices

    def draw_pyramid(self):
        """
            Draw function to draw cube
        """
        for item in self.subdivision_list:
            glBegin(GL_POLYGON)
            glColor3f(0.5, 0.5, 0.5)
            glVertex3f(item[0].x, item[0].y, item[0].z)
            glVertex3f(item[1].x, item[1].y, item[1].z)
            glVertex3f(item[2].x, item[2].y, item[2].z)
            glEnd()
