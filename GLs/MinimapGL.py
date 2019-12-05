# Модуль описуе OpenGL віджет мінімапи

from math import *
from OpenGL.GL import *
from PyQt5.QtWidgets import QOpenGLWidget


# Клас віджету мінімапи
class MinimapGL(QOpenGLWidget):
    # Позиційні поля
    xPos = 0
    zPos = 0

    # Конструктор віджету
    def __init__(self, signalRange, xPos, zPos, parent=None):
        # Конструюємо класи предків
        super(MinimapGL, self).__init__(parent)

        # Встановлюємо дальність сигналу
        self.signalRange = signalRange * 0.045
        # Встановлюємо пропорцию координатів
        self.coordinatesProportion = self.signalRange / 2
        # Встановлюємо початкову позицію
        self.setPose(xPos, zPos)

    # Метод встановлення позиції квадрокоптера
    def setPose(self, xPos, zPos):
        # Встановлюємо позицію квадрокоптера на мінімапі
        # Ділимо поточні координати на пропорцию
        self.xPos = xPos/self.coordinatesProportion
        self.zPos = zPos/self.coordinatesProportion
        # Оновлюємо віджет
        self.update()

    # Метод ініціалізування віджета
    def initializeGL(self):
        # Встановлюємо колір фону
        glClearColor(1.0, 1.0, 1.0, 1.0)
        # Відчищаємо віджет
        glClear(GL_COLOR_BUFFER_BIT)

    # Метод змінення розміру віджету
    def resizeGL(self, w, h):
        # Встановлюємо режим матриці
        glMatrixMode(GL_PROJECTION)
        # Завантажуємо матрицю
        glLoadIdentity()
        # Встановлюємо параметри проекції
        glOrtho(-50, 50, -50, 50, -50.0, 50.0)
        # Встановлюємо точку зору
        glViewport(0, 0, w, h)

    # Метод відображення віджету
    def paintGL(self):
        # Встановлюємо колір
        glColor3f(1.0, 0.0, 0.0)
        # Малюємо червоний прямокутник оператора
        glRectf(1, 0, -1, -2)

        # Малюємо коло
        self.draw_loop(0, 0, 45, 100)

        # Встановлюємо колір
        glColor3f(0.0, 0.0, 1.0)
        # Малюємо синій прямокутник квадрокоптера
        glRectf(-self.zPos+1, self.xPos, -self.zPos-1, self.xPos-2)

    # Метод малювання кола
    @staticmethod
    def draw_loop(x, y, Radius, amountSegments):
        # Починаємо малювання кола
        glBegin(GL_LINE_LOOP)
        # Малюємо сегменти в циклі
        for SegmentInx in range(amountSegments):
            # Встановлюємо параметри сегменту
            angle = 2 * pi * float(SegmentInx) / float(amountSegments)
            dx = Radius * cos(angle)
            dy = Radius * sin(angle)
            # Малюємо сегмент
            glVertex2f(x + dx, y + dy)
        # Завершуємо малювання
        glEnd()
