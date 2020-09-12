import random, unittest, requests, sys
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QKeySequence

class Win(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        shortcut = QShortcut(QKeySequence("Backspace+O"), self)
        shortcut.activated.connect(self.response)
        layout.addWidget(QLabel("Press Ctrl+O"))
        self.setLayout(layout)
    def response(self):
        print("Ctrl+O pressed")
app = QApplication(sys.argv)
window = Win()
window.show()
app.exec_()