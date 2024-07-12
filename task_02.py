import turtle

def koch_curve(t, order, size_):
    if order == 0:
        t.forward(size_)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size_ / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, size / 2 / 3**0.5)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

# Виклик функції
draw_koch_curve(3)
