'''#PACKAGES REQUIRED ARE:
#step-1: register the face with adhar is done
import cv2
import pickle #used for creating .pkl files where we can store multiple thousands of users face data in the form of text.
#it is converted so that the size is less. we will not store face data but we will store oyr face into text format
import numpy as np# used to create numpy array which stores 50 images with names of an individual.
import os #module for creating and reading files

#whenever this file loads it check whether the data folder exist or not if it doesnt exist then it simply creates the file 
if not os.path.exists('data/'):
    os.makedirs('data/')
#cv2.videocapture is used to load the webcam ie., it will open my computer camera
video=cv2.VideoCapture(0)#here 0 means first camera 1 means 2nd cmaera so on you can change according to ur need
#now we're going to use face detection
facedetect=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# haarcascade_frontalface_default.xml is the file name
# it is trained model for face detection given by open cv2
#we use is cascadeclassifier in that we use haar cascade. We just need to import this as it is available by default

#we have empty face data array which stores images
faces_data=[]
#we use loop to click images of a person
i=0
name=input("enter your aadhar number:")#to verify the face of a peron and link i ask aadhar but u can ask anything
framesTotal=51 #it is no of frames required to store the images that are clicked of an indiviual
captureAfterFrame=2#it means after every 2 frames click photo that frames are 51 but photos are 25

while True:#used to click photo
    ret,frame=video.read()#read/start the video
    #now we will get the frmae in every millisecond so lets convert it into gray
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #A grayscale image is composed exclusively of shades of gray, varying from black at the weakest intensity to white 
    #at the strongest1. Each pixel in a grayscale image represents a single sample of light intensity, without any color information1.
    #This type of image is often used in photography, computer-generated imagery, and various scientific applications.
    #v2.COLOR_BGR2GRAY:used to convert the image into gray scale
    faces=facedetect.detectMultiScale(gray,1.3,5)
    #every face will ahve 4 parameters by default
    for(x,y,w,h) in faces:#using this parameters we have to create a rectangle around the frame
        crop_img=frame[y:y+h,x:x+w]#means from whole video get the small box
        resized_img=cv2.resize(crop_img,(50,50))#resize that croped image to 50 50 pixels
        if len(faces_data)<=framesTotal and i%captureAfterFrame==0:#runs from 0 to 51 and i%captureAfterFrame==0 means when it is true then it capture the image
            faces_data.append(resized_img)#adding the image to the array we have created to store faces
        i=i+1
        cv2.putText(frame,str(len(faces_data)),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),1)#means after 51 frames it stops
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),1)#rectangle on the video




    cv2.imshow('frame',frame)#show the frame
    k=cv2.waitKey(1)#wait for few minutes
    if k==ord('q') or len(faces_data)>=framesTotal:
        break #if someone presses q or it reaches lst index break
video.release()
cv2.destroyAllWindows()#using this we are going to destroy the data or video

faces_data=np.asarray(faces_data)
faces_data=faces_data.reshape((framesTotal,-1))

print(len(faces_data))
#we will convert it into numpy array as we are not storing the faces but we are storing the text data of images so that data is less(into text or buffer to reduce the size)

if 'names.pkl' not in os.listdir('data/'):#if adhar is not present 
    names=[name]*framesTotal#according to the frames get the aadhar no and dump those names and evry frame is linked with adhar
    with open('data/names.pkl','wb') as f:
        pickle.dump(names,f)
else:#if adhar present
    with open('data/names.pkl','rb') as f:
        names=pickle.load(f)#if the file exist then open this file and load the previous daata and append the new data
    names=names+[name]*framesTotal#adding newnames  to existing
    with open('data/names.pkl','wb') as f:
        pickle.dump(names,f)#we will save the data to the existing ones only to have  the record

#we are goin to link every image with every name

if 'faces_data.pkl' not in os.listdir('data/'):
    with open('data/faces_data.pkl','wb') as f:
        pickle.dump(faces_data,f)
else:#if exist then append to original ones
    with open('data/faces_data.pkl','rb') as f:
        faces=pickle.load(f)
    faces=np.append(faces,faces_data,axis=0)
    with open('data/faces_data.pkl','wb') as f:
        pickle.dump(faces,f)

'''
''''''
import cv2
import pickle
import numpy as np
import os

if not os.path.exists('data/'):
    os.makedirs('data/')

video = cv2.VideoCapture(0)
facedetect= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces_data = []

i=0
name = input("Enter your aadhar number: ")
framesTotal=51
captureAfterFrame=2

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=facedetect.detectMultiScale(gray, 1.3 ,5)
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]
        resized_img = cv2.resize(crop_img, (50, 50))
        if len(faces_data)<= framesTotal and i%captureAfterFrame==0:
            faces_data.append(resized_img)
        i=i+1
        cv2.putText(frame, str(len(faces_data)),(50,50),cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 1 )
        cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 1)


    cv2.imshow('frame', frame)
    k=cv2.waitKey(1)
    if k== ord('q') or len(faces_data) >= framesTotal:
        break


video.release()
cv2.destroyAllWindows()

# print(len(faces_data))
faces_data = np.asarray(faces_data)
faces_data = faces_data.reshape((framesTotal, -1))
print(faces_data)



if 'names.pkl' not in os.listdir('data/'):
    names=[name]*framesTotal
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)
else:
    with open('data/names.pkl', 'rb') as f:
        names=pickle.load(f)
    names=names+[name]*framesTotal
    with open('data/names.pkl', 'wb') as f:
        pickle.dump(names, f)
     

if 'faces_data.pkl' not in os.listdir('data/'):
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces_data, f)
else:
    with open('data/faces_data.pkl', 'rb') as f:
        faces=pickle.load(f)
    faces=np.append(faces, faces_data, axis=0)
    with open('data/faces_data.pkl', 'wb') as f:
        pickle.dump(faces, f)

