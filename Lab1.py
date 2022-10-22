#!/usr/bin/env python3
from cmath import cos, sin
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


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


#dick start
    glColor3f(1.0, 1.0, 0.0)
    glBegin( GL_LINE_LOOP )
    for x in range (0, 64):
        angle = (6.2832 * x / 64)
        x = 0.5 * cos(angle)
        y = 0.5 * sin(angle)
        glVertex2f( float(x.real) * 50 + 25, float(y.real) * 50 - 50)
    glEnd()

    glColor3f(1.0, 1.0, 0.0)
    glBegin( GL_LINE_LOOP )
    for x in range (0, 64):
        angle = (6.2832 * x / 64)
        x = 0.5 * cos(angle)
        y = 0.5 * sin(angle)
        glVertex2f( float(x.real) * 50 - 25, float(y.real) * 50 - 50)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(25,-25)
    glVertex2f(25,75)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-25,-25)
    glVertex2f(-25,75)
    glEnd()

    glColor3f(1.0, 1.0, 0.0)
    glBegin( GL_LINE_LOOP )
    for x in range (0, 33):
        angle = (6.2832 * x / 64)
        x = 0.5 * cos(angle)
        y = 0.5 * sin(angle)
        glVertex2f( float(x.real) * 50, float(y.real) * 50 + 75)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0,85)
    glVertex2f(0,100)
    glEnd()

    #dick end

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
