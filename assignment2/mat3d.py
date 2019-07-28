# CENG 487 Assignment2 by
# Bugrahan Donmez
# March 2019

import math


class Mat3d:

    def __init__(self):
        """Constructor of class
        """
        self.transform_matrix = [[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]]


    @staticmethod
    def multipy_matrices(matrix1, matrix2):
        """Multiplies 4x4 and 4x1 matrices
        
        Arguments:
            matrix1 {List} -- 4x4 Matrix
            matrix2 {List} -- 4x1 Matrix
        
        Returns:
            List -- Result after multiplication
        """
        result = [[0],[0],[0],[0]] 

        # iterating by row of matrix1
        for i in range(len(matrix1)): 

            # iterating by coloum by matrix2
            for j in range(len(matrix2[0])): 

                # iterating by rows of matrix2
                for k in range(len(matrix2)): 
                    result[i][j] += matrix1[i][k] * matrix2[k][j] 
        return result

    @staticmethod
    def multiply_matrices_for_transform(matrix1, matrix2):
        """Multiplies 4x4 and 4x4 matrices
        
        Arguments:
            matrix1 {List} -- 4x4 Matrix
            matrix2 {List} -- 4x4 Matrix
        
        Returns:
            List -- Result after multiplication
        """
        result = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]] 

        # iterating by row of matrix1
        for i in range(len(matrix1)): 

            # iterating by coloum by matrix2
            for j in range(len(matrix2[0])): 

                # iterating by rows of matrix2
                for k in range(len(matrix2)): 
                    result[i][j] += matrix1[i][k] * matrix2[k][j] 
        return result

    @staticmethod
    def translation(dx, dy, dz):
        """Return translation matrix
        
        Arguments:
            dx {Float} -- Factor for x
            dy {Float} -- Factor for y
            dz {Float} -- Factor for z
        
        Returns:
            List -- Translation Matrix
        """
        t_matrix = [[1, 0, 0, dx],
                    [0, 1, 0, dy],
                    [0, 0, 1, dz],
                    [0, 0, 0, 1]]
        return t_matrix

    @staticmethod
    def scale(scale_factor_x, scale_factor_y, scale_factor_z):
        """Returns scale matrix
        
        Arguments:
            scale_factor_x {Float} -- Factor for x
            scale_factor_y {Float} -- Factor for y
            scale_factor_z {Float} -- Factor for z
        
        Returns:
            List -- Scale Matrix
        """
        s_matrix = [[scale_factor_x, 0, 0, 0],
                    [0, scale_factor_y, 0, 0],
                    [0, 0, scale_factor_z, 0],
                    [0, 0, 0, 1]]
        return s_matrix

    @staticmethod
    def rotation(x_axis, y_axis, z_axis):
        """Returns rotation matrix. Only type for rotation angle. Once per axis and rotation.
        
        Arguments:
            x_axis {Float} -- Degree of rotation for x
            y_axis {Float} -- Degree of rotation for y
            z_axis {Float} -- Degree of rotation for z
        
        Returns:
            List -- Rotation Matrix
        """
        if y_axis == 0 and z_axis == 0:
            r_matrix = [[1, 0, 0, 0],
                        [0, math.cos(math.radians(x_axis)), -(math.sin(math.radians(x_axis))), 0],
                        [0, math.sin(math.radians(x_axis)), math.cos(math.radians(x_axis)), 0],
                        [0, 0, 0, 1]]
        elif x_axis == 0 and z_axis == 0:
            r_matrix = [[math.cos(math.radians(y_axis)), 0, math.sin(math.radians(y_axis)), 0],
                        [0, 1, 0, 0],
                        [-(math.sin(math.radians(y_axis))), 0, math.cos(math.radians(y_axis)), 0],
                        [0, 0, 0, 1]]
        elif x_axis == 0 and y_axis == 0:
            r_matrix = [[math.cos(math.radians(z_axis)), -(math.sin(math.radians(z_axis))), 0, 0],
                        [math.sin(math.radians(z_axis)), math.cos(math.radians(z_axis)), 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]]

        return r_matrix
