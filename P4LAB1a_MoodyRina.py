import turtle
wn = turtle.Screen()

rina = turtle.Turtle()
wn.bgcolor("pink")
rina.color("red")
rina.pensize(4)
rina.shape("classic")

rina.left(90)
rina.forward(110)
rina.right(90)
rina.forward(35)
for A in range(5):
    rina.right(30)
    rina.forward(15)

rina.right(28)
rina.forward(35)
rina.left(135)
rina.forward(75)

rina.penup()
rina.left(43)
rina.forward(40)
rina.pendown()

rina.left(80)
rina.forward(110)
rina.right(150)
rina.forward(80)
rina.left(140)
rina.forward(80)
rina.right(150)
rina.forward(110)

wn.mainloop()
