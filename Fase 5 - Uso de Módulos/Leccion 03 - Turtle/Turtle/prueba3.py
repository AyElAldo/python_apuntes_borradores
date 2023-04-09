import turtle as t

t.setup(500,500)

t.shape('turtle')
t.color('green')
t.width(5)


def rectangulo(px, py, ancho, alto):
    t.penup()
    t.goto(px + ancho / 2, py + alto / 2)

    t.seth(180)
    t.pendown()
    t.forward(ancho)
    t.left(90)
    t.forward(alto)
    t.left(90)
    t.forward(ancho)
    t.left(90)
    t.forward(alto)


    pass

rectangulo(0,0, 400, 300)

t.done()
t.bye()

