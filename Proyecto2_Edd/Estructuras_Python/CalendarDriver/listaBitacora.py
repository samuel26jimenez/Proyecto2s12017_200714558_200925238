import os

class nodo_lista:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.siguiente = None

    def get_descripcion(self):
        return self.descripcion

class lista_bitacora:
    def __init__(self):
        self.inicio = None

    def ingresar(self, descrip):
        nuevoNodo = nodo_lista(descrip)

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
            aux.siguiente = None
