# ������ ������ �������� OpenGL �����

from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtWidgets import QOpenGLWidget

import pywavefront
from pywavefront import visualization
from math import *


# ���� ��������� ������
class MainGL(QOpenGLWidget):
    # �������� ����
    xPos = 0.2
    yPos = 0.2
    zPos = 0.2
    facing = 0
    phi = 0
    theta = 0

    # ����������� �����
    def __init__(self, signalRange, xPos, yPos, zPos, parent=None):
        # ����������� ������
        super(MainGL, self).__init__(parent)

        # ������������ �������� �������
        self.signalRange = signalRange * 0.069
        # ������������ ��������� ���������
        self.coordinatesProportion = self.signalRange
        # ������������ ��������� �������
        self.setPose(xPos, yPos, zPos, 0)
        # ����������� 3D ������
        self.model = pywavefront.Wavefront("Objects\\quadrotor_base.obj", create_materials=False)

    # ����� ������������� ������
    def initializeGL(self):
        # ������������ ����� �������
        glMatrixMode(GL_PROJECTION)
        # ����������� �������
        glLoadIdentity()
        # ������������ �����������
        gluPerspective(35, 1.0, 0.1, 1000)
        # ������������ ������ ����� �������
        glMatrixMode(GL_MODELVIEW)
        # ������� �������� �������
        glEnable(GL_DEPTH_TEST)
        # ������������ ���� ����
        glClearColor(0.5, 0.5, 0.5, 0)
        # ³������� �����
        glClear(GL_COLOR_BUFFER_BIT)
        # ������������ ����� ����
        glViewport(-100, -100, 800, 800)

    # ����� ������� ������ ������
    def resizeGL(self, w, h):
        # ������������ ����� �������
        glMatrixMode(GL_PROJECTION)
        # ����������� �������
        glLoadIdentity()
        # ������������ ����� ����
        glViewport(0, 0, w, h)

    # ����� ����������� ������
    def paintGL(self):
        # ³������� ����� ����� �� �������
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # ����������� �������
        glLoadIdentity()
        # ������������ ��������� ��������
        glOrtho(-2, 42, -30, 30, -40.0, 15.0)
        # ��������� ������� � ������� ���������
        glTranslatef(0, 0, 0)
        # ���������� ������� ����� ������ �� 35 �������
        glRotatef(35, 1, 1, 0)
        # ������� ����
        self.drawGrid()
        # ������� ������������
        self.drawQuad()

    # ����� ��������� �������������
    def drawQuad(self):
        # �������� ������� � ����
        glPushMatrix()
        # ������������ ����
        glColor3f(0.0, 0.0, 1.0)
        # ��������� ������� � �������
        glTranslatef(self.xPos, self.yPos, self.zPos)
        # ����������� ������������ ������� �� �
        glRotatef(self.phi, sin(radians(self.facing)), 0, cos(radians(self.facing)))
        glRotatef(-self.theta, cos(radians(self.facing)), 0, -sin(radians(self.facing)))
        glRotatef(self.facing, 0, 1, 0)
        # ��������� �� 90 ������� ������� �� �
        glRotatef(-90, 1, 0, 0)
        # ��������� �� 90 ������� ������� �� Z
        glRotatef(90, 0, 0, 1)
        # ������� �����
        glScale(0.6, 0.6, 0.6)
        # ������� 3D ������ �������������
        visualization.draw(self.model)
        # ��������� ������� � �����
        glPopMatrix()

    # ����� ��������� ����
    @staticmethod
    def drawGrid():
        # ������� ���� � ������ � z
        # ���� ��������� ���
        for i in range(60):
            # �������� ������� � ����
            glPushMatrix()
            if i < 30:
                # ������� 30 ��� �� ����� 0 �������
                # ������ ������� �� � �� �� z
                glTranslatef(0, 0, i)
            elif i < 60:
                # ������� 30 ��� �� ����� 90 �������
                # ������ ������� �� �-30 �� �� �
                glTranslatef(i - 30, 0, 0)
                # ���������� ������� �� -90 ������� ������� �� �
                glRotatef(-90, 0, 1, 0)
            # ������� ��
            glBegin(GL_LINES)
            # ������������ ����
            glColor3f(1, 0, 0)
            # ������������ ����� �����
            glVertex3f(0, -0.1, 0)
            # ������������ ����� ����� �� ��������� ������
            glVertex3f(29, -0.1, 0)
            # ��������� ��������� ���
            glEnd()
            # �������� ������� � �����
            glPopMatrix()

        # ������� ���� � ������ y x
        # ������� ������������ �� � ����
        for i in range(15):
            # �������� ������� � ����
            glPushMatrix()
            # ������ ������� � ����������
            glTranslatef(0, i, 0)
            # ��������� �������� ��
            glBegin(GL_LINES)
            # ������������ ����
            glColor3f(0, 1, 0)
            # ������������ ����� �����
            glVertex3f(0, -0.1, 0)
            # ������������ ����� ����� �� ��������� ������
            glVertex3f(29, -0.1, 0)
            # ��������� ��������� ���
            glEnd()
            # �������� ������� � �����
            glPopMatrix()
        # ������� ���������� �� � ����
        for i in range(30):
            # �������� ������� � ����
            glPushMatrix()
            # ������ ������� � ���������� � 0 0
            glTranslatef(i, 0, 0)
            # ���������� ������� �� -90 ������� ������� �� z
            glRotatef(-90, 0, 0, 1)
            # ��������� �������� ��
            glBegin(GL_LINES)
            # ������������ ����
            glColor3f(0, 1, 0)
            # ������������ ����� �����
            glVertex3f(0, -0.1, 0)
            # ������������ ����� ����� �� ��������� ������
            glVertex3f(-14, -0.1, 0)
            # ��������� ��������� ���
            glEnd()
            # �������� ������� � �����
            glPopMatrix()

        # ������� ���� � ������ z y
        # ������� ������������ �� � ����
        for i in range(15):
            # �������� ������� � ����
            glPushMatrix()
            # ������ ������� � ���������� 29 � 0
            glTranslatef(29, i, 0)
            # ���������� ������� �� -90 ������� ������� �� �
            glRotatef(-90, 0, 1, 0)
            # ��������� �������� ��
            glBegin(GL_LINES)
            # ������������ ����
            glColor3f(0, 0, 1)
            # ������������ ����� �����
            glVertex3f(0, -0.1, 0)
            # ������������ ����� ����� �� ��������� ������
            glVertex3f(29, -0.1, 0)
            # ��������� ��������� ���
            glEnd()
            # �������� ������� � �����
            glPopMatrix()
        # ������� ���������� �� � ����
        for i in range(30):
            # �������� ������� � ����
            glPushMatrix()
            # ������ ������� � ���������� 29 0 �
            glTranslatef(29, 0, i)
            # ���������� ������� �� -90 ������� ������� �� z
            glRotatef(-90, 0, 0, 1)
            # ��������� �������� ��
            glBegin(GL_LINES)
            # ������������ ����
            glColor3f(0, 0, 1)
            # ������������ ����� �����
            glVertex3f(0, -0.1, 0)
            # ������������ ����� ����� �� ��������� ������
            glVertex3f(-14, -0.1, 0)
            # ��������� ��������� ���
            glEnd()
            # �������� ������� � �����
            glPopMatrix()

    # ����� ������������ ������� �������������
    def setPose(self, xPos, yPos, zPos, facing, phi=0, theta=0):
        # ������������ ���������� � ����������� ������� �� ������� ��������� �� ���������
        self.xPos = 14.5 + -zPos / self.coordinatesProportion
        self.yPos = 0.5 + yPos / self.coordinatesProportion
        self.zPos = 14.5 + -xPos / self.coordinatesProportion
        # ������������ ������ ���� �������������
        self.facing = facing
        self.phi = phi
        self.theta = theta
        # ��������� �����
        self.update()
