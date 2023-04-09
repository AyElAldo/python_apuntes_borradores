import turtle as t

t.setup(500,500)


t.shape('turtle')
t.color('red')
t.width(4)


def poligono_regular(px, py, radio, lados):
    t.penup()
    t.goto(px, py - radio)
    
    pass


poligono_regular(0,0,100,6)

t.done()
t.bye()
