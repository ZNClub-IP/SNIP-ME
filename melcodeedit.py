import numpy as np
import cv2

#Teams can add other helper functions which can be \
#added here
def play(img):
    '''
    img-- a single test image as input argument
    letter -- returns the single character specifying the target that was 
    hit  eg. 'A', 'D', etc
    '''
    #add your code here
    img1 = img
    #ret, thresh1 = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY_INV)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)         #GRAY
    ret,thresh1 = cv2.threshold(gray,127,255,0)          #THRESH
    contours, heirarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img1,contours,-1,(255,0,0),3)
    gx1,gx2,gy1,gy2 = 0,0,0,0
#    print len(contours)
    for i in range(len(contours)):
        if cv2.contourArea(contours[i]) > 1:
            M = cv2.moments(contours[i])
            cy = int(M["m01"] / M["m00"])
        if cv2.contourArea(contours[i]) >= 83.0 and cv2.contourArea(contours[i]) <= 93.0 and cy >= 300 and cy <= 400:
            x,y,w,h = cv2.boundingRect(contours[i])
            gx1 = x
            gx2 = x + w
            gy1 = y
            gy2 = y + h
            cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),2)
    """
    x,y,w,h = cv2.boundingRect(contours[812])
    cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),2)

    print cv2.contourArea(contours[812])
       """
    slope = float(gy2 - gy1) / float(gx2 - gx1)
    X = (float(45 - gy1) / slope) + gx1 
#    print X
    cv2.line(img1, (gx1, gy1), (int(X), 45), (0, 0, 0), 2)
    cv2.imshow("Window", img1)
    cv2.waitKey(3000)
    my_list = [0, 77, 77*2, 77*2, 77*3, 77*4, 77*5, 77*6, 77*7, 77*8, 77*9]
    alpha = 0
    letter = ""
    for i in my_list:
        if X >= 0 + i and X <= 77 + i:
            letter = str(chr(70 + alpha))
            break
        alpha += 1  
    return letter

#if __name__ == "__main__":
    #checking output for single image
for i in range(0,1):
    img = cv2.imread('test_images/10.jpg')
    balloon_letter = play(img)
    print balloon_letter, " balloon in range"
    #checking output for all images
    '''
    alpha_list = []
    for file_number in range(1,11):
        file_name = str(file_number)+".jpg"
        pic = cv2.imread(file_name,0)
        balloon_letter = play(pic)
        alpha_list.append(balloon_letter)
    print alpha_list
    '''
if cv2.waitKey(0)==27:        
    cv2.destroyAllWindows()
