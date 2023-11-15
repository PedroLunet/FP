import turtle

def koch(pen, order, size):
    if order == 0:
        pen.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(pen, order-1, size/3)
            pen.left(angle)

wn = turtle.Screen()
tess = turtle.Turtle()
print(koch(tess, 3, 300))