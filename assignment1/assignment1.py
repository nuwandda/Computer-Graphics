# CENG 487 Assignment1 by 
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
from shape import Shape
import time

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'

# Number of the glut window.
window = 0


# A general OpenGL initialization function.  Sets all of the initial parameters.
def InitGL(Width, Height):  # We call this right after our OpenGL window is created.
    glClearColor(0.0, 0.0, 0.0, 0.0)  # This Will Clear The Background Color To Black
    glClearDepth(1.0)  # Enables Clearing Of The Depth Buffer
    glDepthFunc(GL_LESS)  # The Type Of Depth Test To Do
    glEnable(GL_DEPTH_TEST)  # Enables Depth Testing
    glShadeModel(GL_SMOOTH)  # Enables Smooth Color Shading

    # Below, we add vertices to the shapes
    triangle_shape.add_vertex(Vec3d(0.0, 1.0, 0.0, 1.0))
    triangle_shape.add_vertex(Vec3d(1.0, -1.0, 0.0, 1.0))
    triangle_shape.add_vertex(Vec3d(-1.0, -1.0, 0.0, 1.0))

    square_shape.add_vertex(Vec3d(-1.0, 1.0, 0.0, 1.0))
    square_shape.add_vertex(Vec3d(1.0, 1.0, 0.0, 1.0))
    square_shape.add_vertex(Vec3d(1.0, -1.0, 0.0, 1.0))
    square_shape.add_vertex(Vec3d(-1.0, -1.0, 0.0, 1.0))

    # Add operations here to perform transformation
    square_shape.push_to_stack(mat3d_square.rotation(0, 0, 5))
    triangle_shape.push_to_stack(mat3d_triangle.rotation(0, 0, 5))

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Reset The Projection Matrix
    # Calculate The Aspect Ratio Of The Window
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)


# The function called when our window is resized (which shouldn't happen if you enable fullscreen, below)
def ReSizeGLScene(Width, Height):
    if Height == 0:  # Prevent A Divide By Zero If The Window Is Too Small
        Height = 1

    glViewport(0, 0, Width, Height)  # Reset The Current Viewport And Perspective Transformation
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def construct_transform_matrix(shape, mat):
    """Constructs transformation matrix
        
        Arguments:
            shape {Shape} -- Shape to change
            mat {Mat3d} -- Matrix class related to given Shape
    """
    transform_matrix = mat.transform_matrix
    for i in range(len(shape.transform_operations_stack)):
        transform_matrix = mat.multiply_matrices_for_transform(transform_matrix, shape.pop_from_stack())
    return transform_matrix

def transform(shape, matrix):
    """Applies transformation to the vertices
        
        Arguments:
            Shape {Shape} -- Shape to change
            matrix {List} -- Transform matrix
    """
    for j in range(len(shape.vertices_list)):
        temp = Mat3d.multipy_matrices(matrix, shape.vertices_list[j].homo_vector)
        shape.vertices_list[j] = Vec3d(temp[0][0], temp[1][0], temp[2][0], temp[3][0])
        

# The main drawing function.
def DrawGLScene():
    # Clear The Screen And The Depth Buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  # Reset The View

    # Move Left 1.5 units and into the screen 6.0 units.
    glTranslatef(-1.5, 0.0, -6.0)

    # Since we have smooth color mode on, this will be great for the Phish Heads :-).
    # Draw a triangle
    glBegin(GL_POLYGON)  # Start drawing a polygon
    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex3f(triangle_shape.vertices_list[0].x, triangle_shape.vertices_list[0].y,
               triangle_shape.vertices_list[0].z)  # Top
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex3f(triangle_shape.vertices_list[1].x, triangle_shape.vertices_list[1].y,
               triangle_shape.vertices_list[1].z)  # Bottom Right
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex3f(triangle_shape.vertices_list[2].x, triangle_shape.vertices_list[2].y,
               triangle_shape.vertices_list[2].z)  # Bottom Left
    glEnd()  # We are done with the polygon

    # Move Right 3.0 units.
    glTranslatef(3.0, 0.0, 0.0)

    # Draw a square (quadrilateral)
    glColor3f(0.3, 0.5, 1.0)  # Bluish shade
    glBegin(GL_QUADS)  # Start drawing a 4 sided polygon
    glVertex3f(square_shape.vertices_list[0].x, square_shape.vertices_list[0].y,
               square_shape.vertices_list[0].z)  # Top Left
    glVertex3f(square_shape.vertices_list[1].x, square_shape.vertices_list[1].y,
               square_shape.vertices_list[1].z)  # Top Right
    glVertex3f(square_shape.vertices_list[2].x, square_shape.vertices_list[2].y,
               square_shape.vertices_list[2].z)  # Bottom Right
    glVertex3f(square_shape.vertices_list[3].x, square_shape.vertices_list[3].y,
               square_shape.vertices_list[3].z)  # Bottom Left
    glEnd()  # We are done with the polygon

    # Call transform function with related shape and transform matrix to perform transformation
    transform(square_shape, transform_matrix_square)
    transform(triangle_shape, transform_matrix_triangle)

    #  since this is double buffered, swap the buffers to display what just got drawn.
    glutSwapBuffers()
    # Type different argument to change waiting time
    time.sleep(2)


# The function called whenever a key is pressed. Note the use of Python tuples to pass in: (key, x, y)
def keyPressed(*args):
    # If escape is pressed, kill everything.
    if args[0] == ESCAPE:
        sys.exit()


def main():
    # Defines global elements to use 
    global window
    global triangle_shape
    global square_shape
    global mat3d_triangle
    global mat3d_square
    global transform_matrix_triangle
    global transform_matrix_square

    triangle_shape = Shape()
    square_shape = Shape()
    mat3d_triangle = Mat3d()
    mat3d_square = Mat3d()

    
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

    # Below, we construct transformation matrices for each Shape
    transform_matrix_triangle = construct_transform_matrix(triangle_shape, mat3d_triangle)
    transform_matrix_square = construct_transform_matrix(square_shape, mat3d_square)

    # Start Event Processing Engine
    glutMainLoop()


# Print message to console, and kick off the main to get it rolling.
print("Hit ESC key to quit.")
main()
