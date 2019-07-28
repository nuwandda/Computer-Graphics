# CENG 487 Assignment1 by 
# Bugrahan Donmez
# March 2019

class Shape:

    def __init__(self):
        """Consructor of class
        """
        self.vertices_list = []
        self.transform_operations_stack = []
    

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
