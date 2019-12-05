# Модуль містить працівника, потоку

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import time


# Клас працівника
class Worker(QObject):
    # Сигнали, що постачає працівник
    finished = pyqtSignal()
    intReady = pyqtSignal(int)

    # Метод генерування сигналу для обробки оновлення стану квадрокоптера
    @pyqtSlot(name="Quadrotor update")
    def procCounter(self):
        # Цикл роботи
        for _ in range(10000000000):
            # 30 разів на секунду
            time.sleep(1 / 30)
            # Посилаємо сигнал
            self.intReady.emit(_)
