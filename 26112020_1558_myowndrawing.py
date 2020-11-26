from tkinter import *
import random
import time

WIDTH=400
HEIGHT=500

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("My Drawing")
canvas.pack()


box = canvas.create_rectangle(100, 100, 250, 250, fill="red")
xspeed = 4
yspeed = 5

while True:
    canvas.move(box, xspeed, yspeed)
    pos = canvas.coords(box)
    if pos[3] >= HEIGHT or pos[1] <= 0:
        yspeed = -yspeed
    if pos[2] >= WIDTH or pos[0] <= 0:
        xspeed = -xspeed
    tk.update()
    time.sleep(00.1)

canvas.mainloop()
