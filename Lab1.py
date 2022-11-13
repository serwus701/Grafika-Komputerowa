#!/usr/bin/env python3
import random
import sys

from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass

def sierpinski(x_pos, y_pos, a_size, b_size, depth):
    global max_depth
    if depth >= max_depth:
        rectangle(x_pos, y_pos, a_size, b_size, 0)
    else:
        a_size /= 3
        b_size /= 3

        sierpinski(x_pos, y_pos, a_size, b_size, depth + 1)
        sierpinski(x_pos + a_size, y_pos, a_size, b_size, depth + 1)
        sierpinski(x_pos + 2 * a_size, y_pos, a_size, b_size, depth + 1)
        sierpinski(x_pos, y_pos + b_size, a_size, b_size, depth + 1)
        #sierpinski(x_pos + a_size, y_pos + b_size, a_size, b_size, depth + 1)
        sierpinski(x_pos + 2 * a_size, y_pos + b_size, a_size, b_size, depth + 1)
        sierpinski(x_pos, y_pos + 2 * b_size, a_size, b_size, depth + 1)
        sierpinski(x_pos + a_size, y_pos + 2 * b_size, a_size, b_size, depth + 1)
        sierpinski(x_pos + 2 * a_size, y_pos + 2 * b_size, a_size, b_size, depth + 1)

def rectangle(x_pos, y_pos, a_size, b_size, deformation_seed):

    random.seed(deformation_seed)
    deformation = random.random()

    a_size *= deformation
    b_size *= deformation

    global seed

    random.seed(seed)
    red = random.random()
    random.seed(seed + 1)
    green = random.random()
    random.seed(seed + 2)
    blue = random.random()

    random.seed(seed)
    seed = random.random()

    #print(red, green, blue)
    #time.sleep(1)
    glColor3f(red, green, blue)

    glBegin(GL_TRIANGLES)
    glVertex2f(x_pos, y_pos)
    glVertex2f(x_pos + a_size, y_pos)
    glVertex2f(x_pos, y_pos + b_size)
    glEnd()


    glBegin(GL_TRIANGLES)
    glVertex2f(x_pos + a_size, y_pos)
    glVertex2f(x_pos, y_pos + b_size)
    glVertex2f(x_pos + a_size, y_pos + b_size)
    glEnd()


def triangles():
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 1.0)
    glVertex2f(0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.0, 90.0)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(90.0, 0.0)
    glEnd()


    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0.0, 1.0)
    glVertex2f(0.0, 0.0)
    glColor3f(1.0, 0.3, 0.0)
    glVertex2f(0.0, 50.0)
    glColor3f(0.0, 0.5, 0.0)
    glVertex2f(-50.0, 0.0)
    glEnd()

    rectangle(-90, -70, 30, 50, 1)

    glFlush()


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
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    global max_depth
    max_depth = 4

    default_seed = random.random()
    global seed

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
        #triangles()
        
        seed = default_seed
        sierpinski(0, 0, 50, 50, 0)

        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
