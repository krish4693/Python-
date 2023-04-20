import turtle
import time
squary = turtle.Turtle()
squary.speed(0)

for i in range(500): # this "for" loop will repeat these functions 500 times
    squary.forward(i)
    squary.left(91)
time.sleep(1000)