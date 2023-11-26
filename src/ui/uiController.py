import sys
from PyQt5.QtWidgets import *
import mapController

class UIController:
    class Window(QMainWindow):
        def __init__(self):
            super().__init__()
            self.initializeWindow()
        def initializeWindow(self):
            self.setGeometry(500, 500, 1000, 1000)
            self.setWindowTitle("Patient-Hospital")

        def changeLayout(self, layout):
            self.setLayout(layout)

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.app = QApplication(sys.argv)
        self.window = self.Window()
    
    def insertMap(self, window):
        mc = mapController.makeMap()
        
        win = QWidget()
        vbox = QVBoxLayout(win)
        vbox.addWidget(mc)
        self.window.changeLayout(vbox)

if __name__ == "__main__":
    ui = UIController(500, 500)
    ui.window.show()
    ui.app.exec_()