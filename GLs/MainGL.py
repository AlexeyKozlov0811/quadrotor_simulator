# Модуль описуе основний OpenGL віджет

from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtWidgets import QOpenGLWidget

import pywavefront
from pywavefront import visualization
from math import *


# Клас основного віджету
class MainGL(QOpenGLWidget):
    # Позиційні поля
    xPos = 0.2
    yPos = 0.2
    zPos = 0.2
    facing = 0
    phi = 0
    theta = 0

    # Конструктор класу
    def __init__(self, signalRange, xPos, yPos, zPos, parent=None):
        # Конструюємо предків
        super(MainGL, self).__init__(parent)

        # Встановлюємо дальність сигналу
        self.signalRange = signalRange * 0.069
        # Встановлюємо пропорцію координат
        self.coordinatesProportion = self.signalRange
        # Встановлюємо початкову позицію
        self.setPose(xPos, yPos, zPos, 0)
        # Завантажуємо 3D модель
        self.model = pywavefront.Wavefront("Objects\\quadrotor_base.obj", create_materials=False)

    # Метод ініціалізування віджета
    def initializeGL(self):
        # Встановлюємо режим матриці
        glMatrixMode(GL_PROJECTION)
        # Завантажуємо матрицю
        glLoadIdentity()
        # Встановлюємо перспективу
        gluPerspective(35, 1.0, 0.1, 1000)
        # Встановлюємо другий режим матриці
        glMatrixMode(GL_MODELVIEW)
        # Вмикаємо перевірку глибини
        glEnable(GL_DEPTH_TEST)
        # Встановлюємо колір фону
        glClearColor(0.5, 0.5, 0.5, 0)
        # Відчищаємо буфер
        glClear(GL_COLOR_BUFFER_BIT)
        # Встановлюємо точку зору
        glViewport(-100, -100, 800, 800)

    # Метод змінення розміру віджету
    def resizeGL(self, w, h):
        # Встановлюємо режим матриці
        glMatrixMode(GL_PROJECTION)
        # Завантажуємо матрицю
        glLoadIdentity()
        # Встановлюємо точку зору
        glViewport(0, 0, w, h)

    # Метод відображення віджету
    def paintGL(self):
        # Відчищаємо буфер коліру та глибини
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # Завантажуємо матрицю
        glLoadIdentity()
        # Встановлюємо параметри проекції
        glOrtho(-2, 42, -30, 30, -40.0, 15.0)
        # Переміщуємо матрицю в початок координат
        glTranslatef(0, 0, 0)
        # Прокручуємо матрицю через вектор на 35 градусів
        glRotatef(35, 1, 1, 0)
        # Малюємо сітку
        self.drawGrid()
        # Малюємо квадрокоптер
        self.drawQuad()

    # Метод малювання квадрокоптера
    def drawQuad(self):
        # Заносимо матрицю в стек
        glPushMatrix()
        # Встановлюємо колір
        glColor3f(0.0, 0.0, 1.0)
        # Переміщуємо матрицю в позицію
        glTranslatef(self.xPos, self.yPos, self.zPos)
        # Прокручуемо квадрокоптер навколо осі У
        glRotatef(self.phi, sin(radians(self.facing)), 0, cos(radians(self.facing)))
        glRotatef(-self.theta, cos(radians(self.facing)), 0, -sin(radians(self.facing)))
        glRotatef(self.facing, 0, 1, 0)
        # Повертаємо на 90 градусів навколо осі Х
        glRotatef(-90, 1, 0, 0)
        # Повертаємо на 90 градусів навколо ос Z
        glRotatef(90, 0, 0, 1)
        # Змінюємо розмір
        glScale(0.6, 0.6, 0.6)
        # Малюємо 3D модель квадрокоптера
        visualization.draw(self.model)
        # Повертаємо матрицю зі стека
        glPopMatrix()

    # Метод малювання сітки
    @staticmethod
    def drawGrid():
        # Малюємо сітку в площині х z
        # Цикл малювання ліній
        for i in range(60):
            # Заносимо матрицю в стек
            glPushMatrix()
            if i < 30:
                # Малюємо 30 ліній під кутом 0 градусів
                # Зміщуємо матрицю на і по осі z
                glTranslatef(0, 0, i)
            elif i < 60:
                # Малюємо 30 ліній під кутом 90 градусів
                # Зміщуємо матрицю на і-30 по осі х
                glTranslatef(i - 30, 0, 0)
                # Розвертаємо матрицю на -90 градусів навколо осі у
                glRotatef(-90, 0, 1, 0)
            # Малюємо лінії
            glBegin(GL_LINES)
            # Встановлюємо колір
            glColor3f(1, 0, 0)
            # Встановлюємо першу точку
            glVertex3f(0, -0.1, 0)
            # Встановлюємо другу точку та проводимо відрізок
            glVertex3f(29, -0.1, 0)
            # Завершуємо малювання ліній
            glEnd()
            # Виносимо матрицю зі стеку
            glPopMatrix()

        # Малюемо сітку в площині y x
        # Малюемо горизонтальні лінії в циклі
        for i in range(15):
            # Заносимо матрицю в стек
            glPushMatrix()
            # Зміщуємо матрицю в координати
            glTranslatef(0, i, 0)
            # Починаемо малювати лінії
            glBegin(GL_LINES)
            # Встановлюємо колір
            glColor3f(0, 1, 0)
            # Встановлюємо першу точку
            glVertex3f(0, -0.1, 0)
            # Встановлюємо другу точку та проводимо відрізок
            glVertex3f(29, -0.1, 0)
            # Завершуємо малювання ліній
            glEnd()
            # Виносимо матрицю зі стеку
            glPopMatrix()
        # Малюємо вертикальні лінії в циклі
        for i in range(30):
            # Заносимо матрицю в стек
            glPushMatrix()
            # Зміщуємо матрицю в координати і 0 0
            glTranslatef(i, 0, 0)
            # Розвертаємо матрицю на -90 градусів навколо осі z
            glRotatef(-90, 0, 0, 1)
            # Починаемо малювати лінії
            glBegin(GL_LINES)
            # Встановлюємо колір
            glColor3f(0, 1, 0)
            # Встановлюємо першу точку
            glVertex3f(0, -0.1, 0)
            # Встановлюємо другу точку та проводимо відрізок
            glVertex3f(-14, -0.1, 0)
            # Завершуємо малювання ліній
            glEnd()
            # Виносимо матрицю зі стеку
            glPopMatrix()

        # Малюємо сітку в площині z y
        # Малюемо горизонтальні лінії в циклі
        for i in range(15):
            # Заносимо матрицю в стек
            glPushMatrix()
            # Зміщуємо матрицю в координати 29 і 0
            glTranslatef(29, i, 0)
            # Розвертаємо матрицю на -90 градусів навколо осі у
            glRotatef(-90, 0, 1, 0)
            # Починаемо малювати лінії
            glBegin(GL_LINES)
            # Встановлюємо колір
            glColor3f(0, 0, 1)
            # Встановлюємо першу точку
            glVertex3f(0, -0.1, 0)
            # Встановлюємо другу точку та проводимо відрізок
            glVertex3f(29, -0.1, 0)
            # Завершуємо малювання ліній
            glEnd()
            # Виносимо матрицю зі стеку
            glPopMatrix()
        # Малюємо вертикальні лінії в циклі
        for i in range(30):
            # Заносимо матрицю в стек
            glPushMatrix()
            # Зміщуємо матрицю в координати 29 0 і
            glTranslatef(29, 0, i)
            # Розвертаємо матрицю на -90 градусів навколо осі z
            glRotatef(-90, 0, 0, 1)
            # Починаемо малювати лінії
            glBegin(GL_LINES)
            # Встановлюємо колір
            glColor3f(0, 0, 1)
            # Встановлюємо першу точку
            glVertex3f(0, -0.1, 0)
            # Встановлюємо другу точку та проводимо відрізок
            glVertex3f(-14, -0.1, 0)
            # Завершуємо малювання ліній
            glEnd()
            # Виносимо матрицю зі стеку
            glPopMatrix()

    # Метод встановлення позиції квадрокоптера
    def setPose(self, xPos, yPos, zPos, facing, phi=0, theta=0):
        # Встановлюемо координати з урахуванням зміщення від початку координат та пропорції
        self.xPos = 14.5 + -zPos / self.coordinatesProportion
        self.yPos = 0.5 + yPos / self.coordinatesProportion
        self.zPos = 14.5 + -xPos / self.coordinatesProportion
        # Встановлюемо напрям зору квадрокоптера
        self.facing = facing
        self.phi = phi
        self.theta = theta
        # Оновлюемо віджет
        self.update()
