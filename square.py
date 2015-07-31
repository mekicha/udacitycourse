import turtle
window=turtle.Screen()
window.bgcolor('blue' )
def draw_square(arg):
	for i in range(4):
	    arg.forward(100)
	    arg.right(90)


def draw():
    brad = turtle.Turtle()
    draw_square(brad)
    angie=turtle.Turtle()
    angie.color('red')
    angie.circle(100)
    window.exitonclick()

draw()