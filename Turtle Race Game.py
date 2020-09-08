import turtle
import random
playrone=turtle.Turtle()
playrone.color("green")
playrone.shape("turtle")
playrone.penup()
playrone.goto(-200,100)
playrtwo=playrone.clone()
playrtwo.color("blue")
playrtwo.penup()
playrtwo.goto(-200,-100)
playrone.goto(300,60)
playrone.pendown()
playrone.circle(40)
playrone.penup()
playrone.goto(-200,100)
playrtwo.penup()
playrtwo.goto(300,-140)
playrtwo.pendown()
playrtwo.circle(40)
playrtwo.penup()
playrtwo.goto(-200,-100)
dice=[1,2,3,4,5,6]
for i in range(20):
    if playrone.pos()>=(300,100):
        print("player one wins")
        break
    if playrtwo.pos()>=(300,-100):
        print("player two wins")
        break
    else:
        playroneturn=input("Press the enter key to start the game")
        diceoutcome=random.choice(dice)
        print("The result of the dice is",diceoutcome)
        print("The no. of steps moved by the turtle is",20*diceoutcome)
        playrone.fd(20*diceoutcome)
        playrtwoturn=input("Press the enter key to start the game")
        d=random.choice(dice)
        print("The result of the dice is",d)
        print("The no.of steps moved by the turtle is",20*d)
        playrtwo.fd(20*d)
        
