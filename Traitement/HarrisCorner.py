import cv2
import numpy as np
import os
import random
from matplotlib import pyplot as plt

def fct1(filename):
    img = cv2.imread(filename)
    #convertir l image en gray apres en float32
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    #detection de coins
    corners = cv2.goodFeaturesToTrack(gray, 100, 0.02, 10)
    corners = np.int0(corners)
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(img, (x,y), 3, 255, -1)
    return img

def fct2(filename):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)
    # Threshold for an optimal value, it may vary depending on the image.
    img[dst>0.05*dst.max()]=[0,0,255]
    return img
    
def Corner(img):
    Ecrire()
    img1 = fct1(img)
    img2 = fct2(img)
    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

    plt.subplot(1,2,1),plt.imshow(img1)
    plt.title('GoodFeatures'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(img2)
    plt.title('CornerHarris'), plt.xticks([]), plt.yticks([])
    plt.show()
    
def Ecrire():
    fichier = open("Traitement/etapesTraitement.txt", "w")
    l = ["<b style = color:blue;>Detection De Points d'interet</b>", 'lecture dimage']
    l.append("transformation en gris")
    l.append("application de méthode de goodFeatures")
    l.append("application de méthode de Harris")
    l.append("\t1-delatation")
    l.append("\t2-définir un seuil")
    l.append("affichage du résultat ")
    fichier.write(str(len(l))+"\n")
    for i in l:
        fichier.write(str(i)+"\n")
    fichier.close()




