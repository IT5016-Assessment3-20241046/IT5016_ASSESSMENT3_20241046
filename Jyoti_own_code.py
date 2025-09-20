# turtle_drawing.py
# Author:Jyoti Singh (ID:20241046)
# A turtle graphics program demonstrating modularity, reusability, and design possibilities

import turtle

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

# Function to draw a triangle
def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

# Function to draw a star
def draw_star(size):
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

# Example usage
turtle.color("blue")
draw_square(100)

turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()
turtle.color("green")
draw_triangle(120)

turtle.penup()
turtle.goto(150, 0)
turtle.pendown()
turtle.color("red")
draw_star(150)

turtle.done()
