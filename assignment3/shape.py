# CENG 487 Assignment3 by
# Bugrahan Donmez
# April 2019

from mat3d import Mat3d
from vec3d import Vec3d
from sets import Set
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Shape(object):

    def __init__(self):
        """Constructor of class
        """
        self.vertices_list = Set([])
        self.faces = []
        self.subdivision_level = 0
        self.transform_operations_stack = []
        self.transform_matrix = Mat3d().transform_matrix

    def add_vertex(self, vertices):
        """Adds vertex to the shape
        
        Arguments:
            vertices {Vec3d} -- Vec3d object that contains points
        """
        self.vertices_list.add(vertices)

    def remove_vertex(self, vertices):
        """Removes vertex from shape
        
        Arguments:
            vertices {Vec3d} -- Vec3d object that contains points
        """
        self.vertices_list.remove(vertices)

    def push_to_stack(self, matrix):
        """Pushes matrix to operations stack
        
        Arguments:
            matrix {List} -- Operation matrix
        """
        self.transform_operations_stack.append(matrix)

    def pop_from_stack(self):
        """Pops matrix from operations stack
        
        Returns:
            List -- Operation matrix
        """
        popped_matrix = self.transform_operations_stack.pop()
        return popped_matrix

    def construct_transform_matrix(self):
        """Constructs transformation matrix

            Arguments:
                shape {Shape} -- Shape to change
                mat {Mat3d} -- Matrix class related to given Shape
        """
        self.transform_matrix = Mat3d().reset_transform_matrix()
        for i in range(len(self.transform_operations_stack)):
            self.transform_matrix = Mat3d.multiply_matrices_for_transform(self.transform_matrix, self.pop_from_stack())

    def transform(self):
        """Applies transformation to the vertices

            Arguments:
                Shape {Shape} -- Shape to change
                matrix {List} -- Transform matrix
        """
        for vertex in self.vertices_list:
            temp = Mat3d.multiply_matrices(self.transform_matrix, vertex.homo_vector)
            vertex.x = temp[0][0]
            vertex.y = temp[1][0]
            vertex.z = temp[2][0]
            vertex.w = temp[3][0]

    def add_subdivison(self):
        """
            Function that add subdivisions. Finds all the vertices of a plane
            and get middle points. Then, repeats for left points.
        """
        temp_sub_vertices = []
        for plane in self.faces:
            center = Vec3d(float((plane[0].x + plane[2].x) / 2), float((plane[0].y + plane[2].y) / 2),
                           float((plane[0].z + plane[2].z) / 2),
                           1)
            for index in range(len(plane)):
                v2 = Vec3d(0, 0, 0, 0)
                v4 = Vec3d(0, 0, 0, 0)
                temp_index = index + 1

                if index + 1 == len(plane):
                    temp_index = 0

                v1 = plane[index]

                v2.x = float((plane[index].x + plane[temp_index].x) / 2)
                v2.y = float((plane[index].y + plane[temp_index].y) / 2)
                v2.z = float((plane[index].z + plane[temp_index].z) / 2)
                v2.w = plane[index].w

                v3 = center

                v4.x = float((plane[index].x + plane[index - 1].x) / 2)
                v4.y = float((plane[index].y + plane[index - 1].y) / 2)
                v4.z = float((plane[index].z + plane[index - 1].z) / 2)
                v4.w = plane[index].w
                temp_sub_vertices.append([v1, v2, v3, v4])

                self.vertices_list.add(v1)
                self.vertices_list.add(v2)
                self.vertices_list.add(v3)
                self.vertices_list.add(v4)

        self.faces = temp_sub_vertices
        self.subdivision_level += 1

    def remove_subdivison(self):
        """
            Function that removes subdivisions. It removes by finding predecessor
            points of mid points
        """
        if self.subdivision_level != 0:
            temp_sub_vertices = []
            for index in range(0, len(self.faces) - 1, 4):
                temp_sub_vertices.append([self.faces[index + 0][0], self.faces[index + 1][0], self.faces[index + 2][0],
                                          self.faces[index + 3][0]])

            self.faces = temp_sub_vertices
            self.subdivision_level -= 1
        else:
            print ("Subdivision level is already 0!")

    def draw(self):
        """
            Draw function to draw
        """
        for item in self.faces:
            glBegin(GL_QUADS)
            glColor3f(0.5, 0.5, 0.5)
            for vertex in item:
                glVertex3f(vertex.x, vertex.y, vertex.z)
            glEnd()
