# CENG 487 Assignment3 by
# Bugrahan Donmez
# April 2019

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from camera import Camera
from shape import Shape


class Scene(object):

    def __init__(self):
        """
            Constructor of class
        """
        self.shape = None
        self.camera = None

    def add(self, element):
        """
        :param element: An object to add to scene.
        """
        if isinstance(element, Camera):
            self.camera = element
        elif isinstance(element, Shape):
            self.shape = element

    # The main drawing function.
    def draw_scene(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        gluLookAt(self.camera.camera_pos.vector[0], self.camera.camera_pos.vector[1], self.camera.camera_pos.vector[2],
                  self.camera.camera_pos.sum_vectors(self.camera.camera_front)[0],
                  self.camera.camera_pos.sum_vectors(self.camera.camera_front)[1],
                  self.camera.camera_pos.sum_vectors(self.camera.camera_front)[2],
                  self.camera.camera_up.vector[0], self.camera.camera_up.vector[1], self.camera.camera_up.vector[2])

        # Turns on wireframe mode
        # Use GL_FILL to turn off
        glPolygonMode(GL_FRONT, GL_LINE)
        glPolygonMode(GL_BACK, GL_LINE)

        glTranslatef(0.0, 0.0, -6.0)
        self.shape.draw()
        glRasterPos3f(-7, -5, -6.0)
        text = "Level : " + str(self.shape.subdivision_level)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

        glutSwapBuffers()
