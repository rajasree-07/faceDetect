import cv2

alg="haarcascade_frontalface_default.xml";
har_cascade=cv2.CascadeClassifier(alg)

cam=cv2.VideoCapture(0)
while True:
    
          _,img=cam.read()
          grayscaleImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
##          cv2.imshow("grayImg",grayscaleImg)

          face=har_cascade.detectMultiScale(grayscaleImg,1.3,2)

          for (x,y,w,h) in face:
              rectangle=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
              cv2.imshow("faceDetect",rectangle)
              print("face Detected")
              key=cv2.waitKey(10)
              print(key)
              if key == 113:
                break
            
              
cam.release()
cv2.destroyAllWindows()
