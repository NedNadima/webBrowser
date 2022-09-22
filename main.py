import sys
import os
import json

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit,
                             QTabBar, QFrame,
                             QStackedLayout, QTabWidget)

from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5.QtCore import *

class App(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Browser")
        self.setBaseSize(1366, 768)
        self.CreateApp()


    def CreateApp(self):
        self.layout = QVBoxLayout()

        self.tabbar = QTabBar()

        self.tabbar.addTab("Tab 1")
        self.tabbar.addTab("Tab 2")

        self.tabbar.setCurrentIndex(0)

        self.layout.addWidget(self.tabbar)
        self.setLayout(self.layout)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()

    sys.exit(app.exec_())