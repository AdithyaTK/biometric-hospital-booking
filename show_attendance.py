import pandas as pd
from glob import glob
import os
import tkinter
import csv
import tkinter as tk
from tkinter import *

def subjectchoose(text_to_speech):
    subject = Tk()
    subject.title("Doctor Login")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="black")
    titl = tk.Label(subject, bg="black", relief=RIDGE, bd=10, font=("arial", 30))
    titl.pack(fill=X)
    titl = tk.Label(
        subject,
        text="ENTER YOUR DEPARTMENT",
        bg="white",
        fg="black",
        font=("arial", 25),
    )
    titl.place(x=100, y=12)
    def Attf():
        sub = tx.get()
        if sub == "":
            t="Please enter the department name!!!"
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
        text="Specialization:",
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
    subject.mainloop()