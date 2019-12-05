# ������ ������ ����������, ������

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import time


# ���� ����������
class Worker(QObject):
    # �������, �� ������� ���������
    finished = pyqtSignal()
    intReady = pyqtSignal(int)

    # ����� ����������� ������� ��� ������� ��������� ����� �������������
    @pyqtSlot(name="Quadrotor update")
    def procCounter(self):
        # ���� ������
        for _ in range(10000000000):
            # 30 ���� �� �������
            time.sleep(1 / 30)
            # �������� ������
            self.intReady.emit(_)
