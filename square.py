import turtle
window=turtle.Screen()
window.bgcolor('blue' )
def draw_square(arg):
	for i in range(4):
	    arg.forward(100)
	    arg.right(90)


def draw():
    brad = turtle.Turtle()
    brad.speed(2)
    brad.shape('turtle')
    brad.color('red')
    for i in range(36):
        draw_square(brad)
        brad.right(10)
    
    window.exitonclick()

draw()