from scheduler import *
from timing import *
from datetime import datetime, timedelta
import tkinter as tk

root = tk.Tk()
root.title('Automated School System [ASS]')
text1 = tk.Text(root, height=20, width=30)
photo = tk.PhotoImage(file='./bell.png')
text1.insert(tk.END, '\n')
text1.image_create(tk.END, image=photo)

text1.pack(side=tk.LEFT)

text2 = tk.Text(root, height=20, width=50)
scroll = tk.Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Segoe UI', 12, 'bold', 'italic'))
text2.tag_configure('big', font=('Segoe UI', 18, 'bold'))
text2.tag_configure('color',
                    foreground='#476042',
                    font=('Segoe UI', 12, 'bold'))
text2.tag_bind('follow',
               '<1>',
               lambda e, t=text2: t.insert(tk.END, "Not now, maybe later!"))
text2.insert(tk.END,'\nAutomated School System [ASS]\n', 'big')
quote = """
An Awesome project created by
JETS Club for the main purpose
of sacking the time keeper plus
to show how amazing Mr Bolu can
be.
xoxo
from the best club ever!!!
Beat this if you can!!!!
HaHaHaHaHaHa
*Evil Laughter*
"""
text2.insert(tk.END, quote, 'color')

text2.pack(side=tk.LEFT)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
root.mainloop()



#ct = assemblytime()
ct = assembly
#first period
currenttime = ct + timedelta(minutes=periodsch)
tim = datetime.now().time()
while(int(tim.strftime("%H%M%S")) != int(currenttime.strftime("%H%M%S"))):
    tim = datetime.now().time()
    if (int(tim.strftime("%H%M%S")) == int(currenttime.strftime("%H%M%S"))):
        break
period()

#second period
currenttime = currenttime + timedelta(minutes=periodsch)
tim = datetime.now().time()
while(int(tim.strftime("%H%M%S")) != int(currenttime.strftime("%H%M%S"))):
    tim = datetime.now().time()
    if (int(tim.strftime("%H%M%S")) == int(currenttime.strftime("%H%M%S"))):
        break
period()

#third period
currenttime = currenttime + timedelta(minutes=periodsch)
tim = datetime.now().time()
while(int(tim.strftime("%H%M%S")) != int(currenttime.strftime("%H%M%S"))):
    tim = datetime.now().time()
    if (int(tim.strftime("%H%M%S")) == int(currenttime.strftime("%H%M%S"))):
        break
period()

#tea break
currenttime = currenttime + timedelta(minutes=teabreak)
tim = datetime.now().time()
while(int(tim.strftime("%H%M%S")) != int(currenttime.strftime("%H%M%S"))):
    tim = datetime.now().time()
    if (int(tim.strftime("%H%M%S")) == int(currenttime.strftime("%H%M%S"))):
        break
teabreak()

#fourth period
currenttime = currenttime + timedelta(minutes=periodsch)
tim = datetime.now().time()
while(int(tim.strftime("%H%M%S")) != int(currenttime.strftime("%H%M%S"))):
    tim = datetime.now().time()
    if (int(tim.strftime("%H%M%S")) == int(currenttime.strftime("%H%M%S"))):
        break
period()

#fifth period
currenttime = currenttime + timedelta(minutes=periodsch)
tim = datetime.now().time()
while(int(tim.strftime("%H%M%S")) != int(currenttime.strftime("%H%M%S"))):
    tim = datetime.now().time()
    if (int(tim.strftime("%H%M%S")) == int(currenttime.strftime("%H%M%S"))):
        break
period()

#sixth period
currenttime = currenttime + timedelta(minutes=periodsch)
tim = datetime.now().time()
while(int(tim.strftime("%H%M%S")) != int(currenttime.strftime("%H%M%S"))):
    tim = datetime.now().time()
    if (int(tim.strftime("%H%M%S")) == int(currenttime.strftime("%H%M%S"))):
        break
period()

#long break
currenttime = currenttime + timedelta(minutes=longbreak)
tim = datetime.now().time()
while(int(tim.strftime("%H%M%S")) != int(currenttime.strftime("%H%M%S"))):
    tim = datetime.now().time()
    if (int(tim.strftime("%H%M%S")) == int(currenttime.strftime("%H%M%S"))):
        break
longbreak()

#seventh period
currenttime = currenttime + timedelta(minutes=periodsch)
tim = datetime.now().time()
while(int(tim.strftime("%H%M%S")) != int(currenttime.strftime("%H%M%S"))):
    tim = datetime.now().time()
    if (int(tim.strftime("%H%M%S")) == int(currenttime.strftime("%H%M%S"))):
        break
period()

#eight period
currenttime = currenttime + timedelta(minutes=periodsch)
tim = datetime.now().time()
while(int(tim.strftime("%H%M%S")) != int(currenttime.strftime("%H%M%S"))):
    tim = datetime.now().time()
    if (int(tim.strftime("%H%M%S")) == int(currenttime.strftime("%H%M%S"))):
        break
period()

#ext break
currenttime = currenttime + timedelta(minutes=extbreak)
tim = datetime.now().time()
while(int(tim.strftime("%H%M%S")) != int(currenttime.strftime("%H%M%S"))):
    tim = datetime.now().time()
    if (int(tim.strftime("%H%M%S")) == int(currenttime.strftime("%H%M%S"))):
        break
extbreak()

#Nineth period
currenttime = currenttime + timedelta(minutes=periodsch)
tim = datetime.now().time()
while(int(tim.strftime("%H%M%S")) != int(currenttime.strftime("%H%M%S"))):
    tim = datetime.now().time()
    if (int(tim.strftime("%H%M%S")) == int(currenttime.strftime("%H%M%S"))):
        break
period()

#tenth period
currenttime = currenttime + timedelta(minutes=periodsch)
tim = datetime.now().time()
while(int(tim.strftime("%H%M%S")) != int(currenttime.strftime("%H%M%S"))):
    tim = datetime.now().time()
    if (int(tim.strftime("%H%M%S")) == int(currenttime.strftime("%H%M%S"))):
        break
closetime()

