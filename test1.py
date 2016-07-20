import numpy as np
import cv2


def play(frame,j): #frame,j
    param1=[15,22,10]
    param2=[67,87,200]
    
    #frame = cv2.imread('1.jpg')

    lower=np.array(param1)
    upper=np.array(param2)
    
    mask=cv2.inRange(frame,lower,upper)
    cv2.imshow("image",frame)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    #mask=cv2.inRange(frame,lower,upper)
    #res=cv2.bitwise_and(frame,frame,mask=mask)

    gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)         #GRAY
    ret,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)          #THRESH
    
    cv2.imshow('thresh',res)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)    #CONTOUR
   # print len(contours)
    
    for i in range(0,len(contours)):
       
        print cv2.contourArea(contours[i])
        if cv2.contourArea(contours[i])>=300.5 and cv2.contourArea(contours[i])<=400.5:
        #if cv2.contourArea(contours[i])==max(cv2.contourAreacountours[]):
            cv2.drawContours(res,contours,i,(255,0,0),1)
            M = cv2.moments(contours[i])
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            centroid = cx,cy
            cv2.circle(res,(cx,cy),5,(0,255,0),2)
            x,y,w,h = cv2.boundingRect(contours[i])

            h1,w1,c=res.shape
            hi=int(h1/11)
            wj=int(w1/11)

            

            
           # print x,y,w,h
            #img = cv2.rectangle(res,(x,y),(x+w,y+h),(0,255,0),2)
                           
            
                    
            #slope=float((369-342)//(297-285))
            slope=float((cy-y))/(cx-x)
            #print slope
                                        
            y1=2*hi
            #print y1
            x1=int(cx-((cy-y1)/slope))

            #img3 = cv2.line(res,(290,372),(cx,cy),(19,200,255),1)
            img3 = cv2.line(res,(x1,y1),(cx,cy),(192,209,21),1)
            cv2.imshow('Cont'+str(j),res)

            #levels
            l=[wj,2*wj,3*wj,4*wj,5*wj,6*wj,7*wj,8*wj,9*wj,10*wj,11*wj]
            #list
            b=['F','G','H','I','J','K','L','M','N','O','P']

            for i in range(0,11):
                       # print i
                 if x1 in range(i*wj,(i+1)*wj):
                    
                    return b[i]
                    

##frame = cv2.imread('1.jpg')
##balloon = play(frame)
##print balloon
alpha_list = []
for file_number in range(1,11):
    file_name = str(file_number)+".jpg"
    frame = cv2.imread(file_name)
    cv2.imshow('window',frame)
    balloon_letter = play(frame,file_number)
    alpha_list.append(balloon_letter)
print alpha_list                          

cv2.waitKey(0)
cv2.destroyAllWindows()
