#####       SHOOT THE BALLOON
####
###
##
#




import numpy as np
import cv2

#Teams can add other helper functions which can be \
#added here

def play(img):

    
    #dim
    h,w,c=img.shape
    #color=[[0,0,0],[255,255,255],[1,1,222],[222,1,100],[255,255,109]]   #5

    
    
    cv2.imshow('IMG',img)
    print "%d x %d "%(h,w)
    hi=int(h/11)
    wj=int(w/11)
    
    #levels
    l=[wj,2*wj,3*wj,4*wj,5*wj,6*wj,7*wj,8*wj,9*wj,10*wj,11*wj]
    #list
    b=['F','G','H','I','J','K','L','M','N','O','P']
    
    #contour
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)         #GRAY
    ret,thresh = cv2.threshold(gray,127,255,0)          #THRESH
    #cv2.imshow('gray',thresh)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)    #CONTOUR
    #print len(contours)
    
    #cv2.drawContours(img,contours,-1,(0,0,0),4)        #DRAW CONTOUR
    #print contours[100]



    for i in range(0,len(contours)):        
        M = cv2.moments(contours[i])
        try:
            cx = int(M['m10']//M['m00'])
            cy = int(M['m01']//M['m00'])

                        #REQUIRED CENTROID
            if cy>=344 and cy<=387 and  len(contours[i])>=25 and len(contours[i])<=55:                
                print "Centroid = ", cx, ", ", cy
                #print i
                #print len(contours[i]),"\n"
                #print contours[i]

                
                cv2.circle(img,(cx,cy), 5, (19,200,255), -1)
                cv2.drawContours(img,contours,i,(10,0,255),1)
                img3 = cv2.line(img,(0,cy),(cx,cy),(19,200,255),1)
                img3 = cv2.line(img,(cx,0),(cx,cy),(19,200,255),1)
                
                #cv2.circle(img,(285,342), 5, (19,200,255), -1)
                #cv2.circle(img,(297,369), 5, (19,200,255), -1)
                #m=search(contours[i])
                
                
                x,y,w,h = cv2.boundingRect(contours[i])
                '''
                print x,y,w,h
                img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                '''                
                
                #slope=float((369-342)//(297-285))
                slope=float((h)//(w))
                print slope
                                    
                y1=1*hi
                x1=int(cx-((cy-y1)/slope))

                img3 = cv2.line(img,(x1,y1),(cx,cy),(19,200,255),1)

                for i in range(0,11):
                    print i
                    if x1 in range(i*wj,(i+1)*wj):
                        return b[i]
                        #break                        
                                            
        except: #ZeroDivisionError as er: #BUG : ERROR of DIVISION
            #print "error"+str(er)
            pass
            
    #grid
    i=1
    j=1
    while i<h or j<w:
        if i==345 or i==388:
            img3 = cv2.line(img,(0,i),(w,i),(1,1,255),2)
            img3 = cv2.line(img,(j,0),(j,h),(255,255,255),2)
        else:
            img3 = cv2.line(img,(0,i),(w,i),(1,1,1),2)
            img3 = cv2.line(img,(j,0),(j,h),(255,255,255),2)
        i=hi+i
        j=wj+j

        
    '''
    i=10
    print "Area = ", cv2.contourArea(contours[i])
    print "Perimeter = ", cv2.arcLength(contours[i],True)
    M = cv2.moments(contours[i])
    try:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        print "Centroid = ", cx, ", ", cy
        cv2.circle(img,(cx,cy), 5, (0,0,255), -1)
    except:
        pass
    '''

    
    #cv2.imshow('CONTOUR',img3)
    #cv2.imwrite('saved3.jpeg',img)        
    #return letter
'''
for file_number in range(1,11):
    file_name = "test_images/"+str(file_number)+".jpg"
    img = cv2.imread(file_name)
    balloon_letter = play(img)
'''
    
img = cv2.imread('test_images/10.jpg')    
print play(img)
cv2.imshow('CONTOUR',img)

if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()
