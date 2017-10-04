#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QVBoxLayout,
                             QPushButton, QFileDialog, QWidget, QInputDialog,
                             QLineEdit, QHBoxLayout, QDialog)
from PyQt5.QtCore import *

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):               
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Reference Keeper')
        self.show()        

class MainWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        
        okButton.clicked.connect(self.addReferenceDialog)
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)    
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')    
        self.show()

    def addReferenceDialog(self):
        d = QDialog()
        b1 = QPushButton("ok",d)
        b1.move(50,50)
        d.setWindowTitle("Dialog")
        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()
     
        
def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_widget = MainWidget()
    main_window.setCentralWidget(main_widget)
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

