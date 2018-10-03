import turtle 
wn = turtle.Screen()        # set wn to the window object
wn.bgcolor("#0D0D0D") 

def cross(x, y):
  rectangle.goto(x, y)
 
wn.onclick(cross)

rectangle = turtle.Turtle()

for i in range(41):
    rectangle.pencolor("#07F8B6")
    rectangle.forward(i * 10)
    rectangle.right(90)

turtle.done()