import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QCoreApplication
import random

class RepresentativeSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_UI()

    def initialize_UI(self):
        self.set_image()
        self.set_button()
        self.set_tooltip()
        self.set_number()

        self.setWindowTitle('Elect a representative!')
        self.setWindowIcon(QIcon('img/cat.png'))
        self.setGeometry(500, 500, 400, 400)
        self.show()

    def set_image(self):
        self.main_image = QLabel(self)
        self.main_image.setPixmap(QPixmap('img/cat.png').scaled(35, 44))
        self.main_image.move(100, 10)

    def set_button(self):
        pass

    def set_tooltip(self):
        pass

    def set_number(self):
        pass

program_endless_loop = QApplication(sys.argv)
exec_instance = RepresentativeSelector()
program_endless_loop.exec_()
