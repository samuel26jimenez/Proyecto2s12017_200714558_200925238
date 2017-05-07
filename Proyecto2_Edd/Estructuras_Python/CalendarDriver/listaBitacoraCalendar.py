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

    def Graficar_Bit_Calendar(self):
        fiche = open("bitac_calendar.dot", "w")
        fiche.write("digraph G{\n rankdir = LR")
        temp = self.inicio
        cont = 0
        while temp != None:
            fiche.write("\"Node" + str(cont) + "\"[label = \"" + temp.get_descripcion() + "\" style = filled] \n")
            if temp.siguiente != None:
                fiche.write("\"Node" + str(cont) + "\" -> \"Node" + str(cont+1) + "\"")
            cont = cont +1
            temp = temp.siguiente
        fiche.write("}")
        fiche.close()
        os.system("dot -Tpng bitac_calendar.dot > bitac_calendar.png")

class Principal:
    a = lista_bitacora()
    a.ingresar("usuario5")
    a.ingresar("usuario3")
    a.ingresar("usuario8")
    a.ingresar("usuario9")
    a.Graficar_Bit_Calendar()
    print ("Cargar...")
