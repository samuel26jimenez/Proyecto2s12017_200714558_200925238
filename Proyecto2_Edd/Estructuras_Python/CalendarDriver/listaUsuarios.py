import os

class nodo_lista:
    def __init__(self, usuario, contrasena):
        self.usuario = usuario
        self.contrasena = contrasena
        self.siguiente = None
        self.anterior = None

    def get_user(self):
        return self.usuario

    def get_contra(self):
        return self.contrasena

class lista_usuarios:
    def __init__(self):
        self.inicio = None

    def ingresar(self, usu, passw):
        nuevoNodo = nodo_lista(usu, passw)

        if self.existe(usu) == True:
            print("USUARIO YA EXISTE\n")

        else:
            if(self.inicio == None):
                self.inicio = nuevoNodo
            else:
                aux = self.inicio
                aux2 = self.inicio
                while(aux != None):
                    aux2 = aux
                    aux = aux.siguiente

                aux = nuevoNodo
                aux2.siguiente = aux
                aux.anterior = aux2

    def existe(self, usuario):
        aux = self.inicio
        while(aux != None):
            if(aux.get_user() == usuario):
                return True
            aux = aux.siguiente
        return False

    def graficar(self):
        fichero = open("lisUs.dot", "w")
        fichero.write("digraph G{\n rankdir = LR")
        tempo = self.inicio
        conta = 0
        while tempo != None:
            fichero.write("\"Node" + str(conta) + "\"[label = \"" + tempo.get_user() + tempo.get_contra() + "\" style = filled]\n")
            if tempo.siguiente != None:
                fichero.write("\"Node" + str(conta) + "\" -> \"Node" + str(conta+1) + "\"" )
            conta += 1
            tempo = tempo.siguiente
        fichero.write("}")
        fichero.close()
        os.system("dot -Tpng lisUs.dot > lisUs.png")

class Principal:
    x = lista_usuarios()
    x.ingresar("Sammuel", " 234")
    x.ingresar("Alberto", "1234")
    x.ingresar("Perez", "456")
    x.ingresar("Jimenez", "9584")
    x.graficar()
