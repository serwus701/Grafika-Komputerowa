import math
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

N = 20


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def shutdown():
    pass

def calculate_egg_points():
    tab = [[[0.0] * 3 for _ in range(N)] for _ in range(N)]
    #print(tab)

    for i in range(N):
        u = 1/(N - 1) * i
        for j in range(N):
            v = 1/(N - 1) * j

            tab[i][j][0] = (-90 * u ** 5 + 225 * u ** 4 - 270 * u ** 3 + 180 * u ** 2 - 45 * u) \
                              * math.cos(math.pi * v)

            tab[i][j][1] = 160 * u ** 4 - 320 * u ** 3 + 160 * u ** 2 - 5

            tab[i][j][2] = (-90 * u ** 5 + 225 * u ** 4 - 270 * u ** 3 + 180 * u ** 2 - 45 * u) \
                              * math.sin(math.pi * v)

    return tab
def triangles_egg():
    tab = calculate_egg_points()

    for i in range(N - 1):
        for j in range(N - 1):
            glBegin(GL_TRIANGLES)

            glColor3f(0.75, 0.25, 0.34)

            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            glVertex3f(tab[i + 1][j][0], tab[i + 1][j][1], tab[i + 1][j][2])
            glVertex3f(tab[i][j + 1][0], tab[i][j + 1][1], tab[i][j + 1][2])

            glColor3f(0.21, 0.67, 0.84)

            glVertex3f(tab[i + 1][j + 1][0], tab[i + 1][j + 1][1], tab[i + 1][j + 1][2])
            glVertex3f(tab[i + 1][j][0], tab[i + 1][j][1], tab[i + 1][j][2])
            glVertex3f(tab[i][j + 1][0], tab[i][j + 1][1], tab[i][j + 1][2])

            glEnd()


def lines_egg():
    tab = calculate_egg_points()

    for i in range(N):
        for j in range(N):
            
            if i == N - 1:
                next_i = 0
            else:
                next_i = i + 1

            if j == N - 1:
                next_j = 0
            else:
                next_j = j + 1

            glColor3f(1, 1, 1)
            glBegin(GL_LINES)

            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            glVertex3f(tab[next_i][j][0], tab[next_i][j][1], tab[next_i][j][2])

            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            glVertex3f(tab[i][next_j][0], tab[i][next_j][1], tab[i][next_j][2])

            glEnd()

def pointsEgg():
    tab = calculate_egg_points()

    for i in range(N):
        for j in range(N):
            glColor3f(1, 1, 1)
            glBegin(GL_POINTS)

            glVertex(tab[i][j][0], tab[i][j][1], tab[i][j][2])

            glEnd()


def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0) 
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()


def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    spin(time * 180 / 3.1415)
    
    lines_egg()

    axes()

    glFlush()

def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()