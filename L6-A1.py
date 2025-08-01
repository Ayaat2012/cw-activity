import turtle

sc = turtle.Screen()

# creating canvas
sc.bgcolor("purple")
sc.setup(500, 500)

turtle.title("Welcome to Turtle Window")

# turtle object cretion
board = turtle.Turtle()

n = 6
# creating a square
for i in range(n):
    board.forward(100)
    board.left(360/n)

turtle.done()