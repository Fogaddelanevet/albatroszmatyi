import turtle
def negyzet_rajzolas(toll,h):
        toll.left(0)
        toll.right(0)
        toll.forward(h)
        toll.left(160)
        toll.forward(h)
        toll.right(43)
        toll.forward(h)
        toll.left(270)
        toll.forward(h)
        toll.right(97)
        toll.forward(h)
        toll.right(43)
        toll.forward(h)
        toll.left(200)
        toll.forward(h)
        toll.right(940)
        toll.forward(h)
        toll.left(17)
        toll.forward(h)
        toll.right(86)
        toll.forward(h)

a =turtle.Screen()
a.bgcolor("green")
a.title("négyzetrajz")
#rajz létrehozása
toll=turtle.Turtle()
negyzet_rajzolas(toll,100)

#8.feladat: BAlrA