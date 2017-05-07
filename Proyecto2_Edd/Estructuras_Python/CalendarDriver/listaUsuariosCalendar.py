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


    def Graficar_lis_Us_Calen(self):
        arch = open("lisUsCalen.dot", "w")
        arch.write("digraph G{\n rankdir = LR")
        t1 = self.inicio
        cont1 =  0
        while t1 != None:
            arch.write("\"Node" + str(cont1) + "\"[label = \"" + t1.get_user() + t1.get_contra() + "\" style = filled]\n")
            if t1.siguiente != None:
                arch.write("\"Node" + str(cont1) + "\" -> \"Node" + str(cont1+1) + "\"")
            cont1 = cont1 +1
            t1 =t1.siguiente
        arch.write("}")
        arch.close()
        os.system("dot -Tpng lisUsCalen.dot > lisUsCalen.png")

class Principal:
    x = lista_usuarios()
    x.ingresar("Samuel", " 2468")
    x.ingresar("Alberto", " 3579")
    x.ingresar("Perez", " 4670")
    x.ingresar("Jimenez", " 9273")
    x.Graficar_lis_Us_Calen()
    print("carga2...")

