import turtle
import random
import time
delay=0.1

#----------set up the Screen------
window=turtle.Screen()  
window.bgcolor('black')
window.title('Snake Game by Narasimhulu')
window.setup(width=600,height=600)
window.tracer(0) #when windows updation 

#--------Snake head--------------
head=turtle.Turtle()
head.shape('square')
head.color('red')
head.speed(0)
head.goto(0,0)
head.penup() #used the remove the line when it is moved
head.direction='stop'

#----Snake food
food=turtle.Turtle()
food.shape('circle')
food.color('green')
food.speed(0)
food.penup()
food.goto(random.randint(-290,290),random.randint(-290,290)) #290 is used because food should not touch the border

#----Score---
score=0
pen=turtle.Turtle()
pen.hideturtle()
pen.shape('square')
pen.color('red')
pen.speed(0)
pen.penup()
pen.goto(0,260)
pen.write(f'SCORE:{score}',align='center')


def move():
    if head.direction=='Up':
        y=head.ycor()
        head.sety(y+20)
    if head.direction=='Down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction=='Right':
        x=head.xcor()
        head.setx(x+20)
    if head.direction=='Left':
        x=head.xcor()
        head.setx(x-20)

def go_up():
    if head.direction!='Down':
        head.direction='Up'
def go_down():
    if head.direction!='Up':
        head.direction='Down'
def go_right():
    if head.direction!='Left':
        head.direction='Right'
def go_left():
    if head.direction!='Right':
        head.direction='Left'

window.listen() #listen to keys what user is doing
window.onkeypress(go_up,'Up')
window.onkeypress(go_down,'Down')
window.onkeypress(go_right,'Right')
window.onkeypress(go_left,'Left')
body=[]
while True:
    window.update() #used to update the screen
    #border collisions
    if head.ycor()>290 or head.ycor()<-290 or head.xcor()>290 or head.xcor()<-290:
        head.goto(0,0)
        time.sleep(2)
        head.direction='stop'
        score=0
        pen.clear()
        pen.write(f'SCORE:{score}',align='center')
        for new_body in body:
            new_body.goto(1000,1000)
        body.clear()
        
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        score+=1
        delay-=0.0001
        pen.clear()
        pen.write(f'SCORE:{score}',align='center')
        food.goto(x,y)
        
        new_body=turtle.Turtle()
        new_body.shape('square')
        new_body.color('blue')
        new_body.speed(0)
        new_body.penup()
        body.append(new_body)
    #body collisions
    for i in range(len(body)-1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x,y)
    if len(body)>0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)
        
    time.sleep(delay)
    move()

    for new_body in body:
        if new_body.distance(head)<20:
            head.goto(0,0)
            time.sleep(2)
            head.direction='stop'
            score=0
            pen.clear()
            pen.write(f'SCORE:{score}',align='center')
            for new_body in body:
                new_body.goto(1000,1000)
            body.clear()
            
            






















window.mainloop() #used to create the loop in window and it thrown last
