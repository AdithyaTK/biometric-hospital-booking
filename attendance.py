import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3
from glob import glob

import show_attendance
import takeImage
import trainImage
import automaticAttedance

def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


haarcasecade_path = "C:\\Users\\ACER\\OneDrive\\Desktop\\test1\\haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "C:\\Users\\ACER\\OneDrive\\Desktop\\test1\\TrainingImageLabel\\Trainner.yml"
)
trainimage_path = "C:\\Users\\ACER\\OneDrive\\Desktop\\test1\\TrainingImage"
studentdetail_path = (
    "C:\\Users\\ACER\\OneDrive\\Desktop\\test1\StudentDetails\\studentdetails.csv"
)
attendance_path = "C:\\Users\\ACER\\OneDrive\\Desktop\\test1\\Attendance\\{sub}"


window = Tk()
window.title("AI Based Biometric Golden Ager Booking System")
window.geometry("1280x720")
window.configure(background="light blue")
img=ImageTk.PhotoImage(Image.open("1a.jpg"))
label=Label(image=img)
label.pack()


def del_sc1():
    sc1.destroy()


def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="black")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="yellow",
        bg="black",
        font=("times", 20, " bold "),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="yellow",
        bg="black",
        width=9,
        height=1,
        activebackground="Red",
        font=("times", 20, " bold "),
    ).place(x=110, y=50)


def testVal(inStr, acttyp):
    if acttyp == "1":  
        if not inStr.isdigit():
            return False
    return True


frame = LabelFrame(
    window,
    text='',
    bg='light blue',
    font=(20)
)
frame.pack(expand=True, fill=BOTH)
a = tk.Label(
    window,
    text="A Helping Hand for Elders",
    bg="white",
    fg="black",
    bd=10,
    font=("italic", 35),
)
a.pack()

ri = Image.open("UI_Image/plus.jpg")
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=100, y=270)

ai = Image.open("UI_Image/doctor.jfif")
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=980, y=270)

vi = Image.open("UI_Image/bookapp.jfif")
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v)
label3.image = v
label3.place(x=600, y=270)


def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take  Image..")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="black")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="black", relief=RIDGE, bd=10, font=("arial", 35))
    titl.pack(fill=X)
    titl = tk.Label(

        ImageUI, text="REGISTER YOUR FACE", bg="light blue", fg="black", font=("arial", 30),
    )
    titl.place(x=270, y=12)

    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="white",
        fg="black",
        bd=10,
        font=("arial", 24),
    )
    a.place(x=280, y=75)

    lbl1 = tk.Label(
        ImageUI,
        text="Patient ID",
        width=10,
        height=2,
        bg="White",
        fg="black",
        bd=5,
        font=("times new roman", 12),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        validate="key",
        bg="white",
        fg="black",
        font=("times", 25, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="white",
        fg="black",
        bd=5,
        font=("times new roman", 12),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="white",
        fg="black",
        font=("times", 25, "bold"),
    )
    txt2.place(x=250, y=200)
    lbl3 = tk.Label(
        ImageUI,
        text="Additional info",
        width=10,
        height=2,
        bg="white",
        fg="black",
        bd=5,
        font=("times new roman", 12),
    )
    lbl3.place(x=120, y=270)
    txt3 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="white",
        fg="black",
        font=("times", 25, "bold"),
    )
    txt3.place(x=250, y=270)
    

    lbl4 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        bg="white",
        fg="black",
        bd=5,
        font=("times new roman", 12),
    )
    lbl4.place(x=120, y=340)

    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="white",
        fg="black",
        font=("times", 12, "bold"),
    )
    message.place(x=250, y=340)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        from csv import DictWriter
        os.chdir(
        f"C:\\Users\\ACER\\OneDrive\\Desktop\\test1\\StudentDetails")
        filenames = glob(
        f"C:\\Users\\ACER\\OneDrive\\Desktop\\test1\\StudentDetails\\textbox.csv")
        headersCSV = ['ID','Detail']    
        l4 = txt3.get()
        dict={'ID':l1,'Detail':l4}
        print(l1)
        print(l4)
        with open('textbox.csv','a')as file1:
            dictwriter_object = DictWriter(file1, fieldnames=headersCSV)
            dictwriter_object.writerow(dict)
            file1.close()
        txt1.delete(0, "end")
        txt2.delete(0, "end")
        txt3.delete(0,"end")

    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=10,
        font=("times new roman", 18),
        bg="white",
        fg="black",
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=130, y=410)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("times new roman", 18),
        bg="white",
        fg="black",
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=360, y=410)



r = tk.Button(
    window,
    text="CREATE ACCOUNT",
    command=TakeImageUI,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="white",
    height=2,
    width=17,
)
r.place(x=100, y=520)


def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)


r = tk.Button(
    window,
    text="BOOK APPOINTMENT",
    command=automatic_attedance,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="white",
    height=2,
    width=17,
)
r.place(x=600, y=520)


def view_attendance():
    show_attendance.subjectchoose(text_to_speech)


r = tk.Button(
    window,
    text="DOCTOR LOGIN",
    command=view_attendance,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="white",
    height=2,
    width=17,
)
r.place(x=1000, y=520)

window.mainloop()
