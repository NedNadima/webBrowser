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

class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, e):
        self.selectAll()

class App(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Browser")
        self.CreateApp()
        self.setBaseSize(1366, 768)


    def CreateApp(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)

        #Create Tabs
        self.tabbar = QTabBar(movable=True, tabsClosable=True)
        self.tabbar.tabCloseRequested.connect(self.CloseTab)

        self.tabbar.addTab("Tab 1")
        self.tabbar.addTab("Tab 2")

        self.tabbar.setCurrentIndex(0)

        #Create AddressBar
        self.Toolbar = QWidget()
        self.ToolbarLayout = QHBoxLayout()
        self.addressbar = AddressBar()

        self.Toolbar.setLayout(self.ToolbarLayout)
        self.ToolbarLayout.addWidget(self.addressbar)

        self.layout.addWidget(self.tabbar)
        self.layout.addWidget(self.Toolbar)

        self.setLayout(self.layout)

        self.show()

    def CloseTab(self, i):
        self.tabbar.removeTab(i)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()

    sys.exit(app.exec_())