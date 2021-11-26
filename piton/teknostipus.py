import turtle
def negyzet_rajzolas(toll,h):
    for i in range(6):
        toll.forward(h)
        toll.left(60)
      

a =turtle.Screen()
a.bgcolor("green")
a.title("négyzetrajz")
#rajz létrehozása
toll=turtle.Turtle()
negyzet_rajzolas(toll,70)
teknos=turtle.Turtle()

print(type(teknos))