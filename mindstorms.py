import turtle

def draw_sqaure(some_turtle):
    for x in range (0, 4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("gray")

# draw a square    
    blair = turtle.Turtle()
    blair.shape("turtle")
    blair.color("blue")
    for x in range (0, 18):
        draw_sqaure(blair)
        blair.right(20)
# draw a circle
#    alex = turtle.Turtle()
#    alex.shape("arrow")
#    alex.color("red")
#    alex.circle(100)

# draw a triangle
#    brenda = turtle.Turtle()
#     brenda.shape("turtle")
#     brenda.color("green")
#     brenda.right(180)
#     for x in range (0, 3):
#         brenda.forward(200)
#         brenda.left(120)
    
    window.exitonclick()
    
draw_shapes()
