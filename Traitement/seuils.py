import cv2
from matplotlib import pyplot as plt
import numpy as np

def seuil(image):
    filename = ''
    filename = image
    if filename != '':
        img = cv2.imread(filename)
        img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        retval, seuil = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
        fichier = open("Traitement/etapesTraitement.txt", "w")
        l = ['<b style = color:blue;>Appliquer des seuils<b>', "lecture d'image" ,"Application de seuil binaire sur l'image originale"]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        l.append("transformation de RGB vers le GRAY")
        retval2, seuil2 = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY)
        gaus = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
        l.append("\t 1. Application d'un seuil Adaptatiptatif (seuil adaptatif Gaussien) sur l'image en GRAY")
        retval2, otsu = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        l.append("\t 2. Application de seuil d'Otsu sur l'image en GRAY")
        #laplacian = cv2.Laplacian(gray,cv2.CV_64F)
        l.append("Affichage de résultats")

        fichier.write(str(len(l))+"\n")

        for i in l:
            fichier.write(str(i)+"\n")
        fichier.close()

        plt.subplot(2,2,1),plt.imshow(img1)
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(2,2,2),plt.imshow(seuil,cmap = 'gray')
        plt.title('Binary'), plt.xticks([]), plt.yticks([])
        plt.subplot(2,2,3),plt.imshow(gaus,cmap = 'gray')
        plt.title('Gauss'), plt.xticks([]), plt.yticks([])
        plt.subplot(2,2,4),plt.imshow(otsu,cmap = 'gray')
        plt.title('OTSU'), plt.xticks([]), plt.yticks([])
        plt.show()
