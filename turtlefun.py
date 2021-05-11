import time
import turtle


s = turtle.getscreen()
t = turtle.Turtle()

for x in range(60):
    time.sleep(.5)
    t.right(6)
    t.forward(15)
