import pygame
from pygame.locals import *
from tkinter import *
from tkinter import messagebox


def play():


	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((500, 250))
	pygame.display.set_caption('Builder Buddies')
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			pygame.display.update()

	






#	play_window = Tk()
#	play_window.geometry("500x250")
#	play_window.title("Builder Buddies")
#	play_window.config(background="Grey")

#	old_window.destroy()

#	play_window.mainloop()

  




def ive():
     
    # Message box for icloud 
	def Cacc():
		messagebox.showinfo(title='Locating Account',
			                message='No account found in iCloud!')

    # Message box for Game Center
	def Gacc():
		messagebox.showinfo(title='Locating Account',
			                message='No account found in Game Center')


	def cancel():
		ive_window.destroy()




	ive_window = Tk()
	ive_window.geometry("500x250")
	ive_window.title("Builder Buddies")
	ive_window.config(background="Grey")


	label = Label(ive_window,
		          text="Restore Account",
		          font=('Arial',15,'bold'),
		          bg="Grey",
		          fg="White")
	label.pack()

	label = Label(ive_window,
		          text="Restore your account using one of these services.",
		          font=('Arial',15,'bold'),
		          bg="Grey",
		          fg="White")
	label.place(x=7,y=80)

	button = Button(ive_window,
		            text="iCloud",
		            relief=RAISED,
		            bd=3,
		            font=('Arial',15,'bold'),
		            bg="Grey",
		            fg="White",
		            command=Cacc,
		            padx=60,
		            pady=5)
	button.place(x=50,y=110)

	button = Button(ive_window,
		            text="Game Center",
		            relief=RAISED,
		            bd=3,
		            font=('Arial',15,'bold'),
		            bg="Grey",
		            fg="White",
		            padx=25,
		            pady=5,
		            command=Gacc)
	button.place(x=255,y=110)

	button = Button(ive_window,
		            text="Canel",
		            relief=RAISED,
		            bd=3,
		            font=('Arial',15,'bold'),
		            bg="Grey",
		            fg="White",
		            padx=60,
		            pady=5,
		            command=cancel,)
	button.place(x=155,y=167)

	ive_window.mainloop()





old_window = Tk()
old_window.geometry("500x250")
old_window.title("Builder Buddies")
old_window.config(background="Grey")


label = Label(old_window, 
	          text="BUILDER BUDDIES",
	          font=('Arial',20,'bold'),
	          bg='Grey',
	          fg='White')
label.pack(side=TOP)

label = Label(old_window,
	          text="Don Arifi LLC",
	          font=('Arial',12,'bold'),
	          bg="Grey",
	          fg="White",)
label.place(x=5,y=230)

label = Label(old_window,
	          text="v.1.0.0",
	          font=('Arial',12,'bold'),
	          bg="Grey",
	          fg="White",)
label.place(x=440,y=230)

button = Button(old_window,
	            text="Play",
	            font=('Arial',20,'bold'),
	            bg='Grey',
	            fg='White',
	            command=play,
	            padx=30,
	            relief=RAISED,
	            bd=5)
button.place(x=180,y=100)

ive_button = Button(old_window,
	                text="I've Played Before",
	                font=('Arial',7,'bold'),
	                pady=5,
	                bg='Grey',
	                command=ive,
	                fg='White')
ive_button.place(x=5,y=200)



old_window.mainloop()