from tkinter import *
from random import randint
from time import sleep
WIDTH = 800
HEIGHT = 800
CANVAS_MID_X = WIDTH/2
CANVAS_MID_Y = HEIGHT/2
SIDE = WIDTH/8
lastKnownCursor = [0,0]
root = Tk()
canvas = Canvas(root, bg="black", height=HEIGHT, width=WIDTH)
canvas.pack()

vertices = [
    [CANVAS_MID_X - SIDE/2, CANVAS_MID_Y - SIDE/2],
    [CANVAS_MID_X + SIDE/2, CANVAS_MID_Y - SIDE/2],
    [CANVAS_MID_X + SIDE/2, CANVAS_MID_Y + SIDE/2],
    [CANVAS_MID_X - SIDE/2, CANVAS_MID_Y + SIDE/2],
]

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle_arc = _create_circle_arc

def mouseCO(event):
    global center,lastKnownCursor
    if event == "DIRECTION":
        x = lastKnownCursor[0]
        y = lastKnownCursor[1]
    else:
        x, y = event.x, event.y
        lastKnownCursor = [x,y]

    updatePosition([x,y])
        

def updatePosition(center):
    moved_points = []
    moved_points.append([center[0]-SIDE,center[1]-SIDE])
    moved_points.append([center[0]-SIDE,center[1]+SIDE])
    moved_points.append([center[0]+SIDE,center[1]+SIDE])
    moved_points.append([center[0]+SIDE,center[1]-SIDE])
    canvas.create_circle(center[0], center[1], SIDE, fill="blue", outline="#DDD", width=4)
    root.update()

def move(letter):
    global center,lastKnownCursor
    if letter == "w":
        center = [center[0],center[1]-10]
    elif letter == "s":
        center = [center[0],center[1]+10]
    elif letter == "a":
        center = [center[0]-10,center[1]]
    elif letter == "d":
        center = [center[0]+10,center[1]]

    updateDirection("DIRECTION")

        
center = (CANVAS_MID_X, CANVAS_MID_Y)
center = (400.0,400.0)

root.bind('<Motion>', mouseCO)
root.bind('w', lambda x: move('w'))
root.bind('s', lambda x: move('s'))
root.bind('a', lambda x: move('a'))
root.bind('d', lambda x: move('d'))

#root.update()
#angle=180
#while True:
#    angle = input("Enter Angle\n")
#    print(angle)
#    new_square = rotate(vertices, float(angle), center)
#    draw_square(new_square)
#    root.update()

mainloop()
