from tkinter import *
from tkinter import messagebox
import time
import threading
from pygame import mixer
mixer.init()

root= Tk()
root.title("ALARM CLOCK")
root.geometry("650x450")


def th():
	t1 = threading.Thread(target=a, args=())
	t1.start()


def a():

	a = hr.get()
	if a == "":
		msg = messagebox.showerror('Invalid data','Please enter valid time')

	else:
		Alarmtime= a
		CurrentTime = time.strftime("%H:%M")

		while Alarmtime != CurrentTime:
			CurrentTime = time.strftime("%H:%M")
			
		if Alarmtime == CurrentTime:
			mixer.music.load('abcd.mp3')
			mixer.music.play()
			msg = messagebox.showinfo('It is time',f'{amsg.get()}')
			if msg == 'ok':
				mixer.music.stop()



header =Frame(root)
header.place(x=5,y=5)

head =Label(root,text="ALARM CLOCK",border=5,font=('Britannic',20),bg='black',fg='white')
head.pack(fill=X)

panel = Frame(root)
panel.place(x=5,y=70)

alpp = PhotoImage(file='alarm.png')

alp = Label(panel,image=alpp,bg='black',border=4)
alp.grid(rowspan=4,column=0,)

atime = Label(panel,text="Alarm Time \n(Hr:Min)",border=8,font=('Berlin Sans FB',18), fg = "black", bg = "lavender")
atime.grid(row=0,column=1,padx=10,pady=5)

hr = Entry(panel,font=('Berlin Sans FB',20),width=5,border=8)
hr.grid(row=0,column=2,padx=10,pady=5)


amessage = Label(panel,text="Message",font=('Berlin Sans FB',20),border=8, fg = "black", bg = "lavender")
amessage.grid(row=1,column=1,columnspan=2,padx=10,pady=5)

amsg = Entry(panel,font=('Berlin Sans FB',15),width=25,border=8)
amsg.grid(row=2,column=1,columnspan=2,padx=10,pady=5)


start = Button(panel,text="Start alarm",font=('Berlin Sans FB',20), border=6,fg = "black", bg = "lavender",command=th)
start.grid(row=3,column=1,columnspan=2,padx=10,pady=5)
root.mainloop()
