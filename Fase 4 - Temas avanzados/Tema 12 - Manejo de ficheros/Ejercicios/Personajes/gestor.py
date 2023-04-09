import pickle

class Personaje:

    # Metodo constructor
    def __init__(self,nombre,vida,ataque,defensa,alcance):
        
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

    # Metodo String
    def __str__(self):
        return f'''
        Nombre: {self.nombre}      Vida: {self.vida}      Ataque: {self.ataque}       Defensa: {self.defensa}     Alcance: {self.alcance}
        '''

class Caballero(Personaje):

    def __init__(self,nombre,vida,ataque,defensa,alcance):
        super().__init__(nombre,vida,ataque,defensa,alcance)

    def __str__(self):
        return f"-- Caballero --\n {super().__str__()}"

class Arquera(Personaje):

    def __init__(self,nombre,vida,ataque,defensa,alcance):
        super().__init__(nombre,vida,ataque,defensa,alcance)

    def __str__(self):
        return f"-- Arquera -- \n{super().__str__()}"

class Mago(Personaje):

    def __init__(self,nombre,vida,ataque,defensa,alcance):
        super().__init__(nombre,vida,ataque,defensa,alcance)

    def __str__(self):
        return f"-- Mago -- \n{super().__str__()}"

class Guerrero(Personaje):

    def __init__(self,nombre,vida,ataque,defensa,alcance):
        super().__init__(nombre,vida,ataque,defensa,alcance)

    def __str__(self):
        return f"-- Guerrero -- \n{super().__str__()}"

########################################################################

class Gestor:

    personajes = []

    def __init__(self):
        self.cargar()

    def cargar(self):
        
        archivo = open('personajes.pckl','ab+')
        archivo.seek(0)

        try:
            self.personajes = pickle.load(archivo)
        except:
            print("El archivo esta vacio.")
        finally:
            archivo.close()
            print(f"Se han cargado {len(self.personajes)} personajes.")

    def agregar_personaje(self,p):
        for personaje in self.personajes:
            if personaje.nombre == p.nombre:
                return

        self.personajes.append(p)
        self.guardar()
        print(f"El personaje {p.nombre} se ha agregado correctamente.")

    def borrar_personaje(self,nombre):
        for personaje in self.personajes:
            if personaje.nombre == nombre:
                self.personajes.remove(personaje)
                self.guardar()
                print(f"{nombre} se ha borrado de la lista de personajes.")
                return
        
        print("El personaje no se encuentra en la lista de personajes.")

    def mostrar_personajes(self):
        for personaje in self.personajes:
            print(personaje)

    def guardar(self):
        archivo = open('personajes.pckl','wb')
        pickle.dump(self.personajes,archivo)
        archivo.close()

gestor = Gestor()

caballero = Caballero('Juan',4,2,4,2)
guerrero = Guerrero('Kratos',2,4,2,4)
arquera = Arquera('Gloria',2,4,1,8)
mago = Mago('Merlin',3,3,3,3)

gestor.agregar_personaje(caballero)
gestor.agregar_personaje(guerrero)
gestor.agregar_personaje(arquera)
gestor.agregar_personaje(mago)

gestor.mostrar_personajes()

gestor.borrar_personaje('Gloria')

gestor.mostrar_personajes()

