# CENG 487 Assignment3 by
# Bugrahan Donmez
# April 2019

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from vec3d import Vec3d
from mat3d import Mat3d
from camera import Camera
from shape import Shape
from scene import Scene
import time
import math
from input_operations import InputOperations

ESCAPE = '\033'
ADD = '\053'
SUBS = '\055'
RIGHT_ARROW = '\062'
LEFT_ARROW = '\061'

X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0

window = 0


def InitGL(Width, Height):
    global texture
    texture = glGenTextures(1)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)


def ReSizeGLScene(Width, Height):
    if Height == 0:
        Height = 1

    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def keyPressed(*args):
    # If escape is pressed, kill everything.
    if args[0] == ESCAPE:
        sys.exit()
    # If plus is pressed, adds subdivison
    elif args[0] == ADD:
        shape.add_subdivison()
    # If minus is pressed, removes subdivison
    elif args[0] == SUBS:
        shape.remove_subdivison()
    # If left arrow is pressed, rotate left
    elif args[0] == GLUT_KEY_LEFT:
        shape.push_to_stack(Mat3d.rotation(0, -10, 0))
        shape.construct_transform_matrix()
        shape.transform()
    # If right arrow is pressed, rotate right
    elif args[0] == GLUT_KEY_RIGHT:
        shape.push_to_stack(Mat3d.rotation(0, 10, 0))
        shape.construct_transform_matrix()
        shape.transform()


def main():
    # Defines global elements to use 
    global window
    global shape
    global scene
    global camera
    global camera_pos
    global camera_front
    global camera_up
    global camera_speed

    # Initiate scene
    scene = Scene()

    # Change coordinates of camera_pos and camera_up to change camera properties
    camera_pos = Vec3d(0, 0, 2, 1)
    camera_front = Vec3d(0, 0, -1, 1)
    camera_up = Vec3d(0, 1, 0, 1)
    camera_speed = 0.05

    # The second argument is for target. Change for target object. Add camera to the scene
    camera = Camera(camera_pos, Vec3d(0, 0, 0, 1), camera_up, camera_front)
    scene.add(camera)

    # Create a generic shape
    shape = Shape()

    # Read shape from the file and add to the scene
    input_ops = InputOperations()
    input_ops.read_file()
    shape.vertices_list, shape.faces = input_ops.parse_contents()
    scene.add(shape)

    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    glutInitWindowSize(640, 480)

    glutInitWindowPosition(0, 0)

    window = glutCreateWindow("Bugrahan Donmez - Computer Graphics")

    glutDisplayFunc(scene.draw_scene)

    # Uncomment this line to get full screen.
    # glutFullScreen()

    glutIdleFunc(scene.draw_scene)

    glutReshapeFunc(ReSizeGLScene)

    glutSpecialFunc(keyPressed)
    glutKeyboardFunc(keyPressed)

    InitGL(640, 480)

    glutMainLoop()


print("Hit ESC key to quit.\n")
print ("Operations: ")
print ("=> Hit + to add subdivision")
print ("=> Hit - to add subdivision")
print ("=> Hit right arrow to rotate 10 degrees to the y axis")
print ("=> Hit left arrow to rotate 10 degrees to the y axis")
main()
