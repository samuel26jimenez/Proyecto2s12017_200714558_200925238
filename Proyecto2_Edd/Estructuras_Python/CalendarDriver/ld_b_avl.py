__author__ = 'Samuel'
#------ Lista Doblemente Enlazada --------
class ListaD_Nodo:
    def __init__(self, nom):
        self.nom = nom
        self.ante = None
        self.sig = None

    def set_Nomb(self, nombre):
        self.nom = nombre

    def get_Nomb(self, nombre):
        self.nom = nombre

class Metodo_LD:
    def __init__(self):
        self.ini = None
        self.fin = None

    def esVacio(self):
        if self.ante == None & self.sig == None:
            return True
        else:
            return False

    def inserta_Nodo(self, x):
        nvo_Nodo = ListaD_Nodo(x)
        if self.esVacio() == True:
            self.ini = self.fin = nvo_Nodo
        else:
            self.fin.sig = nvo_Nodo
            nvo_Nodo.ante = self.fin
            self.fin = self.fin.sig
