from tkinter import *
from PIL import ImageTk, Image
import ctypes

root = Tk()
img = Image.open("Images\\HomePage.png")
img = ImageTk.PhotoImage(img) #converted to format that tkinter understand 

panel = Label(root, image=img)
panel.pack(side="top", fill="both", expand="yes")

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
lt = [w, h]
a = str(lt[0]//2-480)
b= str(lt[1]//2-270)

root.title("THIS IS TITLE")
root.geometry("776x490+"+a+"+"+b) #widthxheight
root.resizable(0, 0) #width, height...  #0 = false, 1 = true		

def pressed():
	print("button pressed!")

# btn = Button(root, text="click me!", font = ("Agency FB",20), relief =FLAT, bd=0, borderwidth='0', bg="white", fg = "red", activeforeground ="green",activebackground = "white", command=pressed)
# btn.place(x=15,y=98)

predic = Button(root,text = "• Predict Heart Disease",font = ("Agency FB",20),relief = FLAT, bd = 0, borderwidth='0',bg="white",fg="#2C3A63",activebackground = "white",activeforeground = "#2C3A63",command=pressed)
predic.place(x=15,y = 98)

username = Text(root,height=2,width=31,bd=1,font = ("Arial Narrow",12),fg="#A73586")
username.place(x=15,y=200)
root.mainloop()
