import turtle,random
t=turtle.Turtle()
t.pensize(5)
t.hideturtle()

for i in range(17):
    t.fd(100)
    t.right(5*(360/17))

t.up()
t.goto(-200,-200)
t.down()
for i in range(17):
    t.fd(100)
    t.right(7*(360/17))

t.up()
t.goto(-200,200)
t.down()
for i in range(17):
    t.fd(100)
    t.right(9*(360/17))

t.up()
t.goto(200,200)
t.down()
for i in range(17):
    t.fd(100)
    t.right(11*(360/17))
    
t.up()
t.goto(200,-200)
t.down()
for i in range(17):
    t.fd(100)
    t.right(13*(360/17))