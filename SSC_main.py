# Модуль, що містить основну описання логіки інтерфейсу та керування

import sys

from ui import SSC_about_ui
from ui import SSC_ui

from Data.worker import Worker
from Data.SSC_quadrotor import Quadrotor, Quadrotor2

from PyQt5.QtCore import Qt, QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from GLs.MainGL import MainGL
from GLs.MinimapGL import MinimapGL


# Клас вікна довідкової інформації
class SSCAbout(QMainWindow, SSC_about_ui.Ui_MainWindow):
    # Конструктор классу
    def __init__(self):
        # Створити класи-предки
        super().__init__()
        # Додати до класу поля інтерфейсу
        self.setupUi(self)


# Клас основного вікна
class SSCWindow(QMainWindow, SSC_ui.Ui_MainWindow):
    # Поля-флаги стану програми
    isPaused = False
    isMoveKeyPressed = False
    isKeyPressed = False
    # Поле зі списком натиснутих клавіш
    PressedKeyList = []

    # Конструктор классу
    def __init__(self):
        # Створити класи-предки
        super(SSCWindow, self).__init__()

        # Додати до класу поля інтерфейсу
        self.setupUi(self)

        # Створюємо екземпляр класу вікна довідкової інформації
        self.SSCAbout = SSCAbout()
        # Створюємо екземпляр класу квадрокоптера
        self.Quadrotor = Quadrotor2()

        # Поєндуємо елементи інтерфейсу, що визначають режим роботи програми з методом їх обробки
        self.FileFileMod.toggled.connect(self.setMode)
        self.KeybordDisplayMod.toggled.connect(self.setMode)

        # Встановлюємо режим за-замовчуванням
        self.KeybordDisplayMod.setChecked(True)

        # Ініціювання потоку обробки оновлення стану квадрокоптера
        # Створюємо екземпляр классу працівника потоку
        self.worker = Worker()
        # Сворюємо екземпляр классу потоку
        self.thread = QThread()

        # Поєднуємо сигнал від працівника з методами його обробки
        self.worker.intReady.connect(self.quadrotor_update)
        self.worker.intReady.connect(self.MainGL.update)
        self.worker.intReady.connect(self.MinimapGL.update)

        # Ставимо працівника на поток
        self.worker.moveToThread(self.thread)
        # По закінченю, прибираємо
        self.worker.finished.connect(self.thread.quit)
        # Поеднуємо сигнал початку роботи з методом працівника
        self.thread.started.connect(self.worker.procCounter)
        # Відкриваємо поток
        self.thread.start()

        # Встановлюємо початкові значення позиції квадрокоптера в інтерфейсі
        self.MaxDistanceLabel.setText(str(self.Quadrotor.maxDistance))
        self.XLabel.setText(format(self.Quadrotor.xPos, '.0f'))
        self.YLabel.setText(format(self.Quadrotor.yPos, '.0f'))
        self.ZLabel.setText(format(self.Quadrotor.zPos, '.0f'))
        self.CurrDistanceLabel.setText(format(self.Quadrotor.Distance, '.0f'))

        # Поеднуємо сигнал кнопки керування з методами його обробки
        self.ControlButton.clicked.connect(self.compute)
        self.ControlButton.clicked.connect(self.pause)

        # Поєднуємо сигнали меню з меодами їх обробки
        self.ResumeAction.triggered.connect(self.pause)
        self.RestartAction.triggered.connect(self.restart)
        self.Controls.triggered.connect(self.about)
        self.About.triggered.connect(self.about)

        # Плєнднуємо сигнал кнопки "Назад" в вікні довідкової інформації з методом його обробки
        self.SSCAbout.BackButton.clicked.connect(self.back)

        # Створюємо екземпляр классу графічного віджету основного вікна
        self.MainGL = MainGL(self.Quadrotor.maxDistance, self.Quadrotor.xPos, self.Quadrotor.yPos,
                             self.Quadrotor.zPos, parent=self.MainGL)
        # Встановлюємо його мінімальний розмір
        self.MainGL.setMinimumSize(815, 747)
        # Створюємо екземпляр классу графічного віджету мінімапи
        self.MinimapGL = MinimapGL(self.Quadrotor.maxDistance, self.Quadrotor.xPos,
                                   self.Quadrotor.zPos, parent=self.MinimapGL)
        # Встановлюємо його мінімальний розмір
        self.MinimapGL.setMinimumSize(200, 200)

    # Метод, що встановлює інтерфейс під поточний режим роботи програми
    def setMode(self):
        # Перевіряємо активний режим
        # Встановлюємо активніть елементів інтерфейсу та текст кнопки керування
        if self.KeybordDisplayMod.isChecked():
            self.ControlButton.setText("Пауза")
            self.ResumeAction.setEnabled(True)
            self.RestartAction.setEnabled(True)
            self.InfoBox.setEnabled(True)
            self.InputFilePath.setEnabled(False)
            self.OutputFilePath.setEnabled(False)
            self.ComputeAction.setEnabled(False)
        else:
            self.ControlButton.setText("Обрахувати")
            self.ResumeAction.setEnabled(False)
            self.RestartAction.setEnabled(False)
            self.InfoBox.setEnabled(False)
            self.InputFilePath.setEnabled(True)
            self.OutputFilePath.setEnabled(True)
            self.ComputeAction.setEnabled(True)

    # Метод обрахування пересування квадрокоптера в режимі файл-файл
    def compute(self):
        # Перевіряємо активність режиму файл-файл
        if self.FileFileMod.isChecked():
            try:
                # Робимо спробу відкрити файли, що вказав користувач
                inputFile = open(self.InputFilePath.text(), 'r')
                outputFile = open(self.OutputFilePath.text(), 'w')
            except OSError:
                # В разі помилки повідомляємо про неї
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Помилка читання файлів")
                msg.setInformativeText('Введіть коректні файли вводу та виводу')
                msg.setWindowTitle("Помилка")
                msg.exec_()
            else:
                # Якщо файли успішно відкрито, починаємо обрахунок
                outputFile.write("N\t\tt\t\t\tdX\t\tX\t\t\tY\t\t\tZ\n")
                # Зчитуємо інформацію та обробляємо інформацію з вхідного файла
                self.ProceedData(inputFile, outputFile)
                # Закриваємо файли
                inputFile.close()
                outputFile.close()

    # Метод зчитування інформації з вхідного файла, її обробки та запису
    def ProceedData(self, inputFile, outputFile):
        # Змінна, що містить номер поточної строки з командою
        numberOfCommand = 0
        # Змінна, що містить поточний момент часу
        currentTime = 0

        # Цикл обробки вхідного файлу
        for commandLine in inputFile:
            # Інкрементуємо номер строки
            numberOfCommand += 1
            # Ділимо стоку комади на слова
            commandLine.split(' ', 1)
            # Визначаємо команду руху
            moveCommand = commandLine.split(' ')[0]
            # Визначаємо час впродовж якого виконується такий рух
            time = int(commandLine.split(' ')[2])

            # Перевіряємо тип руху, всі типи оброблются ідентично
            if moveCommand == 'Up':
                # Цикл обробки команди руху впродовж часу цього руху
                for _ in range(time):
                    # Інкрементуємо таймер
                    currentTime += 1
                    # Пересуваємо квадрокоптер
                    self.Quadrotor.control_W()
                    # Записуємо поточний стан квадрокоптера у файл
                    self.writeData(outputFile, numberOfCommand, currentTime)
            elif moveCommand == 'Rotate_Left':
                for _ in range(time):
                    currentTime += 1
                    self.Quadrotor.control_A()
                    self.writeData(outputFile, numberOfCommand, currentTime)
            elif moveCommand == 'Rotate_Right':
                for _ in range(time):
                    currentTime += 1
                    self.Quadrotor.control_S()
                    self.writeData(outputFile, numberOfCommand, currentTime)
            elif moveCommand == 'Down':
                for _ in range(time):
                    currentTime += 1
                    self.Quadrotor.control_D()
                    self.writeData(outputFile, numberOfCommand, currentTime)
            elif moveCommand == 'Forward':
                for _ in range(time):
                    currentTime += 1
                    self.Quadrotor.control_I()
                    self.writeData(outputFile, numberOfCommand, currentTime)
            elif moveCommand == 'Left':
                for _ in range(time):
                    currentTime += 1
                    self.Quadrotor.control_J()
                    self.writeData(outputFile, numberOfCommand, currentTime)
            elif moveCommand == 'Back':
                for _ in range(time):
                    currentTime += 1
                    self.Quadrotor.control_K()
                    self.writeData(outputFile, numberOfCommand, currentTime)
            elif moveCommand == 'Right':
                for _ in range(time):
                    currentTime += 1
                    self.Quadrotor.control_L()
                    self.writeData(outputFile, numberOfCommand, currentTime)

    # Метод запису стану квадрокоптера у файл
    def writeData(self, outputFile, numberOfCommand, currentTime):
        outputFile.write("%-3d\t\t%-4d\t\t%-3d\t\t%-4.1f\t\t%-4.1f\t\t%-4.1f\n" %
                         (numberOfCommand, currentTime, self.Quadrotor.facing,
                          self.Quadrotor.xPos, self.Quadrotor.yPos, self.Quadrotor.zPos))

    # Метод, припиняє та продовжує симуляцію
    def pause(self):
        # Перевіряємо, що режим роботи Клавіатура-Дисплей
        if self.KeybordDisplayMod.isChecked():
            # Перевіряємо чи активна пауза
            if self.isPaused:
                # Якщо активна, то продовжуємо симуляцію
                self.CentralWidget.setEnabled(True)
                self.ResumeAction.setEnabled(False)
                self.RestartAction.setEnabled(False)
                self.isPaused = False
            else:
                # Якщо не активна, то припиняємо симуляцію
                self.isPaused = True
                self.CentralWidget.setEnabled(False)
                self.ResumeAction.setEnabled(True)
                self.RestartAction.setEnabled(True)

    # Метод перезапуску симуляції
    def restart(self):
        # Відчищаємо список натиснутих клавіш
        self.PressedKeyList = []
        # Створюємо новий екземпляр классу квадрокоптера
        self.Quadrotor = Quadrotor2()
        # Оновлюємо інформацію про квадрокоптер
        self.isMoveKeyPressed = True
        self.quadrotor_update()
        # Знімаємо паузу
        self.pause()

    # Метод повідомлення інформації про програму або про керування
    def about(self):
        # Визначаємо відправника повідомлення
        sender = self.sender()
        if sender.objectName() == "Controls":
            # Якщо, користувач потребує інформації про керування, виводимо її
            self.SSCAbout.TextLabel.setText("Керування квадрокоптером в режимі Клавіатура-Дисплей\n"
                                            "здійснюється за допомогою клавіш: "
                                            "W A S D та I J K L в латинській розкладці\n"
                                            "Призначення клавіш:\n"
                                            "W - Вверх\n"
                                            "S - Вниз\n"
                                            "A - Горизонтальний розворот вліво\n"
                                            "D - Горизонтальний розворот вправо\n"
                                            "I - Вперед\n"
                                            "K - Назад\n"
                                            "J - Вліво\n"
                                            "L - Вправо\n"
                                            "ESC - Пауза\n\n"
                                            "Керування в режимі Файл-Файл виконується через файл\n"
                                            "В файлі мають бути прописані команди "
                                            "в такому форматі: тип_руху for кількість_секунд_руху\n"
                                            "Список команд та приклад фалу вводу та виводу можна знайти в файлах\n"
                                            "inputExample.txt та outputExample.txt відповідно.")
        else:
            # Якщо, користувач потребує інформації про програму, виводимо її
            self.SSCAbout.TextLabel.setText("Курсова робота з дисципліни \"Системне програмне забезпечення\"\n"
                                            "Автори: студенти группи СП-325 Козлов Олексій і Балицька Ірина\n"
                                            "Тема курсової роботи: Симуляція польоту та керування квадрокоптера\n\n"
                                            "Опис інтерфейсу\n"
                                            "Перш за все потрібно обрати режим роботи програми \n"
                                            "(за замовченням це Клавіатура-Дисплей)\n"
                                            "Це робиться через радіо-кнопки з назвою режиму.\n\n"
                                            "Якщо ви обираєте режим Файл-Файл, потрібно ввести шлях до "
                                            "вхідного і вихідного файла у відповідних полях, \nпісля цого "
                                            "натисніть на кнопку \"Обрахувати\", якщо файли були вказані коректно, \n"
                                            "то ви отримаєте результат у вихідному файлі.\n\n"
                                            "Якщо ви обираєте режим Клавіатура-Дисплей, то "
                                            "основне вікно зліва - "
                                            "це вид на квадрокоптер.\n"
                                            "Панель справа - інформація про квадрокоптер.\n"
                                            "Міна-мапа відображає положення оператора (червона точка) "
                                            "з зоною дії сигнала керування (червоне коло)\n"
                                            "та положення квадрокоптера (синя точка).\n"
                                            "Інформіція про положення відображає координати, "
                                            "відхилення від х, відстань "
                                            "квадрокоптера від оператора \nта максимальну відстань.")
        # Ставимо на паузу
        self.pause()
        # Відображаємо вікно з довідковою інформацією
        self.SSCAbout.show()

    # Метод повернення назад з вікна з довідковою інформацією
    def back(self):
        # Знімаємо паузу
        self.pause()
        # Закриваємо вікно з довідковою інформацією
        self.SSCAbout.close()

    # Метод обробки сигналу натискання клавіші на клавіатурі
    def keyPressEvent(self, event):
        # Перевіряємо активність симуляції
        if not self.isPaused:
            # Клавіша натиснута
            self.isKeyPressed = True
            # Отримаємо код натиснутої клавіші
            PressedKey = event.key()
            # Додаємо код до списку натиснутих клавіш
            self.PressedKeyList.append(PressedKey)

    # Метод обробки відпускання клавіші на клавіатурі
    def keyReleaseEvent(self, event):
        # Перевіряємо активність симуляції
        if not self.isPaused and self.KeybordDisplayMod.isChecked():
            # Перевіряємо чи натиснута клавіша
            if self.isKeyPressed:
                # Обролюємо список клавіш
                self.processMultiKeys(self.PressedKeyList)
            # Клавіша відпущена
            self.isKeyPressed = False
            # Видаляємо останній елемент у списку
            del self.PressedKeyList[-1]

    # Метод обробки списку натиснутих клавіш
    def processMultiKeys(self, KeyList):
        # Перевіряємо чи натиснута кнопка ЕSC
        if Qt.Key_Escape in KeyList:
            # Ставимо на паузу
            self.pause()
        # Перевіряємо чи натиснута якась кнопка пересування, всі варіанти ідентичні, відрізняєтся тільки напрямок
        if Qt.Key_W in KeyList:
            # Викликаємо метод переміщення квадрокоптера
            self.Quadrotor.control_W()
            # Кнопка переміщення була натиснута
            self.isMoveKeyPressed = True
        if Qt.Key_A in KeyList:
            self.Quadrotor.control_A()
            self.isMoveKeyPressed = True
        if Qt.Key_S in KeyList:
            self.Quadrotor.control_S()
            self.isMoveKeyPressed = True
        if Qt.Key_D in KeyList:
            self.Quadrotor.control_D()
            self.isMoveKeyPressed = True
        if Qt.Key_I in KeyList:
            self.Quadrotor.control_I()
            self.isMoveKeyPressed = True
        if Qt.Key_J in KeyList:
            self.Quadrotor.control_J()
            self.isMoveKeyPressed = True
        if Qt.Key_K in KeyList:
            self.Quadrotor.control_K()
            self.isMoveKeyPressed = True
        if Qt.Key_L in KeyList:
            self.Quadrotor.control_L()
            self.isMoveKeyPressed = True

    # Метод оновлення стану квадрокоптера
    def quadrotor_update(self):
        if not self.isMoveKeyPressed:
            # Якщо не була натиснута клавіша керування, стабілізуємо квадрокоптер
            self.Quadrotor.stabilize()
        else:
            # Якщо була натиснута клавіша керування, оновлюємо інтерфейс
            self.isMoveKeyPressed = False

        self.Quadrotor.move()
        # Оновлюємо позицію на мінімапі та на основному віджеті
        self.MinimapGL.setPose(self.Quadrotor.xPos, self.Quadrotor.zPos)
        self.MainGL.setPose(self.Quadrotor.xPos, self.Quadrotor.yPos,
                            self.Quadrotor.zPos, self.Quadrotor.facing, self.Quadrotor.phi, self.Quadrotor.theta)

        # Оновлюємо текстову інформацію про положення
        self.DivitationXLabel.setText(format(self.Quadrotor.facing, '.0f'))
        self.XLabel.setText(format(self.Quadrotor.xPos, '.0f'))
        self.YLabel.setText(format(self.Quadrotor.yPos, '.0f'))
        self.ZLabel.setText(format(self.Quadrotor.zPos, '.0f'))
        self.CurrDistanceLabel.setText(format(self.Quadrotor.Distance, '.0f'))

            # Перевіряємо чи не перевищує поточна дистанція максимальну
        if self.Quadrotor.Distance > self.Quadrotor.maxDistance:
            self.restart()


if __name__ == "__main__":
    # Створюємо додаток
    app = QApplication(sys.argv)
    # Створюємо вікно
    SS = SSCWindow()
    # Відображаемо вікно
    SS.show()
    # В кінці закриваемо поток
    SS.thread.quit()
    # Закриваемо додаток
    sys.exit(app.exec_())
