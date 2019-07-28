# Computer-Graphics
## Assignments of the Introduction to the Computer Graphics course.

### Rotate Polygons using your own vector and matrix classes
- There is a simple example file attached to this assignment.
- If you run this file you will see a triangle and a square on the screen.
- By utilizing your matrix and vector classes, you will rotate the square and the triangle around one their vertices.
- You need to do the rotation around the axis perpendicular to your window.
- So what i am asking you guys to do is this:
  - Write a 3d vector class vec3d which defines a vec3d(x,y,z,w) type and define methods for all of the possible vector and point manipulation operations like dot product, cross product, calculate projection to a basis vector, calculate angle between two vectors, in addition to vector arithmetic methods like addition, scalar multiplication, length calculation etc.
  - Write a 3d transform matrix class mat3d which defines a 4x4 matrix to do 3d transformations. Please also implement typical vec3d, mat3d operations like translation, rotation, scaling of a vec3d by a mat3d, in addition to mat3d algebra like multiplication, transpose etc.
  - Write an object class which hold information about vertices of an object and also the transformation matrix stack for Translation (T), Rotation Around X,Y,Z (RX, RY, RZ), and Scale (S). The class should also keep track of the order of transformation matrices like TRS, SRT, RTS.
  - Then use those classes to transform the triangle and square around one of their vertices. You can wait for a key press to do rotation incrementally or wait for a certain elapsed time since last update and then update the scene (People who does this time based updating will have a bonus for this assignment).
  - Please implement classes vec3d and mat3d in their respective files and apply them in the assignment.py file.
  
### Primitives in 3D
- Implement and display various primitives in 3d:
  - Sphere
  - Plane
  - Box
  - Cylinder
  - Torus
  - Pyramid
  - Platonic Solids
- Start with some predefined subdivisions depending on the primitive type but give user the ability to change the subdivisions by listening for key strokes on keyboard eg. "+" key for increasing subdivisions, "-" key for decreasing etc.
- You will also need to implement a Camera class so that we can display the object in the window from a user defined point.
- BONUS: Transformation of the viewing point (camera) using mouse buttons and Alt Key.
  - Alt + Left Mouse Button: Rotation around center of the object
  - Alt + Right Mouse Button: Move in and out along the x axis for getting closer and further away from the object
  - F key for resetting the view to fully enclose the primitive on screen

### Interactive Subdivision And Obj Parsing
- First of all since this is your third assignment, cleanup all the comments in the assignment#.py file that originates from the original file i gave you guys before starting this project. From now on the comments should only be your comments. And commenting is encouraged for me to better understand wat you do!
- Make a python program called assignment3.py
  - This program should be run as such:
    - assignment3.py objFile.obj
  - Upon launch, you should read the file specified in the first command line argument and parse its vertices and polygons and display it in a window.
    - You only need to parse vertices and faces and assume that there is only one object in the file. We will improve this parser later.
    - https://en.wikipedia.org/wiki/Wavefront_.obj_file
  - If the user presses on right and left arrow key the object is rotated around vertical, y, axis.
  - Please test the program with the attached obj files.
  - Once the obj file is parsed, user should have the ability to press on +, - keys to subdivide each polygon ( quad ) as such:
    - For each face calculate a point at the center of the face ( center being the average point of all vertices of the face )
    - For each edge calculate a mid point between its vertices.
    - Then connect each of those mid points to the center point of the face, to create 4 polygons (quads) per face.
    - If the user presses the + key, we subdivide the object and print the subdivision level on the window at the bottom left corner for each key press assuming the original object is at level 0.
    - If the user presses the - key, we display the object subdivided at level less than the current level. So if before pressing the - key our subdivision level is 2, after the click we show the object at subdivision level 1.
    - Draw edges as lines on screen too, so that we can see the effect of subdivision. 
