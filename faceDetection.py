#simple  Face Detection using Haar Cascade Classifiers
import cv2

#define the classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Read the input image
#img = cv2.imread('test.jpg')


#     #convert to grayscale image
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# #the function to detect the face
# # param 1: image: an grayscale image where objects are detected
# # param 2: scaleFactor: how much the image size is reduced at each image scale
# # param 3: minNeighbors: how many neighbors each candidate rectangle should have to retain it
# faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)


# #Display the output image
# cv2.imshow('image', img)
# cv2.waitKey()
#-----------------------------------
#IN VIDEO
cap = cv2.VideoCapture('test.mp4')

while cap.isOpened():
    _, img = cap.read()

        #convert to grayscale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #the function to detect the face
    # param 1: image: an grayscale image where objects are detected
    # param 2: scaleFactor: how much the image size is reduced at each image scale
    # param 3: minNeighbors: how many neighbors each candidate rectangle should have to retain it
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)


    #Display the output image
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
