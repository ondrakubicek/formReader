import cv2
import numpy as np
import pytesseract
import os

MAX_FEATURES = 500
GOOD_MATCH_PERCENT = 0.15

class dataReader:


    def __init__(self, pointsOfInterest, query):
        self.pointsOfInterest = pointsOfInterest
        self.query = query
        self.per = 90

    def alignImages(self, im1, im2):

        # Convert images to grayscale
        im1Gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
        im2Gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

        # Detect ORB features and compute descriptors.
        orb = cv2.ORB_create(MAX_FEATURES)
        keypoints1, descriptors1 = orb.detectAndCompute(im1Gray, None)
        keypoints2, descriptors2 = orb.detectAndCompute(im2Gray, None)

        # Match features.
        matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
        matches = matcher.match(descriptors1, descriptors2, None)

        # Sort matches by score
        matches.sort(key=lambda x: x.distance, reverse=False)

        # Remove not so good matches
        numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
        matches = matches[:numGoodMatches]

        # Draw top matches
        imMatches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
        h, w, c = im1.shape
        cv2.imshow("matches", cv2.resize(imMatches,(w//2,h//2)))

        # Extract location of good matches
        points1 = np.zeros((len(matches), 2), dtype=np.float32)
        points2 = np.zeros((len(matches), 2), dtype=np.float32)

        for i, match in enumerate(matches):
            points1[i, :] = keypoints1[match.queryIdx].pt
            points2[i, :] = keypoints2[match.trainIdx].pt

        # Find homography
        h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

        # Use homography
        height, width, channels = im2.shape


        im1Reg = cv2.warpPerspective(im1, h, (width, height))
        cv2.imwrite("matches.jpg", im1Reg)

        return im1Reg, h

    def readData(self, image):
        # load query
        # ----

        img1 = cv2.imread(self.query)

        filestr = image.read()
        #convert string data to numpy array
        npimg = np.fromstring(filestr, np.uint8)
        # convert numpy array to image
        img2 = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        imgScan, asx = self.alignImages(img2, img1)

        imgShow = imgScan.copy()

        imgMask = np.zeros_like(imgShow)
        subdata = {}

        # points of interest
        for x,r in enumerate(self.pointsOfInterest):
            cv2.rectangle(imgMask,(r[0][0],r[0][1]),(r[1][0],r[1][1]),(0,255,0),cv2.FILLED)
            imgShow = cv2.addWeighted(imgShow, 0.99, imgMask, 0.1,0)
            imgCrop = imgScan[r[0][1]:r[1][1], r[0][0]:r[1][0]]

            text = pytesseract.image_to_string(imgCrop, 'ces').strip()
            text = str(text)

            if text:
                if r[2] == 'array':
                    try:
                        subdata[r[3]].append(text)
                    except:
                        subdata[r[3]] = []
                        subdata[r[3]].append(text)
                else:
                    subdata[r[3]] = text

        return subdata
