import turtle
import winsound
import math
import random


#window
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("nokia 3310")


turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")
turtle.register_shape("blaze.gif")
#bordure
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pencolor("white")
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#joueur
player = turtle.Turtle()
player.setposition(0,-270)
player.color("green")
player.shape("player.gif")
player.penup()
player.setheading(90)
playerspeed = 15

number_of_enemies = 5
enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())
    
for enemy in enemies:
#creation de l'ennemie
    enemy.shape("invader.gif")
    enemy.color("red")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2



#creating the gun
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("blaze.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()


bulletspeed = 20
# def
#ready to fire
#fire the bullet
bulletstate = "ready"


#mouvement de gauche
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280 :
        x = -280
    player.setx(x)
#mouvement de droite
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280 :
        x = 280
    player.setx(x)
def fire_bullet():
    #global variables
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("shotsound.wav", winsound.SND_ASYNC)
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y+10)
        bullet.showturtle()
    
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True 
    else:
        return False
            

#clav par
turtle.listen()
turtle.onkey(move_left, "q")
turtle.onkey(move_right, "d")
turtle.onkey(fire_bullet, "space")



#loop du jeux
while True:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        
        if enemy.xcor() > 280 :
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if enemy.xcor() < -280 :
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
    #collision
        if isCollision(bullet, enemy):
            winsound.PlaySound("kill.wav", winsound.SND_ASYNC)
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)

            #rzset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            score_pen.clear()
            score +=10
            scorestring = "Score: %s" %score
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            
        
        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break
    #mouvement de balle
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    if bullet.ycor()> 275:
        bullet.hideturtle()
        bulletstate = "ready"
    
    





delay = raw_input("Press Enter")
 



































