from tkinter import *
import random
import time

WIDTH = 800
HEIGHT = 600

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title("Drawing")
canvas.pack()


ball = canvas.create_oval(10, 10, 60, 60, fill="orange")
xspeed = 4
yspeed = 5

ball2 = canvas.create_oval(100, 100, 60, 60, fill="purple")
xspeed2 = 1
yspeed2 = 3

while True: 
    canvas.move(ball, xspeed, yspeed)
    canvas.move(ball2, xspeed2, yspeed2)
    pos = canvas.coords(ball)
    pos2 = canvas.coords(ball2)
    
    if pos[3] >= HEIGHT or pos[1] <= 0:
        yspeed = -yspeed

    if pos2[3] >= HEIGHT or pos2[1] <= 0:
        yspeed2 = -yspeed2

    if pos[2] >= WIDTH or pos[0] <= 0:
        xspeed = -xspeed

    if pos2[2] >= WIDTH or pos2[0] <= 0:
        xspeed2 = -xspeed2

    if pos[3] == pos2[3] or pos[1] == pos2[1]:
        yspeed = -yspeed
        yspeed2 = -yspeed2

    if pos[2] == pos2[2] or pos[0] == pos2[0]:
        xspeed = -xspeed
        xspeed2 = -xspeed2
        
    tk.update()
    time.sleep(0.01)

    
tk.mainloop()
