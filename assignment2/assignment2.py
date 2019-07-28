# CENG 487 Assignment2 by
# Bugrahan Donmez
# March 2019

# Note:
# -----
# This Uses PyOpenGL and PyOpenGL_accelerate packages.  It also uses GLUT for UI.
# To get proper GLUT support on linux don't forget to install python-opengl package using apt
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from vec3d import Vec3d
from mat3d import Mat3d
from camera import Camera
from shape import Shape
import cube
import pyramid
import time
import math

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'
ADD = '\053'
SUBS = '\055'

X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0

# Number of the glut window.
window = 0


# A general OpenGL initialization function.  Sets all of the initial parameters.
def InitGL(Width, Height):  # We call this right after our OpenGL window is created.
    global texture
    texture = glGenTextures(1)
    glClearColor(0.0, 0.0, 0.0, 0.0)  # This Will Clear The Background Color To Black
    glClearDepth(1.0)  # Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)  # The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)  # Enables Depth Testing
    glShadeModel(GL_SMOOTH)  # Enables Smooth Color Shading

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Reset The Projection Matrix
    # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)

    cube_shape.subdivision_list = [
        [Vec3d(1.0, -1.0, -1.0, 1.0), Vec3d(1.0, 1.0, -1.0, 1.0), Vec3d(-1.0, 1.0, -1.0, 1.0),
         Vec3d(-1.0, -1.0, -1.0, 1.0)],
        [Vec3d(1.0, -1.0, 1.0, 1.0), Vec3d(1.0, 1.0, 1.0, 1.0), Vec3d(-1.0, 1.0, 1.0, 1.0),
         Vec3d(-1.0, -1.0, 1.0, 1.0)],
        [Vec3d(1.0, -1.0, -1.0, 1.0), Vec3d(1.0, 1.0, -1.0, 1.0), Vec3d(1.0, 1.0, 1.0, 1.0),
         Vec3d(1.0, -1.0, 1.0, 1.0)],
        [Vec3d(-1.0, -1.0, 1.0, 1.0), Vec3d(-1.0, 1.0, 1.0, 1.0), Vec3d(-1.0, 1.0, -1.0, 1.0),
         Vec3d(-1.0, -1.0, -1.0, 1.0)],
        [Vec3d(1.0, 1.0, 1.0, 1.0), Vec3d(1.0, 1.0, -1.0, 1.0), Vec3d(-1.0, 1.0, -1.0, 1.0),
         Vec3d(-1.0, 1.0, 1.0, 1.0)],
        [Vec3d(1.0, -1.0, -1.0, 1.0), Vec3d(1.0, -1.0, 1.0, 1.0), Vec3d(-1.0, -1.0, 1.0, 1.0),
         Vec3d(-1.0, -1.0, -1.0, 1.0)]]

    pyramid_shape.subdivision_list = [
        [Vec3d(0.0, 1.0, 0.0, 1.0), Vec3d(-1.0, -1.0, 1.0, 1.0), Vec3d(1.0, -1.0, 1.0, 1.0)],
        [Vec3d(0.0, 1.0, 0.0, 1.0), Vec3d(-1.0, -1.0, 1.0, 1.0), Vec3d(0.0, -1.0, -1.0, 1.0)],
        [Vec3d(0.0, 1.0, 0.0, 1.0), Vec3d(0.0, -1.0, -1.0, 1.0), Vec3d(1.0, -1.0, 1.0, 1.0)],
        [Vec3d(-1.0, -1.0, 1.0, 1.0), Vec3d(0.0, -1.0, -1.0, 1.0), Vec3d(1.0, -1.0, 1.0, 1.0)]]


# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:  # Prevent A Divide By Zero If The Window Is Too Small
        Height = 1

    glViewport(0, 0, Width, Height)  # Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


# The main drawing function.
def DrawGLScene():
    global X_AXIS, Y_AXIS, Z_AXIS
    global DIRECTION
    # Clear The Screen And The Depth Buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  # Reset The View

    gluLookAt(camera_pos.vector[0], camera_pos.vector[1], camera_pos.vector[2],
              camera_pos.sum_vectors(camera_front)[0], camera_pos.sum_vectors(camera_front)[1],
              camera_pos.sum_vectors(camera_front)[2],
              camera_up.vector[0], camera_up.vector[1], camera_up.vector[2])

    # Turns on wireframe mode
    # Use GL_FILL to turn off
    glPolygonMode(GL_FRONT, GL_LINE)
    glPolygonMode(GL_BACK, GL_LINE)

    glTranslatef(-1.5, 0.0, -6.0)
    cube_shape.draw_cube()
    glTranslatef(3.0, 0.0, 0.0)
    pyramid_shape.draw_pyramid()

    #  since this is double buffered, swap the buffers to display what just got drawn.
    glutSwapBuffers()
    # Type different argument to change waiting time


# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)
def keyPressed(*args):
    # If escape is pressed, kill everything.
    if args[0] == ESCAPE:
        sys.exit()
    # If plus is pressed, adds subdivison
    elif args[0] == ADD:
        cube_shape.add_subdivison()
        pyramid_shape.add_subdivision()
    # If minus is pressed, removes subdivison
    elif args[0] == SUBS:
        cube_shape.remove_subdivison()
        pyramid_shape.remove_subdivison()


def main():
    # Defines global elements to use 
    global window
    global cube_shape
    global pyramid_shape
    global camera
    global camera_pos
    global camera_front
    global camera_up
    global camera_speed

    # Change coordinates of camera_pos and camera_up to change camera properties
    camera_pos = Vec3d(3, 3, 10, 1)
    camera_front = Vec3d(0, 0, -1, 1)
    camera_up = Vec3d(0, 1, 0, 1)
    camera_speed = 0.05

    # The second argument is for target. Change for target object
    camera = Camera(camera_pos, Vec3d(0, 0, 0, 1), camera_up)

    cube_shape = cube.Cube()
    pyramid_shape = pyramid.Pyramid()

    # For now we just pass glutInit one empty argument. I wasn't sure what should or could be passed in (tuple, list, ...)
    # Once I find out the right stuff based on reading the PyOpenGL source, I'll address this.
    glutInit(sys.argv)

    # Select type of Display mode:
    #  Double buffer
    #  RGBA color
    # Alpha components supported
    # Depth buffer
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    # get a 640 x 480 window
    glutInitWindowSize(640, 480)

    # the window starts at the upper left corner of the screen
    glutInitWindowPosition(0, 0)

    # Okay, like the C version we retain the window id to use when closing, but for those of you new
    # to Python (like myself), remember this assignment would make the variable local and not global
    # if it weren't for the global declaration at the start of main.
    window = glutCreateWindow("Jeff Molofee's GL Code Tutorial ... NeHe '99")

    # Register the drawing function with glut, BUT in Python land, at least using PyOpenGL, we need to
    # set the function pointer and invoke a function to actually register the callback, otherwise it
    # would be very much like the C version of the code.
    glutDisplayFunc(DrawGLScene)

    # Uncomment this line to get full screen.
    # glutFullScreen()

    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)

    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)

    # Register the function called when the keyboard is pressed.
    glutKeyboardFunc(keyPressed)

    # Initialize our window.
    InitGL(640, 480)

    # Start Event Processing Engine
    glutMainLoop()


# Print message to console, and kick off the main to get it rolling.
print("Hit ESC key to quit.")
main()
