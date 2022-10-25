#!/usr/bin/env python3
import sys
import random

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass

def rectangle(xPos, yPos, aSize, bSize, randomSeed):

    random.seed(randomSeed)
    deformation = random.random()

    aSize *= deformation
    bSize *= deformation

    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 1.0)
    glVertex2f(xPos, yPos)
    glVertex2f(xPos + aSize, yPos)
    glVertex2f(xPos, yPos + bSize)
    glEnd()


    #glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(xPos + aSize, yPos)
    glVertex2f(xPos, yPos + bSize)
    glVertex2f(xPos + aSize, yPos + bSize)
    glEnd()


def render(time):
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
