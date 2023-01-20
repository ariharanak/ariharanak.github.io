import turtle as t

score_A=0
score_B=0

#display game
win=t.Screen()
win.setup(800,600)
win.bgcolor("yellow")
win.title("PING PONG")
win.tracer(0)

#left paddle
lp=t.Turtle()
lp.speed(0)
lp.shape("square")
lp.color("Black")
lp.shapesize(stretch_wid=5,stretch_len=1)
lp.penup()
lp.goto(-390,0)

#right paddle
rp=t.Turtle()
rp.speed(0)
rp.shape("square")
rp.color("Black")
rp.shapesize(stretch_wid=5,stretch_len=1)
rp.penup()
rp.goto(380,0)

#Ball
ball=t.Turtle()
ball.speed(0)
ball.penup()
ball.shape("circle")
ball.color("blue")
ball.dx=1
ball.dy=1

#score
pt=t.Turtle()
pt.speed(0)
pt.color("Black")
pt.hideturtle()
pt.penup()
pt.goto(0,260)
pt.write("SCORES- A:0 B:0",align="center",font=("Ariel",24,"normal"))

#Padding function
def lp_up():
    lp.sety(lp.ycor()+20)

def lp_down():
    lp.sety(lp.ycor()-20)

def rp_up():
    rp.sety(rp.ycor()+20)

def rp_down():
    rp.sety(rp.ycor()-20)

win.listen()
win.onkeypress(lp_up,'w')
win.onkeypress(lp_down,'s')
win.onkeypress(rp_up,'Up')
win.onkeypress(rp_down,'Down')

while True:
    win.update()
    #ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    #ball wall collide
    #top wall
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    #bottom wall
    if ball.ycor()<-280:
        ball.sety(-280)
        ball.dy*=-1
    #right wall
    if ball.xcor()>380:
        ball.setx(380)
        ball.dx*=-1
        pt.clear()
        score_A+=1
        pt.write("SCORES- A:{} B:{}".format(score_A,score_B),align="center",font=("Ariel",24,"normal"))

    #left wall
    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx*=-1
        pt.clear()
        score_B+=1
        pt.write("SCORES- A:{} B:{}".format(score_A,score_B),align="center",font=("Ariel",24,"normal"))

    #paddle collide
    if ball.xcor() > 370 and rp.ycor()-50 < ball.ycor() < rp.ycor()+50:
        ball.setx(370)
        ball.dx*=-1
    if ball.xcor() < -370 and lp.ycor()-50 < ball.ycor() < lp.ycor()+50:
        ball.setx(-370)
        ball.dx*=-1