import cv2
import numpy as np
from matplotlib import pyplot as plt

def morphologique(img):
    
    frame = cv2.imread(img)
    fichier = open("Traitement/etapesTraitement.txt", "w")
    frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    l = ['<b style = color:blue;>Appliquer des opérations morphologiques<b>',"lecture d'image"  ]
    l.append("Transfomation de RGB vers HSV")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l.append("Transfomation de RGB vers HSV")
    lower_red = np.array([20,100,50])
    upper_red = np.array([170,255,150])
    l.append("Definir un seuil min et max pour le masque")

    #filtre
        
    mask = cv2.inRange(hsv, lower_red, upper_red)
    l.append("Création de masque")
    res = cv2.bitwise_and(frame, frame, mask = mask)
    l.append("Applique le masque sur l'image originale")

    #transformations morphologiques
    kernel = np.ones((5,5) ,np.uint8)
        
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(mask, kernel, iterations = 1)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    l.append("Applique les transformation morphologique sur l'image masqué")

    l.append("Affichage de résultats")

    fichier.write(str(len(l))+"\n")

    for i in l:
        fichier.write(str(i)+"\n")
    fichier.close()

    plt.subplot(2,3,1),plt.imshow(frame1)
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,2),plt.imshow(res,cmap = 'hsv')
    plt.title('Image filtré'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,3),plt.imshow(erosion,cmap = 'gray')
    plt.title('Erosion'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,4),plt.imshow(dilation,cmap = 'gray')
    plt.title('Dilation'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,5),plt.imshow(opening,cmap = 'gray')
    plt.title('Opening'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,6),plt.imshow(closing,cmap = 'gray')
    plt.title('Closing'), plt.xticks([]), plt.yticks([])
    plt.show()
