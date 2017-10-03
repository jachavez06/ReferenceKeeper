#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QVBoxLayout,
                             QPushButton, QFileDialog)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    # Defaults for main app window
    def initUI(self):               

        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        
        # Add layout
        layout = QVBoxLayout()
        
        # Button
        self.button = QPushButton('Test', self)
        self.button.clicked.connect(self.close)
        layout.addWidget(self.button)
        
        # Open File Button
        self.ofile_button = QPushButton('Open', self)
        self.ofile_button.move(100,0)
        self.ofile_button.clicked.connect(self.openFileDialog)
        layout.addWidget(self.ofile_button)
        
        self.show()
    
    def openFileDialog(self):
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(
                self, 
                "QFileDialog.getOpenFileNames()",
                "",
                "All Files (*);;Python Files (*.py)", options = options)

def main():

    app = QApplication(sys.argv)
    main_window = MainWindow()
    app.exec_()


if __name__ == '__main__':
    main()
    
    
    # -----
    # Get filename using QFileDialog
    #filename = QFileDialog.getOpenFileName(w, 'Open File', '/')

    #if filename:
    #    print filename
        
        # print file contents
    #    with open(filename, 'r') as f:
    #        print(f.read())
    # -----

