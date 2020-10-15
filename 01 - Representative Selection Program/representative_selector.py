import sys
from PyQt5.QtWidgets import QApplication, QWidget

class RepresentativeSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_UI()

    def initialize_UI(self):
        self.setGeometry(500, 500, 400, 400)
        self.show()

program_endless_loop = QApplication(sys.argv)
exec_instance = RepresentativeSelector()
program_endless_loop.exec_()
