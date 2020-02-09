import cv2
import numpy as np


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

def mainGl(img, img1):
    im2 = ''
    if img == "Images/Image5.jpg":
        im2 = cv2.imread("Images/Image52.jpg", 0)
        a = 0.35
    else:
        a = 0.35
    img_bgr = cv2.imread(img)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(img1, 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = a
    loc = np.where(res >= threshold)
    a = 0
    rec1 = []
    rec2 = []
    for pt in zip(*loc[::-1]):
        rec1 = [pt[0], pt[1], pt[0]+w, pt[1]+h]
        cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,0,255), 2)
        break
    for pt in zip(*loc[::-1]):
        rec2 = [pt[0], pt[1], pt[0]+w, pt[1]+h]
        a = get_iou(rec1, rec2, 1e-5)
        if a == 0:
            cv2.rectangle(img_bgr,pt, (pt[0]+w, pt[1]+h), (0,0,255), 2)
            
        rec1 = rec2

    if img == "Images/Image5.jpg":
        w1, h1 = im2.shape[::-1]
        res2 = cv2.matchTemplate(img_gray, im2, cv2.TM_CCOEFF_NORMED)
        loc1 = np.where(res2 >= 0.65)
        
        a = 0
        rec1 = []
        rec2 = []
        
        for p in zip(*loc1[::-1]):
            rec1 = [p[0], p[1], p[0]+w1, p[1]+h1]
            cv2.rectangle(img_bgr, p, (p[0]+w1, p[1]+h1), (0,0,255), 2)
            break
        for p in zip(*loc1[::-1]):
            rec2 = [p[0], p[1], p[0]+w1, p[1]+h1]
            a = get_iou(rec1, rec2, 1e-5)
            if a == 0:
                cv2.rectangle(img_bgr,p, (p[0]+w1, p[1]+h1), (0,0,255), 2)
            
            rec1 = rec2
    
    cv2.imshow('detected', img_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
