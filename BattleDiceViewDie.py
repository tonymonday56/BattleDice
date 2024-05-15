#warviewimage.py

from tkinter import *
from PIL import ImageTk, Image
from BattleDice import p1_roll

#This creates the main window of an application
window = Tk()
window.title("Battle Dice")
window.geometry("650x675")
window.configure(bg='#310ff0')

path = "C:\\Projects\\BattleDice"

def next_hand():
    print('Next Hand')

def view_game():
    print('View Game')

def last_hand():
    print('Last Hand')

def speed_controller():
    '''
    5 levels of speed being controlled.
    
	.Hyperspeed
	.Fast
	.Medium
	.Slow
	.Snailspeed
    '''
    global speed 
    



path1 = "C:\\Projects\\BattleDice\\images\\" + str(p1_roll.get("p1_die1")) + ".jpg"
path2 = "C:\\Projects\\BattleDice\\images\\" + str(p1_roll.get("pi_die2")) + ".jpg"
path3 = "C:\\Projects\\BattleDice\\images\\" + str(p1_roll.get("pi_die3")) + ".jpg"
path4 = "C:\\Projects\\BattleDice\\images\\" + str(p1_roll.get("p1_die4")) + ".jpg"
path5 = "C:\\Projects\\BattleDice\\images\\" + str(p1_roll.get("p1_die5")) + ".jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img1 = ImageTk.PhotoImage(Image.open(path1))
img2 = ImageTk.PhotoImage(Image.open(path2))
img3 = ImageTk.PhotoImage(Image.open(path3))
img4 = ImageTk.PhotoImage(Image.open(path4))
img5 = ImageTk.PhotoImage(Image.open(path5))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
label = Label(window, text='Player1 Cards', bg='#310ff0', fg='yellow',  borderwidth=0, relief='solid', font=('bold', 14))
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)


label = Label(window, borderwidth=15, background='#8ecae9', relief="raised", image=img1)
label.image=img1
label.grid(row=1, column=0, padx=20, pady=20)


label = Label(window, borderwidth=15, background='#8ecae9', relief="raised", image=img2)
label.image=img2
label.grid(row=1, column=1, pady=20, padx=20)

label = Label(window, text='Player2 Cards', bg='#310ff0', fg='yellow', borderwidth=0, relief='solid', font=('bold', 14))
label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


label = Label(window, borderwidth=15, background='#1ba2e8', relief="raised",  image=img3)
label.image=img3
label.grid(row=3, column=0, pady=20, padx=20)

label = Label(window, borderwidth=15, background='#1ba2e8', relief="raised",  image=img4)
label.image=img4
label.grid(row=3, column=1, pady=20, padx=20)

add_btn = Button(window, bg='#00ff96', fg='#5400ff', text='Next Hand', width=10, height=2, borderwidth=15, font=('bold', 12), relief=RAISED, command=next_hand, pady=0, padx=0)
add_btn.grid(row=1, column=2)

add_btn = Button(window, bg='#00ff96', fg='#5400ff', text='Last Hand', width=10, height=2, borderwidth=15, font=('bold', 12), relief=RAISED, command=last_hand, pady=0, padx=0)
add_btn.grid(row=2, column=2)

add_btn = Button(window, bg='#00ff96', fg='#5400ff', text='View Game', width=10, height=2, borderwidth=15, font=('bold', 12), relief=RAISED, command=view_game, pady=0, padx=0)
add_btn.grid(row=3, column=2)

add_btn = Button(window, bg='#00ff96', fg='#5400ff', text='Speed Controller', width=10, height=2, borderwidth=15, font=('bold', 12), relief=RAISED, command=speed_controller, pady=0, padx=0, command=next_hand, pady=0, padx=0)
add_btn.grid(row=4, column=2)


#The Pack geometry manager packs widgets in rows or columns.
# panel.pack(side = "bottom", fill = "both", expand = "yes")

#Start the GUI
window.mainloop()