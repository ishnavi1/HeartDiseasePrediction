#### --------------------------------------- IMPORTING MODULES ---------------------------------------- ####
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import ctypes
import pandas as pd
import tkinter.messagebox as tkMessageBox
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import os,PIL
from tkinter import messagebox
import re

global window
def heart():
    global window
    def submit():
        try:
            x = [3,6,7]
            y = ['male','female']
            z = ['y','n']
            if fbs.get()=='' or gen.get()==''or eia.get()=='':
                warning = Label(canvas, text="***Please Fill All The Required Fields***", font=('arial', 12,'bold'), fg="yellow", bg="firebrick3", bd=10)
                warning.place(x = 30,y = 405)
                warning.after(2500, lambda: warning.destroy())
            elif age.get()<=0 :                        
                warning = Label(canvas, text="***Age Must Not Be Zero***", font=('arial', 12,'bold'), fg="yellow", bg="firebrick3", bd=10)
                warning.place(x = 30,y = 405)
                warning.after(2500, lambda: warning.destroy())
                
            elif cp.get()<0 or cp.get()>3:                        
                warning = Label(canvas, text="***Chest Pain Level Must Be Between 0 to 3***", font=('arial', 12,'bold'), fg="yellow", bg="firebrick3", bd=10)
                warning.place(x = 30,y = 405)
                warning.after(2500, lambda: warning.destroy())
            
            elif tha.get() not in x:                        
                warning = Label(canvas, text="***Thalassemia Must Be 3,6 or 7***", font=('arial', 12,'bold'), fg="yellow", bg="firebrick3", bd=10)
                warning.place(x = 30,y = 405)
                warning.after(2500, lambda: warning.destroy())
            elif (gen.get()).lower() not in y:                        
                warning = Label(canvas, text="***Unidentified input in Gender field***", font=('arial', 12,'bold'), fg="yellow", bg="firebrick3", bd=10)
                warning.place(x = 30,y = 405)
                warning.after(2500, lambda: warning.destroy())
            elif (fbs.get()).lower() not in z:                        
                warning = Label(canvas, text="Unidentified input in Fasting Blood Pressure field***", font=('arial', 12,'bold'), fg="yellow", bg="firebrick3", bd=10)
                warning.place(x = 30,y = 405)
                warning.after(2500, lambda: warning.destroy())
            elif (eia.get()).lower() not in z:                        
                warning = Label(canvas, text="Unidentified input in Excercise Indused Angina field***", font=('arial', 12,'bold'), fg="yellow", bg="firebrick3", bd=10)
                warning.place(x = 30,y = 405)
                warning.after(2500, lambda: warning.destroy())
            else:
                df = pd.read_csv('heart.csv')
                data = df.values
                X = data[:, :-1]
                Y = data[:, -1:]
                value = ''
                if (gen.get()).lower()=='male':
                    ge = 1
                elif (gen.get()).lower()=='female':
                    ge = 0
                if (fbs.get()).lower()=='y':
                    fb = 1
                elif (fbs.get()).lower()=='n':
                    fb = 0
                if (eia.get()).lower()=='y':
                    ei = 1
                elif (eia.get()).lower()=='n':
                    ei = 0                              
                ag = age.get()
                sex = ge
                chp = cp.get()
                trestbps = rbp.get()
                chl = chol.get()
                fbos = fb
                restecg = res.get()
                thalach = mha.get()
                exang = ei
                oldpeak = st.get()
                slope = slst.get()
                ca = mv.get()
                thal = tha.get()

                user_data = np.array((ag,sex,chp, trestbps, chl,  fbos, restecg, thalach, exang,oldpeak,slope, ca, thal)).reshape(1, 13)
                rf = RandomForestClassifier(n_estimators=16,criterion='entropy', max_depth=9)
                rf.fit(np.nan_to_num(X), Y.ravel())
                rf.score(np.nan_to_num(X), Y)
                predictions = rf.predict(user_data)

                if int(predictions[0]) == 1:
                        warning = Label(canvas, text="Result : Positive", font=('arial', 12,'bold'), fg="black", bg="firebrick3", bd=10)
                        warning.place(x = 30,y = 405)
                        warning.after(4500, lambda: warning.destroy())
                        
                elif int(predictions[0]) == 0:
                        warning = Label(canvas, text="Result : Negative", font=('arial', 12,'bold'), fg="black", bg="firebrick3", bd=10)
                        warning.place(x = 30,y = 405)
                        warning.after(4500, lambda: warning.destroy())
                        
        except:
                warning = Label(canvas, text="Some Unknown Error Has Occoured Please Try Again", font=('arial', 12,'bold'), fg="yellow", bg="firebrick3", bd=10)
                warning.place(x = 30,y = 405)
                warning.after(2500, lambda: warning.destroy())
    
    window = Tk()

    window.resizable(0,0)

    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    lt = [w, h]
    a = str(lt[0]//2-446)
    b= str(lt[1]//2-383)

    window.geometry("892x710+"+a+"+"+b)
    window.title('HeartDiseasePrediction')

    img = Image.open(r"Images/bg.jpg")
    img = ImageTk.PhotoImage(img)
    panel = Label(window, image=img)
    panel.pack(side="top", fill="both", expand="yes")

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    age = IntVar()
    gen = StringVar()
    cp = IntVar()
    rbp = DoubleVar()
    chol = DoubleVar()
    fbs = StringVar()
    res = DoubleVar()
    mha = DoubleVar()
    eia = StringVar()
    st = DoubleVar()
    slst = DoubleVar()
    mv = IntVar()
    tha = IntVar()     

    canvas = Canvas(window, bg="firebrick3", height=457, width=888)
    canvas.place(x=0,y=249)

    agel = Label(canvas, text="Age :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    agel.place(x = 30,y = 2)

    agee = Entry(canvas, textvariable=age, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    agee.place(x=465, y=11)

    genl = Label(canvas, text="Gender :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    genl.place(x = 30,y = 31)

    gene = Entry(canvas, textvariable=gen, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    gene.place(x=465, y=40)

    cpl = Label(canvas, text="Chest Pain Level (0 to 3) :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    cpl.place(x = 30,y = 60)

    cpe = Entry(canvas, textvariable=cp, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    cpe.place(x=465, y=69)

    rbpl = Label(canvas, text="Resting Blood Pressure(In mm Hg) :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    rbpl.place(x = 30,y = 89)

    rbpe = Entry(canvas, textvariable=rbp, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    rbpe.place(x=465, y=98)

    rbpl = Label(canvas, text="Resting Blood Pressure(In mm Hg) :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    rbpl.place(x = 30,y = 89)

    rbpe = Entry(canvas, textvariable=rbp, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    rbpe.place(x=465, y=98)

    lchol = Label(canvas, text="Cholesterol In mg/dl  :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    lchol.place(x = 30,y = 118)

    echol = Entry(canvas, textvariable=chol, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    echol.place(x=465, y=127)

    lfbs = Label(canvas, text="Fasting Blood Suger>120 mg/dl  (Y/N) :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    lfbs.place(x = 30,y = 147)

    efbs = Entry(canvas, textvariable=fbs, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    efbs.place(x=465, y=156)

    lres = Label(canvas, text="Resting Electrocardiography Result :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    lres.place(x = 30,y = 176)

    eres = Entry(canvas, textvariable=res, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    eres.place(x=465, y=185)

    lmha = Label(canvas, text="Maximum Heart Rate Achived :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    lmha.place(x = 30,y = 205)

    emha = Entry(canvas, textvariable=mha, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    emha.place(x=465, y=214)

    leia = Label(canvas, text="Excercise Indused Angina(Y/N) :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    leia.place(x = 30,y = 234)

    leiae = Entry(canvas, textvariable=eia, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    leiae.place(x=465, y=243)

    stl = Label(canvas, text="ST Depression Induced By Exercise Relative To Rest :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    stl.place(x = 30,y = 263)

    ste = Entry(canvas, textvariable=st, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    ste.place(x=465, y=272)

    sl = Label(canvas, text="The Slope Of The Peak Exercise ST Segment :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    sl.place(x = 30,y = 292)

    se = Entry(canvas, textvariable=slst, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    se.place(x=465, y=301)

    lmv = Label(canvas, text="Number Of Major Vessels Colored By Flourosopy :", font=('arial', 12,'bold'), fg="white", bg="firebrick3", bd=10)
    lmv.place(x = 30,y = 321)

    lmve = Entry(canvas, textvariable=mv, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    lmve.place(x=465, y=330)

    ltha = Label(canvas, text='A Blood Disorder Called Thalassemia :', font=('arial', 12,'bold'), fg="white", bg="firebrick3",bd=10)
    ltha.place(x = 30,y = 350)
    ltha = Label(canvas, text='  (3=Normal, 6 = Fixed Defect, 7 = Reversable Defect)',font=('arial', 12,'bold'), fg="white", bg="firebrick3")
    ltha.place(x = 30,y = 379)
    etha = Entry(canvas, textvariable=tha, font=('arial', 12,'bold'), width=45, bg="white", fg = 'firebrick3')
    etha.place(x=465, y=359)

    bh = Button(canvas, text="Analyze", fg="white", bg="firebrick3", width = 36,
                font=("Calibri", "16",'bold'),command=submit)
    bh.place(x=467, y=390)

    window.mainloop()
heart()
