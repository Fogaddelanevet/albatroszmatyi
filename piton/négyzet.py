
import turtle


def negyzet_rajzolas(toll,h):
    for i in range(4):
        toll.forward(h)
        toll.left(90)
      

a =turtle.Screen()
a.bgcolor("green")
a.title("négyzetrajz")
#rajz létrehozása
toll=turtle.Turtle()
negyzet_rajzolas(toll,70)

