import turtle

sc = turtle.Screen()

sc.bgcolor("deep pink")
sc.setup(500, 500)

turtle.title("Welcome to Turtle Window")

# crating a star
board = turtle.Turtle()

# first triangle for the star
board.forward(100) # draw base

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

# second triangle for the star
board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

turtle.done()