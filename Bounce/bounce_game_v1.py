from tkinter import *
import random
import time

# Ball class
class Ball:
    # initiation function setup
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas # get a variable for the canvas
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
            self.y = -3 - (abs(paddle.x)/2)
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

# Score Class
class Score:
    def __init__(self, canvas, score):
        self.canvas = canvas
        self.score = score
        self.display = self.canvas.create_text(0, 0, text=str(self.score), font=('AtkinsonHyperlegible', '12'))
        self.canvas.move(self.display, 10, 10) # move text

    def updateScore(self):
        pos = ball.canvas.coords(ball.id) # variable for current position of ball
        if ball.hit_paddle(pos) == True:
            self.score = self.score + 1
        self.canvas.itemconfig(self.display, text=str(self.score))


# Game Over Class
class GameOver:
    def __init__(self, canvas):
        self.canvas = canvas # set variable for canvas
        self.text = self.canvas.create_text(0, 0, text="GAME OVER!", font=('AtkinsonHyperlegible', '15')) # create game over text.
        self.canvas.move(self.text, 250, 200) # move text to centre
        self.canvas.itemconfig(self.text, state=HIDDEN) # hide text
    
    def endgame(self, isOver):
        while isOver == False:
            self.canvas.itemconfig(self.text, state=HIDDEN)  # hide text while game is playing
        else:
            time.sleep(0.5) # sleep for 1/2 a second
            self.canvas.itemconfig(self.text, state=NORMAL) # show game over text

# Game Start Class
class GameStart:
    def __init__(self, canvas):
        self.canvas = canvas
        self.playing = False # variable for if the game has started
        self.canvas.bind_all('<Return>', self.startgame) # bind startgame function to the enter key
    
    # function to start the game
    def startgame(self, evt):
         self.playing = True

# Window class
class Window:
    def startup(self):
        # Window Setup
        self.tk = Tk() # create a window
        self.tk.title("Paddle Bounce") # name the window
        self.tk.resizable(0,0) # stop resizing
        # Create background
        self.canvas = Canvas(self.tk, width=500, height=400, bd=0, highlightthickness=0, background='blue') # create a canvas
        # put the canvas into the window
        self.canvas.pack()
        self.tk.update()

    # Update entire window
    def update_window(self):
        self.tk.update_idletasks() # update background tasks
        self.tk.update() # update the window

# Create window
window = Window()
window.startup()

# Create Game Start
gameStart = GameStart(window.canvas)
# Create a Paddle
paddle = Paddle(window.canvas, 'purple')
# Create a ball
ball = Ball(window.canvas, paddle, 'red')
#Create Score
score = Score(window.canvas, 0)
# Create Game Over
gameEnd = GameOver(window.canvas)


# Keeps window open + constantly refeshing
while 1:
    while gameStart.playing == False:
        window.update_window() # Update entire window
        time.sleep(0.01) # sleep for 1/100 of a second
    score.updateScore()
    while ball.hit_bottom == False:
        paddle.draw() # allows paddle movement updates
        ball.draw() # move ball
        score.updateScore() # Update Score
        window.update_window() # Update entire window
        time.sleep(0.01) # pause for 1/1000 of a second
    gameEnd.endgame(ball.hit_bottom) # Checks Game Ending
    window.update_window() # Update entire window
    time.sleep(0.01) # sleep for 1/100 of a second