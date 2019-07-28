# CENG 487 Assignment2 by
# Bugrahan Donmez
# March 2019

from mat3d import Mat3d
from vec3d import Vec3d


class Shape:

    def __init__(self):
        """Consructor of class
        """
        self.vertices_list = []
        self.transform_operations_stack = []
        self.transform_matrix = Mat3d().transform_matrix

    def add_vertex(self, vertices):
        """Adds vertex to the shape
        
        Arguments:
            vertices {Vec3d} -- Vec3d object that contains points
        """
        self.vertices_list.append(vertices)

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
        for i in range(len(self.transform_operations_stack)):
            self.transform_matrix = Mat3d.multiply_matrices_for_transform(self.transform_matrix, self.pop_from_stack())
        # return self.transform_matrix.transform_matrix

    def transform(self):
        """Applies transformation to the vertices
            
            Arguments:
                Shape {Shape} -- Shape to change
                matrix {List} -- Transform matrix
        """
        for j in range(len(self.vertices_list)):
            temp = Mat3d.multipy_matrices(self.transform_matrix, self.vertices_list[j].homo_vector)
            self.vertices_list[j] = Vec3d(temp[0][0], temp[1][0], temp[2][0], temp[3][0])
