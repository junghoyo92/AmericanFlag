import turtle
import time
import random

def draw_rectangle(length, height):
    turtle.up()
    x = length
    y = height

    turtle.begin_fill()
    turtle.setpos(x,y)
    turtle.down()
    turtle.forward(418)
    turtle.right(90)
    turtle.forward(220)
    turtle.right(90)
    turtle.forward(418)
    turtle.right(90)
    turtle.forward(220)
    turtle.end_fill()
    return


def draw_flag(A):
    height = int(A)
    length = height*1.9
    draw_rectangle(length, height)
    return

A = input("please enter the height of the flag: ")
