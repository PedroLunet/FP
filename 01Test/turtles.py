import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Py turtles. Lunet")

lunet = turtle.Turtle()
lunet.color("Orange")
lunet.pensize(3)

turtle.register_shape("pedro.gif")
pedro = turtle.Turtle()
pedro.shape("pedro.gif")
pedro.pensize(3)



pedro.left(180)
pedro.forward(50)
pedro.right(120)
pedro.forward(100)

lunet.forward(50)
lunet.left(120)
lunet.forward(100)

window.mainloop()
turtle.bye()