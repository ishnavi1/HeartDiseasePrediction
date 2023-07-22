from tkinter import * # for GUI designing...
import ctypes
from tkinter.tix import * 
from PIL import ImageTk, Image #python image library
import tkinter.messagebox as tkMessageBox
import sqlite3 # for storing the data of contact us in database

def HomePage():
	global cntct,about

	try:
		cntct.destroy()
	except:
		pass
	try:
		about.destroy()
	except:
		pass

	window = Tk()
	img = Image.open("Images\\HomePage.png")
	img = ImageTk.PhotoImage(img)
	panel = Label(window, image=img)
	panel.pack(side="top", fill="both", expand="yes")

	user32 = ctypes.windll.user32
	user32.SetProcessDPIAware()
	[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
	lt = [w, h]
	a = str(lt[0]//2-480)
	b= str(lt[1]//2-270)

	window.title("HOME - Heart Disease Prediction")
	window.geometry("776x490+"+a+"+"+b)
	window.resizable(0,0)

	def predict():
		try:
			window.destroy()
		except Exception as e:
			print(e)
		import heart_disease_prediction
		HomePage()


	# EXIT . . . 
	def exit():
		global cntct,about
		result = tkMessageBox.askquestion("Heart Disease Prediction", "Are you sure you want to exit?", icon= "warning")
		if result == 'yes':
			try:
				window.destroy()
			except:
				pass
			try:
				cntct.destroy()
			except:
				pass
			try:
				about.destroy()
			except:
				pass

	def contactUs():
		global chckbal,cntct,about
		try:
			window.destroy()
		except:
			pass
		try:
			about.destroy()
		except:
			pass
		
		cntct = Tk()
		img = Image.open("Images\\contactus.png")
		img = ImageTk.PhotoImage(img)
		panel = Label(cntct, image=img)
		panel.pack(side="top", fill="both", expand="yes")

		user32 = ctypes.windll.user32
		user32.SetProcessDPIAware()
		[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
		lt = [w, h]
		a = str(lt[0]//2-480)
		b= str(lt[1]//2-270)

		cntct.title("CONTACT US - Heart Disease Prediction")
		cntct.geometry("776x490+"+a+"+"+b)
		cntct.resizable(0,0)


		home = Button(cntct,text = "Home",font = ("Agency FB",16,"bold"),relief = FLAT, bd = 0, borderwidth='0',bg="white",fg="#A73586",activebackground = "white",activeforeground = "#A73586",command=HomePage)
		home.place(x=175,y = 40)
		aboutus = Button(cntct,text = "About Us",font = ("Agency FB",16,"bold"),relief = FLAT, bd = 0, borderwidth='0',bg="white",fg="#A73586",activebackground = "white",activeforeground = "#A73586",command=aboutUS)
		aboutus.place(x=245,y = 40)
		exitbtn = Button(cntct,text = "Exit",font = ("Agency FB",16,"bold"),relief = FLAT, bd = 0, borderwidth='0',bg="white",fg="#A73586",activebackground = "white",activeforeground = "#A73586",command=exit)
		exitbtn.place(x=345,y = 40)

		username = Text(cntct,height=1,width=31,bd=0,font = ("Arial Narrow",12),fg="#A73586")
		username.place(x=498,y=234)
		email = Text(cntct,height=1,width=31,bd=0,font = ("Arial Narrow",12),fg="#A73586")
		email.place(x=498,y=278)
		message = Text(cntct,height=4,width=35,bd=0,font = ("Arial Narrow",12),fg="#A73586")
		message.place(x=467,y=345)

		def submit():
			
			name1=username.get(1.0,END)
			email1=email.get(1.0,END)
			message1=message.get(1.0,END)
			conn=sqlite3.connect('contactus.db')
			cursor=conn.cursor()
			cursor.execute('CREATE TABLE IF NOT EXISTS CONTACTUS (Fullname TEXT,Email TEXT, Message TEXT)')
			cursor.execute('INSERT INTO CONTACTUS (Fullname,Email,Message) VALUES(?,?,?)',(name1,email1,message1))
			conn.commit()
			result = tkMessageBox.showinfo("Heart Disease Prediction", "Message sent succesfully! wait for our email. thank you!")

		sendbtn = Button(cntct,text = "SEND",font = ("Arial Narrow",12,"bold"),relief="ridge",bd=1, borderwidth='3',bg="#A73586",fg="#F9FAFB",activebackground = "#CD70B2",activeforeground = "#F9FAFB",command=submit)
		sendbtn.place(x=570,y=445)
		cntct.mainloop()

	def aboutUS():
		global cntct,about
		try:
			window.destroy()
		except:
			pass
		try:
			cntct.destroy()
		except:
			pass

		about = Tk()
		img = Image.open("Images\\aboutus.png")
		img = ImageTk.PhotoImage(img)
		panel = Label(about, image=img)
		panel.pack(side="top", fill="both", expand="yes")

		user32 = ctypes.windll.user32
		user32.SetProcessDPIAware()
		[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
		lt = [w, h]
		a = str(lt[0]//2-480)
		b= str(lt[1]//2-270)

		about.title("ABOUT US - Heart Disease Prediction")
		about.geometry("776x490+"+a+"+"+b)
		about.resizable(0,0)


		home = Button(about,text = "Home",font = ("Agency FB",16,"bold"),relief = FLAT, bd = 0, borderwidth='0',bg="white",fg="#E85B5A",activebackground = "white",activeforeground = "#E85B5A",command=HomePage)
		home.place(x=175,y = 40)
		contactus = Button(about,text = "Contact Us",font = ("Agency FB",16,"bold"),relief = FLAT, bd = 0, borderwidth='0',bg="white",fg="#E85B5A",activebackground = "white",activeforeground = "#E85B5A",command=contactUs)
		contactus.place(x=240,y = 40)
		exitbtn = Button(about,text = "Exit",font = ("Agency FB",16,"bold"),relief = FLAT, bd = 0, borderwidth='0',bg="white",fg="#E85B5A",activebackground = "white",activeforeground = "#E85B5A",command=exit)
		exitbtn.place(x=335,y = 40)

		about.mainloop()



	''' USER OPTIONS '''
	predic = Button(window,text = "• Predict Heart Disease",font = ("Agency FB",20),relief = FLAT, bd = 0, borderwidth='0',bg="white",fg="#2C3A63",activebackground = "white",activeforeground = "#2C3A63",command=predict)
	predic.place(x=15,y = 98)
	about = Button(window,text = "• About the Project",font = ("Agency FB",20),relief = FLAT, bd = 0, borderwidth='0',bg="white",fg="#2C3A63",activebackground = "white",activeforeground = "#2C3A63",command=aboutUS)
	about.place(x=15,y = 158)
	contct = Button(window,text = "• Get in Touch",font = ("Agency FB",20),relief = FLAT, bd = 0, borderwidth='0',bg="white",fg="#2C3A63",activebackground = "white",activeforeground = "#2C3A63",command=contactUs)
	contct.place(x=15,y = 218)
	exi = Button(window,text = "• Leave",font = ("Agency FB",20),relief = FLAT, bd = 0, borderwidth='0',bg="white",fg="#2C3A63",activebackground = "white",activeforeground = "#2C3A63",command=exit)
	exi.place(x=15,y = 278)
	window.mainloop()

HomePage()