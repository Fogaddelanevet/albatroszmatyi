import turtle
def negyzet_rajzolas(toll,h):
    for i in range(3):
        toll.forward(h)
        toll.left(120)
      

a =turtle.Screen()
a.bgcolor("green")
a.title("négyzetrajz")
#rajz létrehozása
toll=turtle.Turtle()
negyzet_rajzolas(toll,70)