import turtle
wn = turtle.Screen()         
wn.bgcolor("lightblue")


tina = turtle.Turtle()      
tina.color("hotpink")
tina.pensize(6)

emma = turtle.Turtle()
emma.color("blue")
emma.pensize(2)

tina.forward(130)            
tina.left(120)
tina.forward(130)
tina.left(120)
tina.forward(130)
tina.left(120)              

tina.right(180)              
tina.forward(80)             

emma.forward(70)            
emma.left(90)
emma.forward(70)
emma.left(90)
emma.forward(70)
emma.left(90)
emma.forward(70)
emma.left(90)

wn.mainloop()
