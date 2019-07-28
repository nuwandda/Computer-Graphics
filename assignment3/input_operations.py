# CENG 487 Assignment3 by
# Bugrahan Donmez
# April 2019


import sys
from sets import Set
from vec3d import Vec3d


class InputOperations:
    def __init__(self):
        self.contents = []

    def read_file(self):
        with open(sys.argv[1], 'r') as f:
            self.contents = f.readlines()

    def parse_contents(self):
        vertices = []
        faces = []
        for line in self.contents:
            if line[0] == 'v':
                temp_line = line.split()
                vertices.append(Vec3d(float(temp_line[1]), float(temp_line[2]), float(temp_line[3]), 1.0))
            elif line[0] == 'f':
                temp_faces = line.split()
                temp_list = []
                for index, vertex in enumerate(temp_faces):
                    if vertex == 'f':
                        continue
                    else:
                        temp_list.append(vertices[int(vertex) - 1])
                faces.append(temp_list)
        return Set(vertices), faces
