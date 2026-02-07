from tkinter import *
import random
import time

# Ball class
class Ball:
    # initiation function setup
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas # get a variavle for the canvas
        self.paddle = paddle # create a paddle variable in ball
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) # get a variable for the ball
        self.canvas.move(self.id, 245, 100) # move the ball
        starts = [-3, -2, 1, 1, 2, 3] # list of possible x starts
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height() # variable for current window height
        self.canvas_width = self.canvas.winfo_width() # variable for current window width
        self.hit_bottom = False # variable for hitting bottom
    
    # detect if ball and paddle touch
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id) # get current coords of paddle
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    # function to move the ball
    def draw(self):
        self.canvas.move(self.id, self.x, self.y) # move the ball
        pos = self.canvas.coords(self.id) # variable for current position of ball
        # if ball at top/bottom, change y direction
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        # if the ball hits the paddle, change y
        if self.hit_paddle(pos) == True:
            self.y = -3
        # if ball at sides, change x direction
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

# Paddle Class
class Paddle:
    # initilization function setup
    def __init__(self, canvas, color):
        self.canvas = canvas # get a variavle for the canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color) # get a variable for the paddle
        self.canvas.move(self.id, 200, 300) # move paddle to centre
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        # bind left/right functions to left/right arrows
        self.canvas.bind_all('<KeyPress-Left>', self.turnleft)
        self.canvas.bind_all('<KeyPress-Right>', self.turnright)
    
    # function to move paddle
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        # bounce back if on edge
        if pos[0] <= 0:
            self.x = 3
        elif pos[2] >= self.canvas_width:
            self.x = -3

    # functions to move left or right
    def turnleft(self, evt):
        self.x = -3
    def turnright(self, evt):
        self.x = 3

# Window Setup
tk = Tk() # create a window
tk.title("Paddle Bounce") # name the window
tk.resizable(0,0) # stop resizing

# Create background
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0, background='blue') # create a canvas
# put the canvas into the window
canvas.pack()
tk.update()

# Create a Paddle
paddle = Paddle(canvas, 'purple')
# Create a ball
ball = Ball(canvas, paddle, 'red')

# Keeps window open + constantly refeshing
while 1:
    # game lossing mechanic
    if ball.hit_bottom == False:
        ball.draw() # move ball
        paddle.draw() # allows paddle movement updates
    tk.update_idletasks() # update background tasks
    tk.update() # update the window
    time.sleep(0.01) # sleep for 2/100 of a second