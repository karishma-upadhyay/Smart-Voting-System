#step-2: recognise the person and give vote
#here we use knn 
#knn is used to classsify the person based upon the previously stored data it is classified to the catorgy to which it resembles more

# vote code

'''from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from win32com.client import Dispatch

def speak(str1):#this function is used to speak the text
    speak=Dispatch("SAPI.SpVoice")#SAPI.SpVoice it is default in windows
    speak.Speak(str1)

video=cv2.VideoCapture(1)
facedetect=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
if not os.path.exists('data/'):
    os.makedirs('data/')

with open('data/names.pkl','rb') as f:
    LABELS=pickle.load(f)

with open('data/faces_data.pkl','rb') as f:
    FACES=pickle.load(f)

knn=KNeighborsClassifier(n_neighbors=5)
#faces and names are our database
knn.fit(FACES,LABELS)#database
#load the image

imgBackground=cv2.imread("background.jpg")

COL_NAMES=['NAME','VOTE','DATE','TIME']

while True:#to compare the face and the adta in the database of that individual
    ret,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=facedetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:#it runs until the person votes
        crop_img=frame[y:y+h,x:x+w]
        resized_img=cv2.resize(crop_img,(50,50)).flatten().reshape(1,-1)
        output=knn.predict(resized_img)#it gives label as outpt
        ts=time.time()
        date=datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")
        exist=os.path.isfile("Votes"+".csv")
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
        cv2.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
        cv2.putText(frame,str(output[0]),(x,y-15),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),1)
        attendance=[output[0],timestamp]
        #used to show the screen at a specific position

    imgBackground[370:370 + 480, 225:225 + 640] = frame
    
    cv2.imshow('frame',imgBackground)
    k=cv2.waitKey(1)

    def check_if_exists(value):
        try:#it check whether the user is trying to vote multiple times or not
            with open("Votes.csv","r") as csvfile:
                reader=csv.reader(csvfile)
                for row in reader:
                    if row and row[0]==value:
                        return True

        except FileNotFoundError:
            print("File not found or unable to open the csv file.")
        return False
    
    voter_exist=check_if_exists(output[0])
    if voter_exist:
        speak("YOU HAVE ALREADY VOTED")
        break
    if k==ord('1'):#if u haven't voted
        speak("YOUR VOTE HAS BEEN RECORDED")
        if exist:
            with open("Votes"+".csv","+a") as csvfile:
                writer=csv.writer(csvfile)
                #output[0] used to get the specific adhar number
                attendance=[output[0],"BJP",date,timestamp]
                writer.writerow(attendance)
            csvfile.close()
        else:
            with open("Votes"+".csv","+a") as csvfile:
                writer=csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                attendance=[output[0],"YES",date,timestamp]
                writer.writerow(attendance)
            csvfile.close()
        speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
        break
    if k==ord('2'):#if u haven't voted
        speak("YOUR VOTE HAS BEEN RECORDED")
        time.sleep(3)

        if exist:
            with open("Votes"+".csv","+a") as csvfile:
                writer=csv.writer(csvfile)
                #output[0] used to get the specific adhar number
                attendance=[output[0],"BJP",date,timestamp]
                writer.writerow(attendance)
            csvfile.close()
        else:
            with open("Votes"+".csv","+a") as csvfile:
                writer=csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                attendance=[output[0],"CONGRESS",date,timestamp]
                writer.writerow(attendance)
            csvfile.close()
        speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
        break
    if k==ord('3'):#if u haven't voted
        speak("YOUR VOTE HAS BEEN RECORDED")
        time.sleep(3)
        if exist:
            with open("Votes"+".csv","+a") as csvfile:
                writer=csv.writer(csvfile)
                #output[0] used to get the specific adhar number
                attendance=[output[0],"AAP",date,timestamp]
                writer.writerow(attendance)
            csvfile.close()
        else:
            with open("Votes"+".csv","+a") as csvfile:
                writer=csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                attendance=[output[0],"YES",date,timestamp]
                writer.writerow(attendance)
            csvfile.close()
        speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
        break

    if k==ord('4'):#if u haven't voted
        speak("YOUR VOTE HAS BEEN RECORDED")
        time.sleep(3)
        if exist:
            with open("Votes"+".csv","+a") as csvfile:
                writer=csv.writer(csvfile)
                #output[0] used to get the specific adhar number
                attendance=[output[0],"NOTA",date,timestamp]
                writer.writerow(attendance)
            csvfile.close()
        else:
            with open("Votes"+".csv","+a") as csvfile:
                writer=csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                attendance=[output[0],"YES",date,timestamp]
                writer.writerow(attendance)
            csvfile.close()
        speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
        break

    video.release()
    cv2.destroyAllWindows()'''
'''
#front end 
import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def button_click(option):
    messages = {
        1: "You selected 'BJP'",
        2: "You selected 'CONGRESS'",
        3: "You selected 'AAP'",
        4: "You selected 'NOTA'"
    }
    messagebox.showinfo("Selection", messages.get(option, "Invalid option"))

# Create the main window
root = tk.Tk()
root.title("Smart Voting System")

# Adjust the window size to fit a typical laptop screen
root.geometry("600x400")
root.configure(bg="#dff2f5")

# Title Label
title_label = tk.Label(root, text="SMART VOTING SYSTEM", font=("Arial", 20, "bold"), bg="#dff2f5")
title_label.place(x=120, y=20)

# Button options
buttons = [
    {"text": "Press '1' for 'BJP'", "color": "#FFA500", "option": 1},  # Orange for BJP
    {"text": "Press '2' for 'CONGRESS'", "color": "#00FF00", "option": 2},  # Green for Congress
    {"text": "Press '3' for 'AAP'", "color": "#00BFFF", "option": 3},  # Blue for AAP
    {"text": "Press '4' for 'NOTA'", "color": "#FF6347", "option": 4}   # Red for NOTA
]

# Create buttons and place them
for idx, button in enumerate(buttons):
    tk.Button(root, 
              text=button["text"], 
              font=("Arial", 14), 
              bg=button["color"], 
              fg="white", 
              command=lambda opt=button["option"]: button_click(opt)).place(x=400, y=100 + idx * 60, width=180, height=40)

# Add a frame to represent the voting area (left side)
voting_frame = tk.Frame(root, bg="white", width=350, height=300)
voting_frame.place(x=20, y=80)

# Run the application
root.mainloop()


#code

from sklearn.neighbors import KNeighborsClassifier

import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from win32com.client import Dispatch


def speak(str1):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)


video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
if not os.path.exists('data/'):
    os.makedirs('data/')

with open('data/names.pkl', 'rb') as f:
    LABELS = pickle.load(f)

with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)
imgBackground = cv2.imread("background.png")

COL_NAMES = ['NAME', 'VOTE', 'DATE', 'TIME']

def check_if_exists(value):
    try:
        with open("Votes.csv", "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row and row[0] == value:
                    return True
    except FileNotFoundError:
        print("File not found or unable to open the CSV file.")
    return False

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    
    output = None  # Initialize output to a default value
    for (x, y, w, h) in faces:
        crop_img = frame[y:y+h, x:x+w]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
        output = knn.predict(resized_img)
        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")
        exist = os.path.isfile("Votes.csv")
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
        cv2.rectangle(frame, (x, y-40), (x+w, y), (50, 50, 255), -1)
        cv2.putText(frame, str(output[0]), (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)
        attendance = [output[0], timestamp]
        
    imgBackground[370:370 + 480, 225:225 + 640] = frame
    cv2.imshow('frame', imgBackground)
    k = cv2.waitKey(1)
    
    if output is not None:
        voter_exist = check_if_exists(output[0])
        if voter_exist:
            speak("YOU HAVE ALREADY VOTED")
            break

        if k == ord('1'):
            speak("YOUR VOTE HAS BEEN RECORDED")
            time.sleep(5)
            if exist:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    attendance = [output[0], "BJP", date, timestamp]
                    writer.writerow(attendance)
            else:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(COL_NAMES)
                    attendance = [output[0], "BJP", date, timestamp]
                    writer.writerow(attendance)
            speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
            break

        if k == ord('2'):
            speak("YOUR VOTE HAS BEEN RECORDED")
            time.sleep(5)
            if exist:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    attendance = [output[0], "CONGRESS", date, timestamp]
                    writer.writerow(attendance)
            else:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(COL_NAMES)
                    attendance = [output[0], "CONGRESS", date, timestamp]
                    writer.writerow(attendance)
            speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
            break

        if k == ord('3'):
            speak("YOUR VOTE HAS BEEN RECORDED")
            time.sleep(5)
            if exist:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    attendance = [output[0], "AAP", date, timestamp]
                    writer.writerow(attendance)
            else:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(COL_NAMES)
                    attendance = [output[0], "AAP", date, timestamp]
                    writer.writerow(attendance)
            speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
            break

        if k == ord('4'):
            speak("YOUR VOTE HAS BEEN RECORDED")
            time.sleep(5)
            if exist:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    attendance = [output[0], "NOTA", date, timestamp]
                    writer.writerow(attendance)
            else:
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(COL_NAMES)
                    attendance = [output[0], "NOTA", date, timestamp]
                    writer.writerow(attendance)
            speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
            break

video.release()
cv2.destroyAllWindows()


'''

import tkinter as tk
from tkinter import messagebox
from threading import Thread
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from win32com.client import Dispatch
from PIL import Image, ImageTk
from sklearn.neighbors import KNeighborsClassifier


# Function to handle button clicks in Tkinter GUI
def button_click(option):
    global selected_option
    selected_option = option
    messagebox.showinfo("Selection", f"You selected option {option}")
    # Stop video capture if an option is selected
    global running
    running = False

# Initialize global variables
selected_option = None
running = True

# Create the main Tkinter window
def create_gui():
    global root
    root = tk.Tk()
    root.title("Smart Voting System")
    root.geometry("900x600")
    root.configure(bg="#dff2f5")

    title_label = tk.Label(root, text="SMART VOTING SYSTEM", font=("Arial", 20, "bold"), bg="#dff2f5")
    title_label.place(x=300, y=20)

    # Create a frame for the voting and camera side by side
    frame_container = tk.Frame(root, bg="#dff2f5")
    frame_container.place(x=20, y=80)

    # Create a frame for camera feed
    voting_frame = tk.Frame(frame_container, bg="white", width=450, height=400)
    voting_frame.grid(row=0, column=0)

    global image_label
    image_label = tk.Label(voting_frame)
    image_label.pack()

    # Create a frame for voting buttons next to the camera
    buttons_frame = tk.Frame(frame_container, bg="#dff2f5", width=350, height=400)
    buttons_frame.grid(row=0, column=1, padx=20)

    buttons = [
        {"text": "Press '1' for 'BJP'", "color": "#FFA500", "option": 1},
        {"text": "Press '2' for 'CONGRESS'", "color": "#00FF00", "option": 2},
        {"text": "Press '3' for 'AAP'", "color": "#00BFFF", "option": 3},
        {"text": "Press '4' for 'NOTA'", "color": "#FF6347", "option": 4}
    ]

    for idx, button in enumerate(buttons):
        tk.Button(buttons_frame,
                  text=button["text"],
                  font=("Arial", 14),
                  bg=button["color"],
                  fg="white",
                  command=lambda opt=button["option"]: button_click(opt)).pack(pady=20, fill='x')

    root.mainloop()

# Function to handle text-to-speech
def speak(text):
    speaker = Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

# Function to process video and detect faces
def process_video():
    global running
    video = cv2.VideoCapture(0)
    facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    with open('data/names.pkl', 'rb') as f:
        LABELS = pickle.load(f)

    with open('data/faces_data.pkl', 'rb') as f:
        FACES = pickle.load(f)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(FACES, LABELS)

    COL_NAMES = ['NAME', 'VOTE', 'DATE', 'TIME']

    def check_if_exists(value):
        try:
            with open("Votes.csv", "r") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row and row[0] == value:
                        return True
        except FileNotFoundError:
            print("File not found or unable to open the CSV file.")
        return False

    while running:
        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray, 1.3, 5)

        output = None
        for (x, y, w, h) in faces:
            crop_img = frame[y:y+h, x:x+w]
            resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
            output = knn.predict(resized_img)
            ts = time.time()
            date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
            timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")
            exist = os.path.isfile("Votes.csv")
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 1)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 2)
            cv2.rectangle(frame, (x, y-40), (x+w, y), (50, 50, 255), -1)
            cv2.putText(frame, str(output[0]), (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)
            attendance = [output[0], timestamp]

        # Convert image for Tkinter
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)

        image_label.config(image=img)
        image_label.image = img

        k = cv2.waitKey(1)

        if output is not None:
            voter_exist = check_if_exists(output[0])
            if voter_exist:
                speak("YOU HAVE ALREADY VOTED")
                running = False
                break

            if selected_option is not None:
                speak("YOUR VOTE HAS BEEN RECORDED")
                time.sleep(5)
                with open("Votes.csv", "a") as csvfile:
                    writer = csv.writer(csvfile)
                    vote = {
                        1: "BJP",
                        2: "CONGRESS",
                        3: "AAP",
                        4: "NOTA"
                    }
                    if exist:
                        attendance = [output[0], vote[selected_option], date, timestamp]
                    else:
                        writer.writerow(COL_NAMES)
                        attendance = [output[0], vote[selected_option], date, timestamp]
                    writer.writerow(attendance)
                speak("THANK YOU FOR PARTICIPATING IN THE ELECTIONS")
                running = False
                break

    video.release()
    cv2.destroyAllWindows()

# Create and start threads
gui_thread = Thread(target=create_gui)
video_thread = Thread(target=process_video)

gui_thread.start()
video_thread.start()

gui_thread.join()
video_thread.join()
