#!/usr/bin/env python
import numpy as np
import cv2
import argparse
import os
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 10
valid_image_extensions = [".jpg", ".jpeg", ".png", ".tif", ".tiff"]
image_path_list = []
temp_path_list = []


class Detect:
    def __init__(self, args):
        self.successful = 0
        self.success = 0
        self.sift = cv2.xfeatures2d.SIFT_create()

        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)

        self.flann = cv2.FlannBasedMatcher(index_params, search_params)

        for file in os.listdir(args.in_path):
            extension = os.path.splitext(file)[1]
            if extension.lower() not in valid_image_extensions:
                continue
            image_path_list.append(file)
            
        for file in os.listdir(args.find):
            extension = os.path.splitext(file)[1]
            if extension.lower() not in valid_image_extensions:
                continue
            temp_path_list.append(file)
            
        self.search(args)

    def search(self, args):
        # load query image
        # repeat for the number specified in args
        for i in range(len(image_path_list)):
            # load image
            #print(args.in_path + image_path_list[i])
            original = cv2.imread(args.in_path + image_path_list[i], 0)
            original_color = cv2.imread(args.in_path + image_path_list[i], 1)
            for j in range(len(temp_path_list)):
                #print(args.find + temp_path_list[j])
                
                query_image = cv2.imread(args.find + temp_path_list[j], 0)
                # find the keypoints and descriptors with SIFT
                
                kp1 = self.sift.detect(query_image, None)
                kp2 = self.sift.detect(original, None)
                des1 = self.sift.compute(query_image, kp1)
                des2 = self.sift.compute(original, kp2)

                matches = self.flann.knnMatch(des1[1], des2[1], k=2)

                # store all the good matches as per Lowe's ratio test.
                good = []
                for m,n in matches:
                    if m.distance < 0.7*n.distance:
                        good.append(m)

                if len(good)>MIN_MATCH_COUNT -2 :
                    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
                    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

                    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
                    matchesMask = mask.ravel().tolist()
                    
                    h,w = query_image.shape
                    pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
                    dst = cv2.perspectiveTransform(pts, M)

                    out = original_color
                    # if the lines need to be visible
                    if args.lines.lower() == 'square':
                        out = self.draw_rectangle(out, [np.int32(dst)])
                    elif args.lines.lower() == 'original':
                        out = cv2.polylines(out, [np.int32(dst)] ,True, 255, 2,cv2.LINE_AA)

                    # if method is chosen
                    if args.method.lower() == 'rotate':
                        out = self.rotate_image(out, [np.int32(dst)])
                    self.successful += 1

                else:
                    #print ("Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT))
                    matchesMask = None
                    
            if self.successful > 0:
                self.success += 1
                self.successful = 0
                extension = '.' + image_path_list[i].split('.')[1]
                output_path = (args.out_path + "%5d" + extension) % self.success
                cv2.imwrite(output_path, out)
                img1 = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)
                plt.subplot(2,3,0+self.success),plt.imshow(img1)
                plt.title("Image" + str(self.success)), plt.xticks([]), plt.yticks([])
                #cv2.imshow("b", out)
                

        print ('Finished with %d detected images of the %d' % (self.success, len(image_path_list)))
        plt.show()
    # solution 1: just make a rectangle over the detected rectangle
    def draw_rectangle(self, img, points):
        # Calculate rectangle and center
        corners = self.calculate_rectangle_opposite_corners(points)
        img = cv2.rectangle(img, corners[0], corners[1], (0, 0, 255), 4)
        return img

    @staticmethod
    def calculate_rectangle_opposite_corners(points):
        left = right = points[0][0][0][0]
        top = bottom = points[0][0][0][1]
        for i in range(4):
            new_x = points[0][i][0][0]
            new_y = points[0][i][0][1]
            if new_x < left:
                left = new_x
            elif new_x > right:
                right = new_x
            if new_y < top:
                top = new_y
            elif new_y > bottom:
                bottom = new_y
        corners = [(left, top), (right, bottom)]
        return corners

    @staticmethod
    def calculate_center(points):
        x = (points[0][0] + points[1][0])/2
        y = (points[0][1] + points[1][1])/2
        point = (x, y)
        return point

    # solution 2: rotate the image
    def rotate_image(self, img, points):
        angle = self.calculate_rotation(points)
        corners = self.calculate_rectangle_opposite_corners(points)
        center = self.calculate_center(corners)

        angle *= 180/np.pi

        shape = img.shape[:2]

        matrix = cv2.getRotationMatrix2D(center, angle, 1)
        img = cv2.warpAffine(img, matrix, shape)

        return img

    def calculate_rotation(self, points):
        # calculate middle of rectangle
        corners = self.calculate_rectangle_opposite_corners(points)
        p1 = self.calculate_center(corners)

        # calculate middle of point3 en 4
        point3 = points[0][2][0]
        point4 = points[0][3][0]
        p2 = self.calculate_center([point3, point4])

        # calculate distance between p1 and p2 in our case equal to distance between p1 and p3
        s3 = s2 = self.calculate_distance(p1, p2)

        # define p3
        p3 = ((p1[0] + s2), p1[1])

        # calculate distance between p2 and p3
        s1 = self.calculate_distance(p2, p3)

        # calculate angle
        angle = self.calculate_angle(s1, s2, s3)

        if p2[1] < p1[1]:
            angle = -angle
        return angle

    @staticmethod
    def calculate_distance(point1, point2):
        # calculate the power of (x1-x2)^2 and (y1-y2)^2
        arg = np.power([(point1[0] - point2[0]), (point1[1] - point2[1])], 2)
        distance = np.sqrt(arg[0] + arg[1])
        return distance

    @staticmethod
    def calculate_angle(side1, side2, side3):
        # calculate arccos((b^2+c^2-a^2)/(2*b*c))
        power = np.power([side1, side2, side3], 2)
        x = power[1] + power[2] - power[0]
        y = 2 * side2 * side3
        angle = np.arccos(x/y)
        return angle
    

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--find', type=str,
                        help='Give the path to the image you want to find. Default is this ./train.jpg.',
                        default='Detection/temp1/')
    parser.add_argument('--in_path', type=str,
                        help='Specify the path to the directory with images.',
                        default='Detection/img/')
    parser.add_argument('--out_path', type=str,
                        help='Specify the path to the directory with images.',
                        default='Detection/out/')
    parser.add_argument('--method', type=str,
                        help='Choose the method of detection. Options: original / rotate. Default is this square.',
                        default="original")
    parser.add_argument('--lines', type=str,
                        help='Choose if you want to show certain lines. Option: original / square / all / none. Default: none',
                        default='square')
    arguments = parser.parse_args()
    sp = Detect(arguments)
    cv2.destroyAllWindows()
