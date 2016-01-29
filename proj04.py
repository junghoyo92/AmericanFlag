## CSE 231
## Section 2

## This part imports the turtle and math modes for the program.

import turtle
import math

## This part of the program is the function that draws a rectangle with parameters length, height, and color.

def draw_rectangle(length, height, color):
    turtle.color(color)                             # designates a color for the pen and fill of the rectangle
    turtle.begin_fill()                             # beginning point of the area that is being filled 
    turtle.forward(length)                          # draws a side as the length of the rectangle
    turtle.left(90)                                 # turns turtle 90 degrees to the left
    turtle.forward(height)                          # draws a side as the height of the rectangle
    turtle.left(90)                                 # turns turtle 90 degrees to the left
    turtle.forward(length)                          # draws a side as the length of the rectangle
    turtle.left(90)                                 # turns turtle 90 degrees to the left
    turtle.forward(height)                          # draws a side as the height of the rectangle
    turtle.left(90)                                 # turns turtle 90 degrees to the left
    turtle.end_fill()                               # fills the area inbetween the beginning point and the end

## This part of the program is the function that draws a star with parameters size and color.

def draw_star(size, color):
    turtle.color(color)                             # designates a color for the pen and fill of the star
    turtle.begin_fill()                             # beginning point of the area that is being filled
    for i in range(5):                              # for loop that draws a star
        turtle.forward(size)                        
        turtle.left(72)
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()                               # fills the area inbetween the beginning point and the end

## This part of the program is the function takes a color string to seperate and return as r,g,b

def get_color(color):
    red = [.698, .132, .203]                        # the color red as a string
    blue = [.234, .233, .430]                       # the color blue as a string
    white = [1.000, 1.000, 1.000]                   # the color white as a string
    black = [0, 0, 0]                               # the color black as a string
    if color is 'red':                              # if the color is said to be red, then the function returns the proper r,g,b values
        r = red[0]
        g = red[1]
        b = red[2]
        return r,g,b
    if color is 'blue':                             # if the color is said to be blue, then the function returns the proper r,g,b values
        r = blue[0]
        g = blue[1]
        b = blue[2]
        return r,g,b
    if color is 'white':                            # if the color is said to be white, then the function returns the proper r,g,b values
        r = white[0]
        g = white[1]
        b = white[2]
        return r,g,b
    if color is 'black':                            # if the color is said to be black, then the function returns the proper r,g,b values
        r = black[0]
        g = black[1]
        b = black[2]
        return r,g,b

## This part of the program is the function which uses the parameter height to draw the American flag.
## The function calls upon the draw_rectangle, draw_star, and get_color functions to draw the American flag.

def draw_flag(height):                              
    height_flag = float(height)                     # Next 6 lines are local variables used in the function
    length_flag = float(1.9 * height)
    height_union = float((7/13) * height)
    length_union = float((2/5) * length_flag)
    height_stripe = float(height/13)
    size_star = (4/5) * height_stripe
    turtle.speed(100)                               # This changes the speed of the drawing

    for i in range(14):                             # A for loop is used to draw the 14 rectangles that are used in the American flag
        if i%2 == 0 and i<6:                        # States if the remainder of i divided by 2 is equal to 0 and less than 6, then run this part of 
            length = (length_flag)                  # the function which calls upon the draw_rectangle function with specific parameters for length,
            height = (height_stripe)                # height, and color.
            color = get_color('red')                # draws the 3 larger red rectangles
            x = 0
            y = i * (1/13) * height_flag
            turtle.goto(x,y)
            draw_rectangle(length, height, color)
        elif i%2 == 1 and i<6:                      # States if the remainder of i divided by 2 is equal to 1 and less than 6, then run this part of
            length = length_flag                    # the function which calls upon the draw_rectangle function with specific parameters for length, 
            height = height_stripe                  # height, and color.
            color = get_color('white')              # draws the 3 larger white rectangles
            x = 0
            y = i * (1/13) * height_flag
            turtle.goto(x,y)
            draw_rectangle(length, height, color)
        elif i%2 == 0 and i>=6 and i<13:            # States if the remainder of i divided by 2 is equal to 0 and greater than or equal to 6 and less
            length = length_flag - length_union     # than 13, then run this part of the function which calls upon the draw_rectangle function with
            height = height_stripe                  # specific parameters for length, height, and color.
            color = get_color('red')                # draws the 4 smaller red rectangles
            x = length_union
            y = i * (1/13) * height_flag
            turtle.goto(x,y)
            draw_rectangle(length, height, color)
        elif i%2 == 1 and i>=6 and i<13:            # States if the remainder of i divided by 2 is equal to 1 and greater than or equal to 6 and less
            length = length_flag - length_union     # than 13, then run this part of the function which calls upon the draw_rectangle functions with
            height = height_stripe                  # specific parameters for length, height, and color.
            color = get_color('white')              # draws the 3 smaller white rectangles
            x = length_union
            y = i * (1/13) * height_flag
            turtle.goto(x,y)
            draw_rectangle(length, height, color)
        elif i == 13:                               # States if i equals 13, then run this part of the function which calls upon the draw_rectangle
            length = length_union                   # function with specific parameters length, height, and color.
            height = height_union                   # draws 1 blue rectangle
            color = get_color('blue')
            x = 0
            y = (6/13) * height_flag
            turtle.penup()
            turtle.goto(x,y)
            turtle.pendown()
            draw_rectangle(length, height, color)

    for i in range(9):                              # A for loop is used to draw 9 lines of stars on the American flag
        size = (1/3) * size_star
        color = get_color('white')
        x = length_union/12
        x_o = x/2
        y = height_union/10
        y_o = height_flag - height_union + (i*y) + y
        if i%2 == 0:                                # States if the remainder of i divided by 2 is equal to 0, then run this part of the function
            for i in range(6):                      # which runs a for loop that calls the draw_star function 6 times while moving the turtle pen
                turtle.penup()                      # in the correct position to create a line with 6 stars with white fill.
                turtle.goto(x_o + (2*x*i),y_o)
                turtle.pendown()
                draw_star(size, color)
        elif i%2 == 1:                              # States if the remainder of i divided by 2 is equal to 1, then run this part of the function
            for i in range(5):                      # which runs a for loop that calls the draw_star function 5 times while moving the turtle pen
                turtle.penup()                      # in the correct position to create a line with 5 stars with white fill.
                turtle.goto((x_o+x) + (2*x*i), y_o)
                turtle.pendown()
                draw_star(size, color)
                
    turtle.penup()                                  # this part draws the black boarder line of the flag
    turtle.goto(0,0)
    turtle.pendown()
    turtle.pencolor(get_color('black'))
    turtle.forward(length_flag)
    turtle.left(90)
    turtle.forward(height_flag)
    turtle.left(90)
    turtle.forward(length_flag)
    turtle.left(90)
    turtle.forward(height_flag)
    
draw_flag(200)                                      # Draws the flag with a height of 200
            
