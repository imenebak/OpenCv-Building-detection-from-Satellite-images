import cv2
import numpy as np
import time

def get_iou(a, b, epsilon=1e-5):
    """ Given two boxes `a` and `b` defined as a list of four numbers:
            [x1,y1,x2,y2]
        where:
            x1,y1 represent the upper left corner
            x2,y2 represent the lower right corner
        It returns the Intersect of Union score for these two boxes.

    Args:
        a:          (list of 4 numbers) [x1,y1,x2,y2]
        b:          (list of 4 numbers) [x1,y1,x2,y2]
        epsilon:    (float) Small value to prevent division by zero

    Returns:
        (float) The Intersect of Union score.
    """
    # COORDINATES OF THE INTERSECTION BOX
    x1 = max(a[0], b[0])
    y1 = max(a[1], b[1])
    x2 = min(a[2], b[2])
    y2 = min(a[3], b[3])

    # AREA OF OVERLAP - Area where the boxes intersect
    width = (x2 - x1)
    height = (y2 - y1)
    # handle case where there is NO overlap
    if (width<0) or (height <0):
        return 0.0
    area_overlap = width * height

    # COMBINED AREA
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    area_b = (b[2] - b[0]) * (b[3] - b[1])
    area_combined = area_a + area_b - area_overlap

    # RATIO OF AREA OF OVERLAP OVER COMBINED AREA
    iou = area_overlap / (area_combined+epsilon)
    return iou
def chocolathouses(img):
    
    #print("Press the 'b' key to close")
    time.sleep(2)

    frame = cv2.imread(img)
    #rUnse2xzQFOfHqaxBv9P0Wgh0m4.jpg
    #Sans titre.png

    # Converts BGR to HSV color codes
    #It uses BGR not RGB, weird isn't it?
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #image = cv2.rectangle(frame,(500,400), (100,100), (0,0,0), 2)

    #Primary colors
    area0 = 300

    #range of red done
    if img == "Images/Image7.jpg":
        
        lower_red = np.array([2,75,131],np.uint8)
        upper_red = np.array([12,253,253],np.uint8)
        area0 = 300
    else:
        lower_red = np.array([2,104,162],np.uint8)
        upper_red = np.array([5,148,225],np.uint8)
        area0 = 1000

    # defining colors and stuff
    red=cv2.inRange(hsv,lower_red,upper_red)

    #boring stuff for the computer to deal with
    this = np.ones((5 ,5), "uint8")

    red=cv2.dilate(red, this)
    if img == "Images/Image2.png":
        red=cv2.dilate(red, this)
        red=cv2.dilate(red, this)
    bdb=cv2.bitwise_and(frame, frame, mask = red)

    listt = []
    somme = 0
    #Tracks Red
    (_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area>area0):
            x,y,w,h = cv2.boundingRect(contour)
            rec1 = [x, y, x+w, y+h]
            listt.append(rec1)
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
    for pic, contour in enumerate(contours):
        area1 = cv2.contourArea(contour)
        if(area>100):
            x,y,w,h = cv2.boundingRect(contour)
            rec2 = [x, y, x+w, y+h]
            if (len(listt) > 0):    
                for i in range(0, len(listt)):
                    a = get_iou(listt[i], rec2, 1e-5)
                    somme += a
                if somme == 0:
                    frame = cv2.rectangle(frame,(rec2[0], rec2[1]),(rec2[2],rec2[3]),(0,255,255),2)

           
            #cv2.putText(frame,"DAR",(x,y),cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,255))
                rec1 = rec2


    cv2.imshow("Detected",frame)
    #cv2.imshow("Color Blind Assistant",red)



    #end it by pressing b
    if cv2.waitKey(10) & 0xFF == ord('b'):
        cv2.destroyAllWindows()


#chocolathouses("../Images/Image7.jpg")
#chocolathouses("../Images/Image2.png")

