import sys
from retranslateUi import *
import subprocess
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from os.path import abspath, dirname
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from Traitement import HarrisCorner
from Traitement.seuils import seuil
from Traitement.OpMorphologique import morphologique
from Detection import templateMatch
from Detection import colorTrack as c
from Detection import siftDetect as sifty


sys.path.insert(0, abspath(dirname(abspath(__file__)) + '/..'))

class Ui_MainWindow(object):
    def openWindowSign(self):
        self.win = QtWidgets.QDialog()
        self.ui_1 = Ui_DialogSign()
        self.ui_1.SignUp(self.win)
        self.win.show()

    def Poi(self):
        HarrisCorner.Corner(self.imageUrl2)

    def Seuil(self):
        seuil(self.imageUrl)
        
    def OppMorpho(self):
        morphologique(self.imageUrl1)
        
    def montrer_etapes(self):
        self.pushButton8.setEnabled(True)
        self.pushButton9.setEnabled(False)
        lis = []
        i = 1
        if(os.path.isfile("Traitement\etapesTraitement.txt")):
            with open("Traitement\etapesTraitement.txt") as file :
                if (os.path.getsize("Traitement\etapesTraitement.txt") == 0):
                    self.text_Etapes_Traitements.setText("Lancer un traitement s'il vous plait !")
                if (os.path.getsize("Traitement\etapesTraitement.txt") != 0):
                    for line in file :
                        lis.append(str(line))
                k = (int(lis[0]))
                while(k > 0):
                    self.text_Etapes_Traitements.append((str(lis[i])))
                    i = i+1
                    k = k-1
        else:
            self.text_Etapes_Traitements.setText("Lancer un traitement s'il vous plait !")

    def cacher_etapes(self):
        self.pushButton9.setEnabled(True)
        self.pushButton8.setEnabled(False)
        self.text_Etapes_Traitements.setText("Etapes de traitements : ")

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self.ImageProcess, "Choisir Image", QDir.homePath(), 'Image (*.jpg *.png *.tiff *.jpeg)')
        if fileName != '':
            self.pushButton7.setEnabled(True)
            self.imageUrl = fileName
            image_traitement = QImage(fileName)
            image_affiche = QPixmap.fromImage(image_traitement.scaled(450,350,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
            self.label_seuil.setPixmap(image_affiche)

    def openFile1(self):
        fileName, _ = QFileDialog.getOpenFileName(self.ImageProcess, "Choisir Image", QDir.homePath(), 'Image (*.jpg *.png *.tiff)')
        if fileName != '':
            self.pushButtonOpp.setEnabled(True)
            self.imageUrl1 = fileName
            image_traitement = QImage(fileName)
            image_affiche = QPixmap.fromImage(image_traitement.scaled(450,350,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
            self.label_OppMorphologique.setPixmap(image_affiche)

    def openFile2(self):
        fileName, _ = QFileDialog.getOpenFileName(self.ImageProcess, "Choisir Image", QDir.homePath(), 'Image (*.jpg *.png *.tiff)')
        if fileName != '':
            self.pushButtonPoi.setEnabled(True)
            self.imageUrl2 = fileName
            image_traitement = QImage(fileName)
            image_affiche = QPixmap.fromImage(image_traitement.scaled(450,350,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
            self.label_Poi.setPixmap(image_affiche)
            
    def changephoto(self):
        if self.imgGl == "Images/Image4Espagne.png":
            self.imgGl = "Images/Image5.jpg"
            self.imgGl1 = "Images/Image51.png"
        else: 
            self.imgGl = "Images/Image4Espagne.png"
            self.imgGl1 = "Images/Image4Espagne1.png"

        self.image_2 = QImage(self.imgGl)
        self.image_2_affiche = QPixmap.fromImage(self.image_2.scaled(350,300,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
        self.label_fentereGl1.setPixmap(self.image_2_affiche)


    def changephoto1(self):
        if self.amg == "Images/Image7.jpg":
            self.amg = "Images/Image2.png"
        else: 
            self.amg = "Images/Image7.jpg"

        self.image_3 = QImage(self.amg)
        self.image_3_affiche = QPixmap.fromImage(self.image_3.scaled(350,300,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
        self.label_cl.setPixmap(self.image_3_affiche)
        

    def about(self):
        QMessageBox.about(None, "About BATIMENT",  "L'application de bureau <b>BATIMENT</b> est une application développée pour un projet de licence, propose des traitements d'images, un accés à des images satellitaires fournis par l'Agence"
                  " spatiale Algerienne, et permet la visualisation de resultats des algorithmes de detection de batiments implementés durant notre stage.")
       
    def aboutAsa(self):
         a = QMessageBox.about(None, "About ASAL",
        "L’Agence Spatiale Algérienne <b>ASAL</b> est un établissement public national à caractère spécifique, Elle a été créée auprès du chef du gouvernement par décret présidentiel n°02-48 du 16 janvier 2002"
        "Son objectif principal est de faire de l’outil spatial un vecteur performant de développement économique, social et culturel du pays et d’assurer la sécurité et le bien-être de la communauté nationale.")

    def fenetreGl(self):
        templateMatch.mainGl(self.imgGl, self.imgGl1)
    def couleurDetect(self):
        c.chocolathouses(self.amg)
        
    def SIFT(self):
        sifty.main()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setStyleSheet("QMainWindow{background-color:\n"
"\n"
"qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 245, 245, 255), stop:0.40 rgba(245, 245, 245, 255), stop:0.80 rgba(250, 250, 250, 255), stop:1 rgba(250, 255, 250, 255))}\n"
"\n"
"\n"
"QLabel#label_Heading{\n"
"font: 55 25pt \"Century Schoolbook L\";\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color:rgb(201, 217, 252);\n"
"}\n"
)

        
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        

        ###############################################################################################################"ACCUEIL
        self.Accueil = QtWidgets.QWidget()
        self.Accueil.setObjectName("Accueil")
        self.Accueil.setStyleSheet("QWidget{background-color:\n"
        "\n"
        "qlineargradient(spread:pad, x1:0.1, y1:0.4, x2:0.7, y2:0.35, stop:0 rgba(63, 81, 181,1.0), stop:0.60 rgba(159, 168, 218,1.0), stop:0.78 rgba(197, 202, 233,1.0), stop:1 rgba(232, 234, 246,1.0))}\n"
        "\n")

        self.icon1 = QIcon("Icones/Accueil.png")

        self.appli = QtWidgets.QVBoxLayout(self.Accueil)
        self.appli.setObjectName("appli")
        self.appli.setSpacing(30)
        self.appli.setContentsMargins(0, 0, 0, 0)

        self.image_appli = QImage("Icones/batim.png")
        self.image_appli_affiche = QPixmap.fromImage(self.image_appli.scaled(1100,190,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
        
        self.label_appli = QLabel(self.Accueil)
        self.label_appli.setObjectName("label_12")
        self.label_appli.setPixmap(self.image_appli_affiche)
        self.appli.addWidget(self.label_appli)

        self.addr = QLabel(self.Accueil)
        self.addr.setOpenExternalLinks(True);
        self.addr.setTextInteractionFlags(Qt.LinksAccessibleByMouse);
        self.addr.setText("<a href=\"http://www.asal.dz\" style=color:#00FF00 >ASAL</a>");
        self.addr.setStyleSheet("background-color: rgb(159, 168, 218,1.0); font: 5 10pt \"Century Schoolbook L\"; color:rgb(255,255,255)")
        self.addr.move(970,550)


        self.hello = QLabel(self.Accueil, text="<b>Agence Spatiale</b>")
        self.hello.setStyleSheet("background-color: rgb(159, 168, 218,1.0); font: 5 8pt \"Century Schoolbook L\"; color: rgb(0,0,0)")
        self.hello.move(850,450)
        self.hello2 = QLabel(self.Accueil, text="<b>Algérienne,</b>")
        self.hello2.setStyleSheet("background-color: rgb(159, 168, 218,1.0); font: 5 8pt \"Century Schoolbook L\"; color: rgb(0,0,0)")
        self.hello2.move(945,450)
        self.hello3 = QLabel(self.Accueil, text="<b>14 Rue Omar</b>")
        self.hello3.setStyleSheet("background-color: rgb(159, 168, 218,1.0); font: 5 8pt \"Century Schoolbook L\"; color: rgb(0,0,0)")
        self.hello3.move(850,470)
        self.hello4 = QLabel(self.Accueil, text="<b>AISSAOUI EL </b>")
        self.hello4.setStyleSheet("background-color: rgb(159, 168, 218,1.0); font: 5 8pt \"Century Schoolbook L\"; color: rgb(0,0,0)")
        self.hello4.move(928,470)
        self.hello5 = QLabel(self.Accueil, text="<b>HAMMADIA,</b>")
        self.hello5.setStyleSheet("background-color: rgb(159, 168, 218,1.0); font: 5 8pt \"Century Schoolbook L\"; color: rgb(0,0,0)")
        self.hello5.move(1005,470)
        self.hello6 = QLabel(self.Accueil, text="<b>BOUZAREAH ALGE</b>")
        self.hello6.setStyleSheet("background-color: rgb(159, 168, 218,1.0); font: 5 8pt \"Century Schoolbook L\"; color: rgb(0,0,0)")
        self.hello6.move(850,490)
        self.hello7 = QLabel(self.Accueil, text="<b>R ALGERIE</b>")
        self.hello7.setStyleSheet("background-color: rgb(159, 168, 218,1.0); font: 5 8pt \"Century Schoolbook L\"; color: rgb(0,0,0)")
        self.hello7.move(950,490)
        self.hello8 = QLabel(self.Accueil, text="<b>TEL:</b> + 213 23 27 05")
        self.hello8.setStyleSheet("background-color: rgb(159, 168, 218,1.0); font: 5 8pt \"Century Schoolbook L\"; color: rgb(0,0,0)")
        self.hello8.move(850,510)
        self.hello9 = QLabel(self.Accueil, text=" 31")
        self.hello9.setStyleSheet("background-color: rgb(159, 168, 218,1.0); font: 5 8pt \"Century Schoolbook L\"; color: rgb(0,0,0)")
        self.hello9.move(950,510)
        


        #label.show();
        #self.appli.addWidget( self.addr)
        
    
        
        self.tabWidget.addTab(self.Accueil,self.icon1, "Accueil")
        ################################################################################################################"" BASE D'IMAGES
        self.Galerie = QtWidgets.QWidget()
        self.Galerie.setObjectName("Galerie")

        self.gridLayout_Galerie = QtWidgets.QGridLayout(self.Galerie)
        self.gridLayout_Galerie.setObjectName("gridLayout_7")

        self.groupBox_7 = QtWidgets.QGroupBox(self.Galerie)
        self.groupBox_7.setObjectName("groupBox_7")
        
        self.icon2 = QIcon("Icones/galerie.png")

        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        

        self.toolBox_7 = QtWidgets.QToolBox(self.groupBox_7)
        self.toolBox_7.setObjectName("toolBox_7")
        
#/////////////////////////////////////////////////////////////////////////////////IMAGE 1 //////////////////////////////////////////////////
        self.Image_1 = QtWidgets.QWidget()
        self.Image_1.setGeometry(QtCore.QRect(0, 0, 100, 242))
        self.Image_1.setObjectName("Image_1")
        self.toolBox_7.addItem(self.Image_1, "")

        self.gridLayout_Img_1 = QtWidgets.QGridLayout(self.Image_1)
        self.gridLayout_Img_1.setObjectName("gridLayout_Img_1")
        self.gridLayout_Img_1.setSpacing(30)
        self.gridLayout_Img_1.setContentsMargins(50, 4, 54, 4)

        
        self.image_1 = QImage("Images/Image4Espagne.png")
        #self.image_1_affiche = self.image_1.scaled(QSize(450,350))
        self.image_1_affiche = QPixmap.fromImage(self.image_1.scaled(450,350,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
        
        self.label_1 = QLabel()
        self.label_1.setObjectName("label_1")
        self.label_1.setPixmap(self.image_1_affiche)
        self.gridLayout_Img_1.addWidget(self.label_1,0, 0, 5, 1)


        self.label_image1 = QLabel(text="<h2 style = color:blue;>Zone Semi-urbaine 1</h2><br></br><p>Cette Image a été prise en Salamanque, au nord-ouest de l'Espagne. Montre une trentaine d'immeubles d'une meme résidance.</p>")

        self.gridLayout_Img_1.addWidget(self.label_image1, 1, 1, 1, 1)
        self.label1_image1 = QLabel(text="<i>Image prise : En 2018 , satellite : Google , taille : 744*718 </i>")

        self.gridLayout_Img_1.addWidget(self.label1_image1, 2, 1, 1, 1)
#//////////////////////////////////////////////////////////////////////////IMAGE 2////////////////////////////////////////////////////////
        self.Image_4 = QtWidgets.QWidget()
        self.Image_4.setGeometry(QtCore.QRect(0, 0, 100, 242))
        self.Image_4.setObjectName("Image_4")
        self.toolBox_7.addItem(self.Image_4, "Image 2")

        self.gridLayout_Img_4 = QtWidgets.QGridLayout(self.Image_4)
        self.gridLayout_Img_4.setObjectName("gridLayout_Img_4")
        self.gridLayout_Img_4.setSpacing(30)
        self.gridLayout_Img_4.setContentsMargins(50, 4, 54, 4)

        self.image_44 = QImage("Images/Image2.png")
        self.image_4_affiche = QPixmap.fromImage(self.image_44.scaled(450,350,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
        
        self.label_4 = QLabel()
        self.label_4.setObjectName("label_4")
        self.label_4.setPixmap(self.image_4_affiche)
        self.gridLayout_Img_4.addWidget(self.label_4,0, 0, 5, 1)

        self.label_image4 = QLabel(text="<h2 style = color:blue;>Zone Semi-urbaine 2</h2><br></br><p>Cette Image a été prise en Salamanque, au nord-ouest de l'Espagne. Montre une école.</p>")

        self.gridLayout_Img_4.addWidget(self.label_image4, 1, 1, 1, 1)
        self.label1_image4 = QLabel(text="<i>Image prise : En 2016 , satellite : Google , taille :685*347 </i>")

        self.gridLayout_Img_4.addWidget(self.label1_image4, 2, 1, 1, 1)
#/////////////////////////////////////////////////////////////////////////////////////IMAGE 3////////////////////////////////////////////////////
        self.Image_5 = QtWidgets.QWidget()
        self.Image_5.setGeometry(QtCore.QRect(0, 0, 100, 242))
        self.Image_5.setObjectName("Image_5")
        self.toolBox_7.addItem(self.Image_5, "Image 3")

        self.gridLayout_Img_5 = QtWidgets.QGridLayout(self.Image_5)
        self.gridLayout_Img_5.setObjectName("gridLayout_Img_5")
        self.gridLayout_Img_5.setSpacing(30)
        self.gridLayout_Img_5.setContentsMargins(50, 4, 54, 4)

        self.image_55 = QImage("Images/im6.png")
        self.image_5_affiche = QPixmap.fromImage(self.image_55.scaled(450,350,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
        
        self.label_5 = QLabel()
        self.label_5.setObjectName("label_5")
        self.label_5.setPixmap(self.image_5_affiche)
        self.gridLayout_Img_5.addWidget(self.label_5,0, 0, 5, 1)

        self.label_image5 = QLabel(text="<h2 style = color:blue;>Zone Urbaine 1</h2><br></br><p>Cette Image a été prise en Valencia, sur l'est d'Espagne. Montre des immeubles.</p>")

        self.gridLayout_Img_5.addWidget(self.label_image5, 1, 1, 1, 1)
        self.label1_image5 = QLabel(text="<i>Image prise : En 2016 , satellite : Google , taille : 645*478 </i>")

        self.gridLayout_Img_5.addWidget(self.label1_image5, 2, 1, 1, 1)
    #//////////////////////////////////////////////////////////////////////////////IMAGE 4//////////////////////////////////////////////////////

        self.Image_2 = QtWidgets.QWidget()
        self.Image_2.setGeometry(QtCore.QRect(0, 0, 100, 242))
        self.Image_2.setMinimumSize(QtCore.QSize(720, 300))
        self.Image_2.setObjectName("Image_2")
        self.toolBox_7.addItem(self.Image_2, "Image 4")

        self.gridLayout_Img_2 = QtWidgets.QGridLayout(self.Image_2)
        self.gridLayout_Img_2.setObjectName("gridLayout_Img_2")
        self.gridLayout_Img_2.setSpacing(30)
        self.gridLayout_Img_2.setContentsMargins(50, 4, 54, 4)

        self.image_22 = QImage("Images/Image7.jpg")
        self.image_2_affiche = QPixmap.fromImage(self.image_22.scaled(450,350,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
        
        self.label_2 = QLabel()
        self.label_2.setObjectName("label_2")
        self.label_2.setPixmap(self.image_2_affiche)
        self.gridLayout_Img_2.addWidget(self.label_2,0, 0, 5, 1)
        
        self.label_image2 = QLabel(text="<h2 style = color:blue;>Zone Urbaine 2</h2><br></br><p>Cette Image a été prise en Valencia, sur l'est d'Espagne. Montre plus d'une centaine d'immeubles d'une meme résidance. </p>")


        self.gridLayout_Img_2.addWidget(self.label_image2, 1, 1, 1, 1)
        self.label1_image2 = QLabel(text="<i>Image prise : En 2016 , satellite : Google, taille : 884*616</i>")

        self.gridLayout_Img_2.addWidget(self.label1_image2, 2, 1, 1, 1)
#///////////////////////////////////////////////////////////////////////IMAGE 5////////////////////////////////////////////////////////
        self.Image_3 = QtWidgets.QWidget()
        self.Image_3.setGeometry(QtCore.QRect(0, 0, 100, 242))
        self.Image_3.setObjectName("Image_3")
        self.toolBox_7.addItem(self.Image_3, "Image 5")

        self.gridLayout_Img_3 = QtWidgets.QGridLayout(self.Image_3)
        self.gridLayout_Img_3.setObjectName("gridLayout_Img_3")
        self.gridLayout_Img_3.setSpacing(30)
        self.gridLayout_Img_3.setContentsMargins(50, 4, 54, 4)

        self.image_33 = QImage("Images/Image5.jpg")
        self.image_3_affiche = QPixmap.fromImage(self.image_33.scaled(450,350,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
        
        self.label_3 = QLabel()
        self.label_3.setObjectName("label_3")
        self.label_3.setPixmap(self.image_3_affiche)
        self.gridLayout_Img_3.addWidget(self.label_3,0, 0, 5, 1)

        self.label_image3 = QLabel(text="<h2 style = color:blue;>Zone Urbaine 3</h2><br></br><p>Cette Image a été prise en Valencia, sur l'est d'Espagne. Montre un hopitale.</p>")

        self.gridLayout_Img_3.addWidget(self.label_image3, 1, 1, 1, 1)
        self.label1_image3 = QLabel(text="<i>Image prise : En 2016 , satellite : , taille : </i>")

        self.gridLayout_Img_3.addWidget(self.label1_image3, 2, 1, 1, 1)


#*************************************************************************************************************************************#        
        self.verticalLayout_7.addWidget(self.toolBox_7)
        self.gridLayout_Galerie.addWidget(self.groupBox_7, 1, 0, 1, 1)

        self.tabWidget.addTab(self.Galerie,self.icon2, "Galerie")
##############################################################################################"""TRAITEMENTS IMAGE"""###################
        self.ImageProcess = QtWidgets.QWidget()
        self.ImageProcess.setObjectName("ImageProcess")

        self.imageUrl = ''
        self.imageUrl1 = ''
        self.imageUrl2 = ''
        self.gridLayout_ImageProcess = QtWidgets.QGridLayout(self.ImageProcess)
        self.gridLayout_ImageProcess.setObjectName("gridLayout_ImageProcess")

        self.icon3 = QIcon("Icones/traitement.png")

        self.groupBox_ImageProcess = QtWidgets.QGroupBox(self.ImageProcess)
        self.groupBox_ImageProcess.setObjectName("groupBox_ImageProcess")

        self.tabWidget_ImageProcess = QtWidgets.QTabWidget(self.ImageProcess)
        self.tabWidget_ImageProcess.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_ImageProcess.TabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_ImageProcess.setMovable(True)
        self.tabWidget_ImageProcess.setUsesScrollButtons(True)

        self.tabWidget_ImageProcess.setObjectName("tableWidget_ImageProcess")
        #***********************************SEUILLAGE*********************************************#
        self.tab_seuil = QtWidgets.QWidget()
        self.tab_seuil.setObjectName("tab_seuil")

        self.gridLayout_seuil = QtWidgets.QGridLayout(self.tab_seuil)
        
        self.pushButton7 = QtWidgets.QPushButton(self.tab_seuil)
        self.pushButton7.setObjectName("pushButton7")
        self.pushButton7.setEnabled(False)
        self.pushButton7.clicked.connect(self.Seuil)

        self.label_seuil = QLabel("<h2 style = color:gray;>Choisissez une Image</h2>")
        self.label_seuil.setObjectName("label_seuil")

        self.label_seuil1 = QLabel("Image :")
        self.label_seuil1.setObjectName("seuil_1")

        self.openButton = QtWidgets.QPushButton("ouvrir...")
        
        self.openButton.clicked.connect(self.openFile)
        
        self.gridLayout_seuil.addWidget(self.label_seuil1, 0, 0, 1, 1)
        self.gridLayout_seuil.addWidget(self.label_seuil, 1, 1, 5, 4)
        self.gridLayout_seuil.addWidget(self.pushButton7, 6, 5, 1,1)
        self.gridLayout_seuil.addWidget(self.openButton, 5, 5, 1,1)
       
        #self.gridLayout_Contour.addWidget(self.pushButton7, 0, 0, 1, 1)

        self.tabWidget_ImageProcess.addTab(self.tab_seuil,"Application de seuillage")
        #******************************OPP MORPHOLOGIQUE****************************************#

        self.tab_OppMorphologique = QtWidgets.QWidget()
        self.tab_OppMorphologique.setObjectName("tab_OppMorphologique")
        
        self.gridLayout_OppMorphologique = QtWidgets.QGridLayout(self.tab_OppMorphologique)
        
        self.pushButtonOpp = QtWidgets.QPushButton(self.tab_OppMorphologique)
        self.pushButtonOpp.setObjectName("pushButtonOpp")
        self.pushButtonOpp.setEnabled(False)
        self.pushButtonOpp.clicked.connect(self.OppMorpho)

        self.label_OppMorphologique = QLabel("<h2 style = color:gray;>Choisissez une Image</h2>")
        self.label_OppMorphologique.setObjectName("label_OppMorphologique")

        self.label_OppMorphologique1 = QLabel("Image :")
        self.label_OppMorphologique1.setObjectName("label_OppMorphologique1")

        self.openButton1 = QtWidgets.QPushButton("ouvrir...")
        
        self.openButton1.clicked.connect(self.openFile1)
        
        self.gridLayout_OppMorphologique.addWidget(self.label_OppMorphologique1, 0, 0, 1, 1)
        self.gridLayout_OppMorphologique.addWidget(self.label_OppMorphologique, 1, 1, 5, 4)
        self.gridLayout_OppMorphologique.addWidget(self.pushButtonOpp, 6, 5, 1,1)
        self.gridLayout_OppMorphologique.addWidget(self.openButton1, 5, 5, 1,1)

        self.tabWidget_ImageProcess.addTab(self.tab_OppMorphologique, "Application d'opération Morphologique")
        #*******************************POI****************************************************#

        self.tab_POI = QtWidgets.QWidget()
        self.tab_POI.setObjectName("tab_POI")

        self.gridLayout_Poi = QtWidgets.QGridLayout(self.tab_POI)
        
        self.pushButtonPoi = QtWidgets.QPushButton(self.tab_OppMorphologique)
        self.pushButtonPoi.setObjectName("pushButtonOpp")
        self.pushButtonPoi.setEnabled(False)
        self.pushButtonPoi.clicked.connect(self.Poi)

        self.label_Poi = QLabel("<h2 style = color:gray;>Choisissez une Image</h2>")
        self.label_Poi.setObjectName("label_Poi")

        self.label_Poi1 = QLabel("Image :")
        self.label_Poi1.setObjectName("label_Poi1")

        self.openButton2 = QtWidgets.QPushButton("ouvrir...")
        self.openButton2.clicked.connect(self.openFile2)
        
        self.gridLayout_Poi.addWidget(self.label_Poi1, 0, 0, 1, 1)
        self.gridLayout_Poi.addWidget(self.label_Poi, 1, 1, 5, 4)
        self.gridLayout_Poi.addWidget(self.pushButtonPoi, 6, 5, 1,1)
        self.gridLayout_Poi.addWidget(self.openButton2, 5, 5, 1,1)

        self.tabWidget_ImageProcess.addTab(self.tab_POI, "Detection de points d'interets")

        
        self.gridLayout_ImageProcess.addWidget(self.tabWidget_ImageProcess, 0, 0, 1, 1)
        self.tabWidget.addTab(self.ImageProcess, self.icon3, "Traitements")
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''T A B L E A U D E S E T A P E S'''''''''''''''''''''''''''''''''''''''''''''#
        self.verticalLayout_Traitement = QtWidgets.QVBoxLayout(self.groupBox_ImageProcess)
        self.verticalLayout_Traitement.setObjectName("verticalLayout_Traitement")
        
        self.Etapes_Traitement = QtWidgets.QWidget()
        self.Etapes_Traitement.setGeometry(QtCore.QRect(0, 0, 500, 242))
        self.Etapes_Traitement.setMinimumSize(QtCore.QSize(420, 200))
        self.Etapes_Traitement.setObjectName("Etapes_Traitement")

        self.gridLayout_Etapes_Traitement = QtWidgets.QGridLayout(self.Etapes_Traitement)
        self.gridLayout_Etapes_Traitement.setObjectName("gridLayout_Etapes_Traitement")

        self.text_Etapes_Traitements = QtWidgets.QTextEdit(self.Etapes_Traitement)
        self.text_Etapes_Traitements.setReadOnly(True) 
        self.text_Etapes_Traitements.setObjectName("text_Etapes_Traitements")
        self.text_Etapes_Traitements.setText("Etapes de traitements : ")


        self.lay_Etapes_traitement = QHBoxLayout()
        self.lay_Etapes_traitement.setObjectName("lay_Etapes_traitement")

        self.pushButton8 = QtWidgets.QPushButton("Caché les étapes")
        self.pushButton8.isDefault()
        self.pushButton8.setObjectName("pushButton8")
        #self.pushButton8.setPosition("left")
        self.pushButton8.clicked.connect(self.cacher_etapes)

        self.pushButton9 = QtWidgets.QPushButton("Montrer les étapes")
        self.pushButton9.setObjectName("pushButton9")
        self.pushButton9.clicked.connect(self.montrer_etapes)

        '''self.lay_Etapes_traitement.addWidget(self.pushButton8,1)
        self.lay_Etapes_traitement.addWidget(self.pushButton9,2)'''

        self.gridLayout_Etapes_Traitement.addWidget(self.text_Etapes_Traitements, 0, 0, 4, 5)

        self.gridLayout_Etapes_Traitement.addWidget(self.pushButton8, 4, 4, 1, 1)
        self.gridLayout_Etapes_Traitement.addWidget(self.pushButton9, 4, 3, 1, 1)
        
        self.verticalLayout_Traitement.addWidget(self.Etapes_Traitement)
        self.gridLayout_ImageProcess.addWidget(self.groupBox_ImageProcess, 2, 0, 1, 1)

      
        ################################################################"""""   DETECTION     #######################################"""""""""""

        self.Detection = QtWidgets.QWidget()
        self.Detection.setObjectName("Detection")

        self.gridLayout_Detection = QtWidgets.QGridLayout(self.Detection)
        self.gridLayout_Detection.setObjectName("gridLayout_Detection")

        self.icon4 = QIcon("Icones/Detection.png")

        self.tabWidget_Detection = QtWidgets.QTabWidget(self.Detection)
        self.tabWidget_Detection.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_Detection.TabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_Detection.setMovable(True)
        self.tabWidget_Detection.setUsesScrollButtons(True)

        self.tabWidget_Detection.setObjectName("tableWidget_Detection")

####################################################################"METHODE ONE #######################################
        self.tab_fentereGl = QtWidgets.QWidget()
        self.tab_fentereGl.setObjectName("tab_fentereGl")

        self.gridLayout_fentereGl = QtWidgets.QGridLayout(self.tab_fentereGl)
        self.gridLayout_fentereGl.setContentsMargins(20, 0, 20, 0)
        

        self.imgGl = "Images/Image4Espagne.png"
        self.imgGl1 = "Images/Image4Espagne1.png"
        
        self.image_2 = QImage(self.imgGl)
        self.image_2_affiche = QPixmap.fromImage(self.image_2.scaled(350,300,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
        self.label_fentereGl1 = QLabel()
        self.label_fentereGl1.setObjectName("label_fentereGl")
        self.label_fentereGl1.setPixmap(self.image_2_affiche)

        self.pushButton99 = QtWidgets.QPushButton("Lancer la detection")
        self.pushButton99.setObjectName("pushButton7")
        self.pushButton99.resize(200,80)
        #self.pushButton9.setEnabled(False)
        self.pushButton99.clicked.connect(self.fenetreGl)

        self.label_fentereGl = QLabel("<h3>Image :</h3>")
        self.label_fentereGl.setObjectName("fentereGlimg")

        self.label_imageGl = QTextEdit()
        self.label_imageGl.setReadOnly(True) 
        self.label_imageGl.setText("<h1 style = color:blue;>A propos de la méthode</h1><p><br>Tmplate matching est l'une des méthode"
                                   " assez basique de la reconnaissance d'objet.L'idée ici est de trouver des régions identiques d'une image"
                                   " qui correspondent à un modèle que nous fournissons, en donnant un certain seuil.<br><br></br><i>Pour des "
                                   "correspondances d'objet exactes, avec un éclairage / une échelle / un angle précis,<br></br> cela peut fonctionner"
                                   " très bien.</i></p>")
        
        self.change = QtWidgets.QPushButton("Changer Image>>",self.tab_fentereGl)
        self.change.resize(110,35)
        self.change.setToolTip('Image suivante')
        self.change.clicked.connect(self.changephoto)
        
        self.gridLayout_fentereGl.addWidget(self.label_fentereGl, 0, 0, 1, 1)
        self.gridLayout_fentereGl.addWidget(self.label_fentereGl1, 0, 1, 9, 12)
        self.gridLayout_fentereGl.addWidget(self.pushButton99, 5, 12, 1 ,3)
        self.gridLayout_fentereGl.addWidget(self.change, 4, 0, 1,1)
        self.gridLayout_fentereGl.addWidget(self.label_imageGl, 3, 10, 2 ,7)

        
        
        self.tabWidget_Detection.addTab(self.tab_fentereGl,"Detection des immeubles qui se ressemble")

###################################################################### DETECTION DE COULEURS ########################################################
        self.tab_colors = QtWidgets.QWidget()
        self.tab_colors.setObjectName("tab_colors")

        self.gridLayout_colors = QtWidgets.QGridLayout(self.tab_colors)
        self.gridLayout_colors.setContentsMargins(20, 0, 20, 0)
        
        self.pushButton0 = QtWidgets.QPushButton("Lancer la detection")
        self.pushButton0.setObjectName("pushButton0")
        self.pushButton0.resize(200,80)
        #self.pushButton9.setEnabled(False)
        self.pushButton0.clicked.connect(self.couleurDetect)

        self.amg = "Images/Image7.jpg"
        
        self.image_3 = QImage(self.amg)
        self.image_3_affiche = QPixmap.fromImage(self.image_3.scaled(350,300,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
        self.label_cl = QLabel()
        self.label_cl.setObjectName("label_fentereGl")
        self.label_cl.setPixmap(self.image_3_affiche)

        
        self.label_colors = QLabel("<h3>Image :</h3>")
        self.label_colors.setObjectName("colors")

        self.label_colors1 = QTextEdit()
        self.label_colors1.setReadOnly(True) 
        self.label_colors1.setText("<h1 style = color:blue;>A propos de la méthode</h1><p><br>La détection d'objets basée sur la couleur est l'une des méthodes"
                                   " les plus rapides et les plus faciles pour trouver un objet ou une forme dans une image."
                                   "<br><br></br><i> La rapidité de cette technique la rend très attrayante pour plusieurs applications"
                                   " mais en raison de sa simplicité, de nombreux problèmes peuvent être causer.</i></p>")

        #self.label_imageGl = QLabel(text="<h2 style = color:blue;>A propos de la méthode</h2><br></br><p>Une des méthode assez basique de la reconnaissance d'objet.<br></br> L'idée ici est de trouver des régions identiques d'une image<br></br> qui correspondent à un modèle que nous fournissons,<br></br> en donnant un certain seuil.<br></br><i>Pour des correspondances d'objet exactes, avec un éclairage / une échelle / un angle précis,<br></br> cela peut fonctionner très bien.</i></p>")
        
        self.changecolors = QtWidgets.QPushButton("Changer Image>>",self.tab_colors)
        self.changecolors.resize(110,35)
        self.changecolors.setToolTip('Image suivante')
        #self.change.setStyleSheet("background-color: rgb(201, 217, 252);")
        self.changecolors.clicked.connect(self.changephoto1)
        
        self.gridLayout_colors.addWidget(self.label_colors, 0, 0, 1, 1)
        self.gridLayout_colors.addWidget(self.label_cl, 0, 1, 9, 12)
        self.gridLayout_colors.addWidget(self.pushButton0, 5, 12, 1 ,3)
        self.gridLayout_colors.addWidget(self.changecolors, 4, 0, 1,1)
        self.gridLayout_colors.addWidget(self.label_colors1, 3, 10, 2 ,7)

        
        
        self.tabWidget_Detection.addTab(self.tab_colors,"Detection des toits")
########################################################################################  SIFT ********************************************************
        self.tab_sift = QtWidgets.QWidget()
        self.tab_sift.setObjectName("tab_sift")

        self.gridLayout_sift = QtWidgets.QGridLayout(self.tab_sift)
        self.gridLayout_sift.setContentsMargins(20, 0, 20, 0)
        
        self.pushButtons = QtWidgets.QPushButton("Lancer la detection")
        self.pushButtons.setObjectName("pushButtons")
        self.pushButtons.resize(200,80)
        #self.pushButton9.setEnabled(False)
        self.pushButtons.clicked.connect(self.SIFT)

        self.sif = "Images/Image7.png"
        
        self.image_s = QImage(self.sif)
        self.image_s_affiche = QPixmap.fromImage(self.image_s.scaled(350,300,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
        self.label_s = QLabel()
        self.label_s.setObjectName("label_fenteres")
        self.label_s.setPixmap(self.image_s_affiche)

        
        self.label_si = QLabel("<h3>Images :</h3>")
        self.label_si.setObjectName("siftImg")

        self.label_sift = QTextEdit()
        self.label_sift.setReadOnly(True) 
        self.label_sift.setText("<h1 style = color:blue;>A propos de la méthode</h1><p><br>La détection d'objets utilisant l'algorithme"
                                "«transformation de caractéristiques visuelles invariante à l'échelle » (SIFT)"
                                 " , est utilisé dans le domaine de la vision par ordinateur pour détecter et identifier les éléments similaires entre différentes images numériques."
                                   "<br><br></br><i> Les applications de la méthode sont nombreuses et ne cessent de s'étendre;"
                                   " elles couvre plusieurs domaines tels que la détection d'objet, la cartographie et la navigation,"
                                "l'assemblage de photos, la modélisation 3D, la recherche d'image par le contenu, le tracking video ou le match moving .</i></p>")


        #self.label_imageGl = QLabel(text="<h2 style = color:blue;>A propos de la méthode</h2><br></br><p>Une des méthode assez basique de la reconnaissance d'objet.<br></br> L'idée ici est de trouver des régions identiques d'une image<br></br> qui correspondent à un modèle que nous fournissons,<br></br> en donnant un certain seuil.<br></br><i>Pour des correspondances d'objet exactes, avec un éclairage / une échelle / un angle précis,<br></br> cela peut fonctionner très bien.</i></p>")
        
        
        
        self.gridLayout_sift.addWidget(self.label_si, 0, 0, 1, 1)
        self.gridLayout_sift.addWidget(self.label_s, 0, 1, 9, 12)
        self.gridLayout_sift.addWidget(self.pushButtons, 5, 12, 1 ,3)
        self.gridLayout_sift.addWidget(self.label_sift, 3, 10, 2 ,7)

        
        
        self.tabWidget_Detection.addTab(self.tab_sift,"Utilisation de descripteur")        
        self.gridLayout_Detection.addWidget(self.tabWidget_Detection, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Detection, self.icon4, "Detection de Batiment")

########################################################################################################
           
        self.verticalLayout_5.addWidget(self.tabWidget)   
        MainWindow.setCentralWidget(self.centralwidget)
        
     
########################################################################################################Dockwidget
        
        self.dockWidget1 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget1.setObjectName("dockWidget1")
        self.dockWidget1.setLayoutDirection(0)
        
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.image_A = QImage("Icones/alg1.png")
        self.image_A_affiche = QPixmap.fromImage(self.image_A.scaled(100,100,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
        
        self.label_A = QLabel()
        self.label_A.setObjectName("label_A")
        self.label_A.setPixmap(self.image_A_affiche)
        self.verticalLayout.addWidget(self.label_A)

        
        self.line = QtWidgets.QFrame(self.dockWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)

        self.image_B = QImage("Icones/logo asal -0.png")
        self.image_B_affiche = QPixmap.fromImage(self.image_B.scaled(90,90,Qt.IgnoreAspectRatio,Qt.SmoothTransformation))
        
        self.label_B = QLabel()
        self.label_B.setObjectName("label_A")
        self.label_B.setPixmap(self.image_B_affiche)
        self.verticalLayout.addWidget(self.label_B)
        
        self.verticalLayout_2.addLayout(self.verticalLayout)
        
        '''self.frame = QtWidgets.QFrame(self.dockWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(120, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.verticalLayout_2.addWidget(self.frame)'''
        
        self.dockWidget1.setWidget(self.dockWidgetContents)
    
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget1)
######################################################################################################"" MENU


        self.fileMenu = MainWindow.menuBar().addMenu("&Fichier")
        self.fileMenu1 = MainWindow.menuBar().addMenu("&Edition")
        self.fileMenu2 = MainWindow.menuBar().addMenu("&?")
        

        self.exit_button = QAction('&Exit', MainWindow)
        self.exit_button.setShortcut('Ctrl+Q')
        self.exit_button.setStatusTip('Exit application')
        self.exit_button.triggered.connect(MainWindow.close)


        self.copy_button = QAction('&Copy', MainWindow)
        self.copy_button.setEnabled(False)
        self.copy_button.setShortcut('Ctrl+C')
        self.copy_button.triggered.connect(self.text_Etapes_Traitements.copy)

        self.aboutApp = QAction(QIcon('Icones/Bâti2.png'), "&A propos de l'app", MainWindow, triggered = self.about)
        
        self.aboutAsal = QAction(QIcon('Icones/logo asal -0.png'), "A propos de l'ASAL", MainWindow, triggered= self.aboutAsa)

        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exit_button)
        self.fileMenu1.addAction(self.copy_button)
        self.fileMenu2.addAction(self.aboutApp)
        self.fileMenu2.addAction(self.aboutAsal)
        
###############################################################################################
        retranslateUi(self,MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox_7.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

################################################################################################

