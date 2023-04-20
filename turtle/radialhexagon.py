from turtle import Turtle
import time

def hexagon(t,length):
    for count in range(6):
        t.forward(length)
        t.left(60)

def radialHexagon(t,n,length):
    for count in range(n):
        hexagon(t,length)
        t.left(360/n)

t=Turtle()
t.speed(0)
radialHexagon(t,100,100)
time.sleep(30)
