import turtle as t

# Tamaño en pixeles
t.setup(540,540)

t.shape("turtle") # Forma a la tortuga
t.color("Blue")

# Pos --> posicion de la tortuga
print(t.pos())
# Se mueve adelante
t.forward(250)
t.left(90)
t.forward(250)

t.left(90)
t.forward(500)

t.left(90)
t.forward(500)

t.left(90)
t.forward(500)

t.left(90)
t.forward(250)
print(t.pos())

# Cerrar la ejecucion con las turinas de cierre
t.done()
t.bye()