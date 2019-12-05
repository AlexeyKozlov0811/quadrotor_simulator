# В цьому модулі опискується класс квадрокоптер, який визначає реакцію на команди керування

from math import *


# Клас квадрокоптера
class Quadrotor:
    # Позиційні поля
    xPos = 10.0
    yPos = 0.0
    zPos = 0.0
    facing = 0

    # Поля швидкості горизонтальних двигунів
    xEngine = 0
    zEngine = 0

    # Поля швидкості
    xSpeed = 0
    ySpeed = 0
    zSpeed = 0

    # Поля відстані від оператора
    maxDistance = 1000
    Distance = 10

    phi = 0  # вугол крена
    theta = 0  # вугол тангажа

    # Метод, що описує пересування квадрокоптера в просторі
    def move(self):
        # При кожному виклику до позиції додаємо вектор швидкості
        self.xPos += self.xSpeed
        self.yPos += self.ySpeed
        self.zPos += self.zSpeed
        # Перевіряємо, щоб координати висоти не були від'ємними
        if self.yPos < 0:
            self.yPos = 0.0
        # Обраховуємо нову відстань до оператора
        self.Distance = sqrt(self.xPos * self.xPos + self.yPos * self.yPos + self.zPos * self.zPos)

    # Медоти, що описують реакцію на команди контролю
    # Метод пересування по осі У, метод control_S - ідентичний в іншому напрямку
    def control_W(self):
        # Перевіряємо, що двигун не перевищує свою максимальну швидкість
        if self.ySpeed <= 5:
            # Прискорюємо на 1
            self.ySpeed += 1
        # Викликаємо метод пересування
        self.move()

    # Метод повороту в горизонтальній площині, метод control_D - ідентичний в іншому напрямку
    def control_A(self):
        # Перевіряємо що градус повороту в межах 360 градусів
        if self.facing < 359:
            # Додаємо до градусу повороту 1
            self.facing += 1
        else:
            # Якщо поточний градус 359, то при додаванні одиниці отримаємо 0
            self.facing = 0

    def control_S(self):
        if self.ySpeed >= -5:
            self.ySpeed -= 1
        self.move()

    def control_D(self):
        if self.facing > 0:
            self.facing -= 1
        else:
            self.facing = 359

    # Метод пересування вперед у горизонтальній площині, метод control_K - ідентичний в іншому напрямку
    def control_I(self):
        # Перевіряємо, що двигун не перевищує свою максимальну швидкість
        if self.xEngine <= 5:
            # Прискорюємо на 1
            self.xEngine += 1
        # Обраховуємо швидкості в горизонтальній площині з урахуванням градусу повороту в ній
        self.xSpeed = self.xEngine * round(cos(radians(self.facing)), 2)
        self.zSpeed = self.xEngine * round(sin(radians(self.facing)), 2)
        # Викликаємо метод пересування
        self.move()

    # Метод пересування вліво у горизонтальній площині, метод control_L - ідентичний в іншому напрямку
    def control_J(self):
        # Перевіряємо, що двигун не перевищує свою максимальну швидкість
        if self.zEngine <= 5:
            # Прискорюємо на 1
            self.zEngine += 1
        # Обраховуємо швидкості в горизонтальній площині з урахуванням градусу повороту в ній
        self.xSpeed = self.zEngine * round(sin(radians(-self.facing)), 2)
        self.zSpeed = self.zEngine * round(cos(radians(-self.facing)), 2)
        # Викликаємо метод пересування
        self.move()

    def control_K(self):
        if self.xEngine >= -5:
            self.xEngine -= 1
        self.xSpeed = self.xEngine * round(cos(radians(self.facing)), 2)
        self.zSpeed = self.xEngine * round(sin(radians(self.facing)), 2)
        self.move()

    def control_L(self):
        if self.zEngine >= -5:
            self.zEngine -= 1
        self.xSpeed = self.zEngine * round(sin(radians(-self.facing)), 2)
        self.zSpeed = self.zEngine * round(cos(radians(-self.facing)), 2)
        self.move()

    # Метод стабілізації положення, викликається при відсутності інших команд
    def stabilize(self):
        self.xSpeed = 0
        self.ySpeed = 0
        self.zSpeed = 0

        self.xEngine = 0
        self.zEngine = 0


class Quadrotor2(Quadrotor):
    p1T = 0
    p2T = 0
    p3T = 0
    p4T = 0
    p5T = 0
    p6T = 0
    p7T = 0
    p8T = 0
    p9T = 0
    p10T = 0
    p11T = 0
    p12T = 0
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    p5 = 0
    p6 = 0
    p8 = 0
    p10 = 0
    p12 = 0

    Ix = 1  # інерція х
    Iy = 1  # інерція у
    Iz = 1  # інерція z
    Jr = 1  # інерція ротора

    U1 = 0  # швидкість ротора
    U2 = 0
    U3 = 0
    U4 = 0

    l = 1
    g = 3
    m = 1  # масса
    b = 30  # тяга двигуна
    d = 0
    k = 1 / m
    w = 0

    Omega = 0
    omega1 = 0
    omega2 = 0
    omega3 = 0
    omega4 = 0

    omega21 = 0
    omega22 = 0
    omega23 = 0
    omega24 = 0

    phiTT = 0
    thetaTT = 0
    psiTT = 0
    zTT = 0
    xTT = 0
    yTT = 0
    phiT = 0
    thetaT = 0
    psiT = 0

    phi = 0  # вугол крена
    theta = 0  # вугол тангажа
    psi = 0  # вугол рискання

    def move(self):
        self.psi = self.facing
        # При кожному виклику до позиції додаємо вектор швидкості

        self.yPos += -self.g + (cos(radians(self.phi))) * cos(radians(self.theta)) * self.U1

        # правильные формулы
        # self.xPos += (cos(radians(self.phi)) * -cos(radians(self.theta+90)) * cos(radians(self.psi)) +
        #               sin(radians(self.phi)) * sin(radians(self.psi))) * self.U1 * self.k
        #
        # self.zPos += (-cos(radians(self.phi+90)) * cos(radians(self.theta)) * cos(radians(self.psi)) +
        #               sin(radians(self.theta)) * sin(radians(self.psi))) * self.U1 * self.k

        self.U1 = pow(self.omega1, 2) + pow(self.omega2, 2) + pow(self.omega3, 2) + pow(self.omega4, 2)

        self.U2 = self.l * (pow(self.omega4, 2) - pow(self.omega2, 2))

        self.U3 = self.l * (pow(self.omega3, 2) - pow(self.omega1, 2))

        self.U4 = (-pow(self.omega1, 2) + pow(self.omega2, 2) - pow(self.omega3, 2) + pow(self.omega4, 2))

        self.phi += self.U2/self.Jr

        self.theta += self.U3/self.Jr

        self.psi += self.U4/self.Jr

        self.facing = self.psi

        # формулы 3
        self.xPos += (cos(radians(self.phi)) * sin(radians(self.theta)) * cos(radians(self.psi)) +
                      sin(radians(self.phi)) * sin(radians(self.psi))) * self.U1

        self.zPos += -(cos(radians(self.phi)) * sin(radians(self.theta)) * sin(radians(self.psi)) -
                      sin(radians(self.phi)) * cos(radians(self.psi))) * self.U1


        # неправильные формулы
        # self.xPos += (cos(radians(self.phi)) * cos(radians(self.theta)) * cos(radians(self.psi)) +
        #               sin(radians(self.phi)) * sin(radians(self.psi))) * self.U1
        #
        # self.zPos += (cos(radians(self.phi)) * cos(radians(self.theta)) * cos(radians(self.psi)) +
        #               sin(radians(self.theta)) * cos(radians(self.psi))) * self.U1

        # Перевіряємо, щоб координати висоти не були від'ємними
        if self.yPos < 0:
            self.yPos = 0.0

        # Обраховуємо нову відстань до оператора
        self.Distance = sqrt(self.xPos * self.xPos + self.yPos * self.yPos + self.zPos * self.zPos)

    # Медоти, що описують реакцію на команди контролю
    # Метод пересування по осі У, метод control_S - ідентичний в іншому напрямку
    def control_W(self):
        # # Перевіряємо, що двигун не перевищує свою максимальну швидкість
        # if self.U1 <= self.b:
        #     # Прискорюємо на 1
        #     self.U1 += 1

        self.omega1 += 0.1
        self.omega2 += 0.1
        self.omega3 += 0.1
        self.omega4 += 0.1

    # Метод повороту в горизонтальній площині, метод control_D - ідентичний в іншому напрямку
    def control_A(self):
        # # Перевіряємо що градус повороту в межах 360 градусів
        if self.facing < 359:
            # Додаємо до градусу повороту 1
            self.facing += 1
        else:
            # Якщо поточний градус 359, то при додаванні одиниці отримаємо 0
            self.facing = 0

        # self.omega1 += 0.1
        # self.omega3 += 0.1

    def control_S(self):
        # if self.U1 >= -self.b:
            # Прискорюємо на 1
            # self.U1 -= 1
            # Викликаємо метод пересування
        if self.omega4 and self.omega3 and self.omega2 and self.omega1 > 0:
            self.omega1 -= 0.1
            self.omega2 -= 0.1
            self.omega3 -= 0.1
            self.omega4 -= 0.1

    def control_D(self):
        if self.facing > 0:
            self.facing -= 1
        else:
            self.facing = 359

        # self.omega2 += 0.1
        # self.omega4 += 0.1

    # Метод пересування вперед у горизонтальній площині, метод control_K - ідентичний в іншому напрямку
    def control_I(self):
        # Перевіряємо, що двигун не перевищує свою максимальну швидкість
        if self.theta < 359:
            # Додаємо до градусу повороту 1
            self.theta += 1
        else:
            # Якщо поточний градус 359, то при додаванні одиниці отримаємо 0
            self.theta = 0

        # if self.omega1 > 0:
        #     self.omega1 -= 0.1
        #     self.omega3 += 0.1

    # Метод пересування вліво у горизонтальній площині, метод control_L - ідентичний в іншому напрямку
    def control_J(self):
        # Перевіряємо, що двигун не перевищує свою максимальну швидкість
        if self.phi < 359:
            # Додаємо до градусу повороту 1
            self.phi += 1
        else:
            # Якщо поточний градус 359, то при додаванні одиниці отримаємо 0
            self.phi = 0

        # if self.omega2 > 0:
        #     self.omega4 += 0.1
        #     self.omega2 -= 0.1

    def control_K(self):
        if self.theta > 0:
            self.theta -= 1
        else:
            self.theta = 359

        # if self.omega3 > 0:
        #     self.omega1 += 0.1
        #     self.omega3 -= 0.1

    def control_L(self):
        if self.phi > 0:
            self.phi -= 1
        else:
            self.phi = 359

        # if self.omega4 > 0:
        #     self.omega4 -= 0.1
        #     self.omega2 += 0.1

    # Метод стабілізації положення, викликається при відсутності інших команд
    def stabilize(self):
        if 0 < self.phi < 180:
            self.phi -= 1
        elif 180 < self.phi < 360:
            self.phi += 1
        if 0 < self.theta < 180:
            self.theta -= 1
        elif 180 < self.theta < 360:
            self.theta += 1
        if self.theta == 360:
            self.theta = 0
        if self.phi == 360:
            self.phi = 0
        pass