import turtle as t
import random as r

t.bgcolor("green")


cel =250

t.penup()
t.goto(250,250)
t.color("light gray")
t.pensize(10)
t.pendown()
t.goto(cel,-100,)

t.hideturtle()

t1=t.Turtle() 
t1.color("Black")
t1.penup()
t1.goto(-250,100)
t1.pendown()
t1.shape("turtle")

t2=t.Turtle() 
t2.color("yellow")
t2.penup()
t2.goto(-250,50)
t2.pendown()
t2.shape("turtle")

t3=t.Turtle() 
t3.color("magenta")
t3.penup()
t3.goto(-250,0)
t3.pendown()
t3.shape("turtle")

t4=t.Turtle() 
t4.color("Red")
t4.penup()
t4.goto(-250,-50)
t4.pendown()
t4.shape("turtle")


szoveg=t.Turtle()
szoveg.penup()
szoveg.color("gold")
szoveg.setpos(-200,200)
szoveg.hideturtle()


szoveg.write("TEKNŐS FUTAM",align="left",font=("Ariel",36,"bold"))

while t1.xcor()<cel and t2.xcor()<cel and  t3.xcor()<cel and t4.xcor()<cel:
    t1.forward (r.randrange(1,5))
    t2.forward (r.randrange(1,5))
    t3.forward (r.randrange(1,5))
    t4.forward (r.randrange(1,5))
    
if t1.xcor()>=cel:
    gyoztes ="Fekete győzött"
elif t2.xcor()>=cel:
   gyoztes = "Sárga szin győzött"
elif t3.xcor()>=cel:
     gyoztes = "Rozsa szin győzött"
else:
     gyoztes = "Piros győzött"

szoveg.setpos(-200,-200)
szoveg.write(gyoztes,align="left",font=("Ariel",30,"bold"))



    
    
