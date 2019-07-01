import turtle

def draw_squ():
    window = turtle.Screen()
    window.bgcolor("violet")

    brad=turtle.Turtle()
    brad.color("red")
    for i in range(0,4):
        brad.forward(100)
        brad.right(90)
    brad.left(45)
    brad.shape("circle")
    brad.backward(70)

    ang=turtle.Turtle()
    ang.color("blue")
    ang.shape("arrow")
    ang.circle(100)
    window.exitonclick()
draw_squ()
