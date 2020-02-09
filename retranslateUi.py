import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
from os.path import abspath, dirname
sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))


def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
        
    self.groupBox.setTitle(_translate("MainWindow", "Etapes de traitement"))
        
    self.toolBox_7.setItemText(self.toolBox_7.indexOf(self.Image_1), _translate("MainWindow", "Image 1"))
        
    self.dockWidget1.setWindowTitle(_translate("MainWindow", "&Encadrement"))

    self.pushButton7.setText(_translate("MainWindow", "Application de seuils"))
    
    self.pushButtonPoi.setText(_translate("MainWindow", "Detecter les coins"))

    self.pushButtonOpp.setText(_translate("MainWindow", "Application des opérations"))

    

