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

    def MostrarBi(self):
        self.t1 = self.inicio
        while(self.t1 != None):
            print (self.t1.get_descripcion())
            self.t1 = self.t1.siguiente

#--------- Graficar Lista Bitacora --------

    def Graficar_Bit(self):
        archBi = open("lis_bitac.dot", "w")
        #archBi.write("digraph G{\n rankdir = LR;")
        archBi.write("digraph G{\n rankdir = LR")
        t1 = self.inicio
        i = 0
        while t1 != None:
            archBi.write("\"Node" + str(i) + "\"[label = \"" + t1.get_descripcion() + "\" style = filled]\n")
            if t1.siguiente != None:
                archBi.write("\"Node" + str(i) + "\" -> \"Node" + str(i+1) + "\"")
            i = i+1
            t1 = t1.siguiente
        archBi.write("}")
        archBi.close()
        os.system("dot -Tpng lis_bitac.dot > lis_bitac.png")


class Home_Bitacora:
    a = lista_bitacora()
    a.ingresar("Samuel")
    a.ingresar("Alberto")
    a.ingresar("Perez")
    a.ingresar("Jimenez")
    a.ingresar("Malndonado")
    a.ingresar("Schuman")
    a.ingresar("Orellana")
    a.MostrarBi()
    a.Graficar_Bit()
    #print("perro")


