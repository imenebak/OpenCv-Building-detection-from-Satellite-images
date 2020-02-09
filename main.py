from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from interface import *
import sys
from os.path import abspath, dirname
sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))



def main():
    
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()

    # setup ui
    ui = Ui_MainWindow()
    ui.setupUi(window)

    window.setWindowTitle("BATIMENT")
    window.setWindowIcon(QIcon('Icones/Bâti2.png'))

    if "--travis" in sys.argv:
        QtCore.QTimer.singleShot(2000, app.exit)

    # run
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
	
   
