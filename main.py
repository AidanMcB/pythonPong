import turtle 
import os 

game_screen = turtle.Screen()
game_screen.title("Pong")
game_screen.bgcolor("black")
game_screen.setup(width=800, height=600)
game_screen.tracer(0)                        #stops the game_screen from updating

# Player 1
paddle_1 = turtle.Turtle()                          #a turtle object for our paddle
paddle_1.speed(0)                                   #the speed of animation, not the speed it moves,
paddle_1.shape("square")                            # sets the speed to the maximum possible speed
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)    #change size from square to rectangle     
paddle_1.penup()
paddle_1.goto(-350,0)                               #starting coordinates x and y

# Player 2
paddle_2 = turtle.Turtle()                 
paddle_2.speed(0)                                  
paddle_2.shape("square")                               
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)    
paddle_2.penup()
paddle_2.goto(350,0)                               #player 2 aligns on the right side of screen            

# Ball
ball = turtle.Turtle()                 
ball.speed(0)                                  
ball.shape("square")                               
ball.color("white") 
ball.penup()
ball.goto(0,0)                                      #align in the center of the screen
# Movement of Ball
ball.dx = 2                                         #Every time the ball moves, it moves by 2 pixels
ball.dy = 2

# scoring pen
pen = turtle.Turtle()               # module.Class()
pen.speed()                         #animation speed 
pen.color("white")
pen.penup()                         #bring up cursor to elimnate line
pen.hideturtle()                    #we want result not to see it
pen.goto(0, 260)
pen.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))

# Scores
score_1 = 0
score_2 = 0


# Functions for Paddle Movement
def paddle_1_up():
    y = paddle_1.ycor()                              #returns the y coordinate
    y += 20                                          #increment y coordinate to move paddle position up
    paddle_1.sety(y)                                 #reposition paddle position to match y variable

def paddle_1_down():
    y = paddle_1.ycor()                            
    y -= 20                                          #decrements y coordinate to move paddle position down
    paddle_1.sety(y)                                 #reposition paddle position to match y variable

def paddle_2_up():
    y = paddle_2.ycor()                             
    y += 20                                         
    paddle_2.sety(y)                               

def paddle_2_down():
    y = paddle_2.ycor()                            
    y -= 20                                     
    paddle_2.sety(y)                             

# Keyboard Bindings
game_screen.listen()                                #listens for keyboard input
game_screen.onkey(paddle_1_up, "w")                 #executes the function: when key "w" is pressed
game_screen.onkey(paddle_1_down, "s")                                       #when key "s" is pressed
game_screen.onkey(paddle_2_up, "Up")                 #executes the function: when "Up" arrow key is pressed
game_screen.onkey(paddle_2_down, "Down")                                    #when "Down" key is pressed




# Game Loop => contains the main game content
while True:
    game_screen.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Establish Borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay thud.mp3&")

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay thud.mp3&")

    # x borders unecessary, keeping for example 
    elif ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))

    elif ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1, score_2), align="center", font=("Courier", 24, "normal"))


    # collision detection with paddles
    #edges are touching, and between top of paddle and bottom of paddle
    if (ball.xcor() > 340 and ball.xcor() < 350)  and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay thud.mp3&")
 

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay thud.mp3&")
 

#   Sound from Zapsplat.com