import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.ttk as tkk
import tkinter.font as font
from glob import glob


haarcasecade_path = "C:\\Users\\ACER\\OneDrive\\Desktop\\test1\\haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "C:\\Users\\ACER\\OneDrive\\Desktop\\test1\\TrainingImageLabel\\Trainner.yml"
)
trainimage_path = "C:\\Users\\ACER\\OneDrive\\Desktop\\test1\\TrainingImage"
studentdetail_path = (
    "C:\\Users\\ACER\\OneDrive\\Desktop\\test1\StudentDetails\\studentdetails.csv"
)
attendance_path = "C:\\Users\\ACER\\OneDrive\\Desktop\\test1\\Attendance\\{sub}"

def subjectChoose(text_to_speech):
    def FillAttendance():
        sub = tx.get()
        now = time.time()
        future = now + 20
        print(now)
        print(future)
        if sub == "":
            t = "Please enter the department to be booked!!!"
            text_to_speech(t)
        else:
            try:
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                try:
                    recognizer.read(trainimagelabel_path)
                except:
                    e = "Model not found,please train model"
                    Notifica.configure(
                        text=e,
                        bg="black",
                        fg="yellow",
                        width=33,
                        font=("times", 15, "bold"),
                    )
                    Notifica.place(x=20, y=250)
                    text_to_speech(e)
                facecasCade = cv2.CascadeClassifier(haarcasecade_path)
                df = pd.read_csv(studentdetail_path)
                cam = cv2.VideoCapture(0)
                font = cv2.FONT_HERSHEY_SIMPLEX
                col_names = ["Enrollment", "Name"]
                attendance = pd.DataFrame(columns=col_names)
                while True:
                    ___, im = cam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = facecasCade.detectMultiScale(gray, 1.2, 5)
                    for (x, y, w, h) in faces:
                        global Id
                        Id, conf = recognizer.predict(gray[y : y + h, x : x + w])
                        if conf < 70:
                            print(conf)
                            global Subject
                            global aa
                            global timeStamp
                            Subject = tx.get()
                            ts = time.time()
                            aa = df.loc[df["Enrollment"] == Id]["Name"].values
                            print(Id)
                            global tt
                            tt = str(Id) + "-" + aa
                            attendance.loc[len(attendance)] = [
                                Id,
                                aa,
                            ]
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 4)
                            cv2.putText(
                                im, str(tt), (x + h, y), font, 1, (255, 255, 0,), 4
                            )
                        else:
                            Id = "Unknown"
                            tt = str(Id)
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                            cv2.putText(
                                im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4
                            )
                    if time.time() > future:
                        break

                    attendance = attendance.drop_duplicates(
                        ["Enrollment"], keep="first"
                    )
                    cv2.imshow("Filling ...", im)
                    key = cv2.waitKey(30) & 0xFF
                    if key == 27:
                        break

                ts = time.time()
                print(aa)
                Hour, Minute, Second = timeStamp.split(":")
                path = os.path.join(attendance_path, Subject)
                fileName = (
                    f"{path}/"
                    + Subject
                    + ".csv"
                )
                attendance = attendance.drop_duplicates(["Enrollment"], keep="first")
                print(attendance)
                attendance.to_csv(fileName, index=False)

                cam.release()
                cv2.destroyAllWindows()
                import tkinter

                root = tkinter.Tk()
                cs = os.path.join(path, fileName)
                print(cs)
                with open(cs, newline="") as file:
                    reader = csv.reader(file)
                    r = 0

                    for col in reader:
                        c = 0
                        for row in col:

                            label = tkinter.Label(
                                root,
                                width=10,
                                height=1,
                                fg="yellow",
                                font=("times", 15, " bold "),
                                bg="black",
                                text=row,
                                relief=tkinter.RIDGE,
                            )
                            label.grid(row=r, column=c)
                            c += 1
                        r += 1
                root.mainloop()
                print(attendance)
            except:
                f = "Successfully Registered"
                print("hellllooooooooooooo")
                print(Subject)
                filename1=str(Subject)+".csv"
                print(filename1)
                os.chdir(
                f"C:\\Users\\ACER\\OneDrive\\Desktop\\test1\\StudentDetails")
                records = {}
                with open('textbox.csv') as file1obj:
                    reader = csv.reader(file1obj)
                    next(reader,None)
                    for row in reader:
                        try:
                            records[int(row[0])]=row[1:]
                        except:
                            pass
                print(records[Id])
                os.chdir(
                f"C:\\Users\\ACER\\OneDrive\\Desktop\\test1\\Attendance\\{Subject}")
                filenames = glob(
                f"C:\\Users\\ACER\\OneDrive\\Desktop\\test1\\Attendance\\{Subject}\\{Subject}*.csv")
                headersCSV = ['ID','NAME','Detail']    
                print(filenames)
                text_to_speech(f)
                dict={'ID':Id,'NAME':aa,'Detail':records[Id]}
                with open(filename1,'a')as file_obj:
                    dictwriter_object = csv.DictWriter(file_obj, fieldnames=headersCSV)
                    dictwriter_object.writerow(dict)
                    file_obj.close()

                cv2.destroyAllWindows()

    subject = Tk()
    subject.title("Booking")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="black")
    titl = tk.Label(subject, bg="black", relief=RIDGE, bd=10, font=("arial", 30))
    titl.pack(fill=X)
    titl = tk.Label(
        subject,
        text="Choose Department",
        bg="white",
        fg="black",
        font=("arial", 25),
    )
    titl.place(x=160, y=12)
    Notifica = tk.Label(
        subject,
        text="Attendance filled Successfully",
        bg="yellow",
        fg="black",
        width=33,
        height=2,
        font=("times", 15, "bold"),
    )

    def Attf():
        sub = tx.get()
        if sub == "":
            t = "Please enter the department name!!!"
            text_to_speech(t)
        else:
            os.startfile(
                f"C:\\Users\\ACER\\OneDrive\\Desktop\\test1\\Attendance\\{sub}"
            )

    attf = tk.Button(
        subject,
        text="Check Sheets",
        command=Attf,
        bd=7,
        font=("times new roman", 15),
        bg="white",
        fg="black",
        height=2,
        width=10,
        relief=RIDGE,
    )
    attf.place(x=360, y=170)

    sub = tk.Label(
        subject,
        text="Enter Department",
        width=10,
        height=2,
        bg="white",
        fg="black",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 15),
    )
    sub.place(x=50, y=100)

    tx = tk.Entry(
        subject,
        width=15,
        bd=5,
        bg="white",
        fg="black",
        relief=RIDGE,
        font=("times", 30, "bold"),
    )
    tx.place(x=190, y=100)

    fill_a = tk.Button(
        subject,
        text="Book Appoinment",
        command=FillAttendance,
        bd=7,
        font=("times new roman", 15),
        bg="white",
        fg="black",
        height=2,
        width=12,
        relief=RIDGE,
    )
    fill_a.place(x=195, y=170)
    subject.mainloop()
