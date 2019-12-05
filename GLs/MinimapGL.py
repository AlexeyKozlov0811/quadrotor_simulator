# ������ ������ OpenGL ����� ������

from math import *
from OpenGL.GL import *
from PyQt5.QtWidgets import QOpenGLWidget


# ���� ������ ������
class MinimapGL(QOpenGLWidget):
    # �������� ����
    xPos = 0
    zPos = 0

    # ����������� ������
    def __init__(self, signalRange, xPos, zPos, parent=None):
        # ����������� ����� ������
        super(MinimapGL, self).__init__(parent)

        # ������������ �������� �������
        self.signalRange = signalRange * 0.045
        # ������������ ��������� ����������
        self.coordinatesProportion = self.signalRange / 2
        # ������������ ��������� �������
        self.setPose(xPos, zPos)

    # ����� ������������ ������� �������������
    def setPose(self, xPos, zPos):
        # ������������ ������� ������������� �� �����
        # ĳ���� ������ ���������� �� ���������
        self.xPos = xPos/self.coordinatesProportion
        self.zPos = zPos/self.coordinatesProportion
        # ��������� �����
        self.update()

    # ����� ������������� ������
    def initializeGL(self):
        # ������������ ���� ����
        glClearColor(1.0, 1.0, 1.0, 1.0)
        # ³������� �����
        glClear(GL_COLOR_BUFFER_BIT)

    # ����� ������� ������ ������
    def resizeGL(self, w, h):
        # ������������ ����� �������
        glMatrixMode(GL_PROJECTION)
        # ����������� �������
        glLoadIdentity()
        # ������������ ��������� ��������
        glOrtho(-50, 50, -50, 50, -50.0, 50.0)
        # ������������ ����� ����
        glViewport(0, 0, w, h)

    # ����� ����������� ������
    def paintGL(self):
        # ������������ ����
        glColor3f(1.0, 0.0, 0.0)
        # ������� �������� ����������� ���������
        glRectf(1, 0, -1, -2)

        # ������� ����
        self.draw_loop(0, 0, 45, 100)

        # ������������ ����
        glColor3f(0.0, 0.0, 1.0)
        # ������� ���� ����������� �������������
        glRectf(-self.zPos+1, self.xPos, -self.zPos-1, self.xPos-2)

    # ����� ��������� ����
    @staticmethod
    def draw_loop(x, y, Radius, amountSegments):
        # �������� ��������� ����
        glBegin(GL_LINE_LOOP)
        # ������� �������� � ����
        for SegmentInx in range(amountSegments):
            # ������������ ��������� ��������
            angle = 2 * pi * float(SegmentInx) / float(amountSegments)
            dx = Radius * cos(angle)
            dy = Radius * sin(angle)
            # ������� �������
            glVertex2f(x + dx, y + dy)
        # ��������� ���������
        glEnd()
