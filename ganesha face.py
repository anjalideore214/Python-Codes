import turtle

# Function to draw circle
def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Function to draw rectangle
def draw_rectangle(color, width, height, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

# Initialize Turtle
turtle.speed(0)
turtle.bgcolor("lightgray")

# Draw face
draw_circle("white", 100, 0, 0)

# Draw eyes
draw_circle("black", 10, -40, 50)
draw_circle("black", 10, 40, 50)

# Draw trunk
draw_rectangle("white", 20, 50, 0, -70)

# Draw tusks
draw_rectangle("white", 5, 20, -10, -70)
draw_rectangle("white", 5, 20, 5, -70)

# Draw mouse
draw_rectangle("black", 40, 10, -20, -100)

# Draw lines for decorative elements
turtle.penup()
turtle.goto(-100, 20)
turtle.pendown()
turtle.color("black")
turtle.width(5)
turtle.right(30)
turtle.forward(40)
turtle.backward(40)
turtle.left(60)
turtle.forward(40)
turtle.backward(40)
turtle.right(30)
turtle.penup()
turtle.goto(100, 20)
turtle.pendown()
turtle.right(180)
turtle.forward(40)
turtle.backward(40)
turtle.right(60)
turtle.forward(40)
turtle.backward(40)
turtle.left(30)

# Hide turtle and display
turtle.hideturtle()
turtle.done()
