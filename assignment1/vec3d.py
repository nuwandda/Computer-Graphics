# CENG 487 Assignment1 by 
# Bugrahan Donmez
# March 2019

import math


class Vec3d:

    def __init__(self, x, y, z, w):
        """Constructor of class
        
        Arguments:
            x {[Float]} -- x-axis point
            y {[Float]} -- y-axis point
            z {[Float]} -- z-axis point
            w {[Float]} -- homogenoues point
        """
        self.w = w
        self.vector = [x, y, z]
        self.homo_vector = [[x], [y], [z], [w]]

    
    @property
    def x(self):
        """This function returns point from x-axis
        
        Returns:
            [float] -- Point from x-axis
        """
        
        return self.vector[0]

    
    @property
    def y(self):
        """This function returns point from y-axis
        
        Returns:
            [float] -- Point from y-axis
        """
        return self.vector[1]


    @property
    def z(self):
        """This function returns point from z-axis
        
        Returns:
            [float] -- Point from z-axis
        """
        return self.vector[2]


    @property
    def angle(self):
        """This function returns homogeneous point
        
        Returns:
            [float] -- Homogeneous Point
        """
        return self.w


    def sum_vectors(self, vector):
        """This function sums given vector with the vector inside
        
        Arguments:
            vector {[Vec3d]} -- Ved3d object to sums
        
        Returns:
            [List] -- List that contains the result after summation
        """
        result = [0, 0, 0]
        for i in range(len(self.vector)):
            result[i] += (self.vector[i] + vector.vector[i])
        return result


    def multiply_vectors(self, vector):
        """This function multiplies given vector with the inside one
        
        Arguments:
            vector {[Vec3d]} -- Vec3d object to multiply
        
        Returns:
            [Float] -- Result that contains the result after multiplication
        """
        return self.dot_product(vector)
        
    def scalar_mult(self, p):
        return [x * p for x in self.vector]

    def dot_product(self, vector):
        """This function applies dot product to given vector and inside one
        
        Arguments:
            vector {[Vec3d]} -- Vec3d object to apply dot product
        
        Returns:
            [Float] -- Result that contains the result after dot product
        """
        return (self.vector[0] * vector.vector[0]) + (self.vector[1] * vector.vector[1]) + (self.vector[2] * vector.vector[2])


    def cross_product(self, vector):
        """This function applies cross product to given vector and inside one
        
        Arguments:
            vector {[Vec3d]} -- Vec3d object to apply dot product
        
        Returns:
            [List] -- List that contains the result from cross product
        """
        cx = self.vector[1] * vector.vector[2] - self.vector[2] * vector.vector[1]
        cy = self.vector[2] * vector.vector[0] - self.vector[0] * vector.vector[2]
        cz = self.vector[0] * vector.vector[1] - self.vector[1] * vector.vector[0]
        return [cx, cy, cz]

    
    def norm(self):
        return math.sqrt((self.vector[0] * self.vector[0]) + (self.vector[1] * self.vector[1]) + (self.vector[2] * self.vector[2]))
    

    def projection_onto_plane(self, vector):
        """Return projection of a vector onto vector
        
        Arguments:
            vector {Vec3d} -- Vec3d object
        
        Returns:
            List -- List that contains scalar multiplied matrix
        """
        return vector.scalar_mult(self.dot(vector) / vector.dot(vector))


    def angle_between_vectors(self, vector):
        """This function return the angle in degree between two vectors
        
        Arguments:
            vector {[Vec3d]} -- Vec3d object to apply dot product
        
        Returns:
            [Float] -- Angle between the vectors
        """
        return math.radians(math.acos(self.dot_product(vector.vector) / (self.norm() *  np.linalg.norm(vector.vector))))