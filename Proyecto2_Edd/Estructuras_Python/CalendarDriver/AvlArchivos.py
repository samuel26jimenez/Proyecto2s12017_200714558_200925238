__author__ = 'Samuel'
import os
escritorio = os.path.expanduser("~/Desktop")

class NodoAvl:
    activos = None

    def __init__(self, nombre):
        self.nombre = nombre



        self.derecho = None
        self.izquierdo = None
        self.fe = 0

    def insertaNombre(self, nombre):
        nuevo = NodoUsar(nombre)
        self.activos.cabeza = self.activos.insertarActivo(nuevo, self.activos.cabeza)
        self.activos.cabeza, val = self.activos.BalanceFactor(self.activos.cabeza)
        self.activos.cabeza = self.activos.ArbolCorre(self.activos.cabeza)

class NodoUsar:
    def __init__(self, nombre):
        self.nombre = nombre
        self.fe = 0


class AVL:
    def __init__(self):
        self.cabeza = None


    def esHoja(self, nodo):
        if nodo==None:
            return False
        if nodo.derecho!=None or nodo.izquierdo!=None:
            return False
        return True






    def BalanceFactor(self, iniciarRa):
        if iniciarRa==None:
            return iniciarRa, 0
        if self.esHoja(iniciarRa):
            iniciarRa.fe = 0
            return iniciarRa, 1
        elif iniciarRa.izquierdo and iniciarRa.derecho:
            iniciarRa.izquierdo, valorIz = self.BalanceFactor(iniciarRa.izquierdo)
            iniciarRa.derecho, valorDer = self.BalanceFactor(iniciarRa.derecho)
            iniciarRa.fe = valorDer - valorIz
            if valorDer> valorIz:
                return iniciarRa, (1+valorDer)
            else:
                return iniciarRa, (1+valorIz)
        elif iniciarRa.izquierdo:
            iniciarRa.izquierdo, valorIz = self.BalanceFactor(iniciarRa.izquierdo)
            iniciarRa.fe = valorIz*(-1)
            return iniciarRa, (1+ valorIz)
        elif iniciarRa.derecho:
            iniciarRa.derecho, valorDer = self.BalanceFactor(iniciarRa.derecho)
            iniciarRa.fe = valorDer
            return iniciarRa, (1+ valorDer)
        return iniciarRa







    def rotacionIzIz(self, inici):
        n0 = inici
        n1 = inici.izquierdo
        n0.izquierdo = n1.derecho
        n1.derecho = n0
        return n1








    def rotacionIzDer(self, inici):
        n0 = inici
        n1 = inici.izquierdo
        n2 = inici.izquierdo.derecho
        n0.izquierdo = n2.derecho
        n1.derecho = n2.izquierdo
        n2.derecho = n0
        n2.izquierdo = n1
        return n2






    def rotacionDerDer(self, inici):
        n0 = inici
        n1 = inici.derecho
        n0.derecho = n1.izquierdo
        n1.izquierdo = n0
        return n1





    def rotacionDerIz(self, inici):
        n0 = inici
        n1 = inici.derecho
        n2 = inici.derecho.izquierdo
        n0.derecho = n2.izquierdo
        n1.izquierdo = n2.derecho
        n2.derecho = n1
        n2.izquierdo = n0
        return n2






    def CasosAVLConsdirar(self, ra):
        if ra.fe==-2:
            if ra.izquierdo.fe==-1:
                ra = self.rotacionIzIz(ra)
            else:
                ra = self.rotacionIzDer(ra)
        if ra.fe==2:
            if ra.derecho.fe==1:
                ra = self.rotacionDerDer(ra)
            else:
                ra = self.rotacionDerIz(ra)
        return ra







    def ArbolCorre(self, ra):
        if ra==None:
            return
        if ra.izquierdo:
           ra.izquierdo = self.ArbolCorre(ra.izquierdo)
        if ra.derecho:
            ra.derecho = self.ArbolCorre(ra.derecho)
        if ra.fe == 2 or ra.fe==-2:
            ra = self.CasosAVLConsdirar(ra)
            ra, val = self.BalanceFactor(ra)
        return ra







    def insertarActivo(self, nodoN, iniciarRa):
        if iniciarRa==None:
            iniciarRa = nodoN

        else:
            if iniciarRa.nombre > nodoN.nombre:
                iniciarRa.izquierdo = self.insertarActivo(nodoN, iniciarRa.izquierdo)
            else:
                iniciarRa.derecho = self.insertarActivo(nodoN,iniciarRa.derecho)
        return iniciarRa






    def eliminarActivo(self, iniciarRa, id):
        if iniciarRa == None:
            return
        elif iniciarRa.id > id:
            iniciarRa.izquierdo = self.eliminarActivo(iniciarRa.izquierdo, id)
        elif iniciarRa.id < id:
            iniciarRa.derecho = self.eliminarActivo(iniciarRa.derecho, id)
        else:
            q = iniciarRa
            if q.izquierdo == None:
                iniciarRa = q.derecho
            elif q.derecho== None:
                iniciarRa = q.izquierdo
            else:
                self.reemplazar(q)
            q = None
        return iniciarRa



    def reemplazar(self, aux):
        p = aux
        a = aux.izquierdo
        while a.derecho:
            p = a
            a = a.derecho
        aux.nombre = a.nombre
        aux.descripcion = a.descripcion
        aux.id = a.id
        if p == aux:
            p.izquierdo = a.izquierdo
        else:
            p.derecho = a.izquierdo
            aux = a




    def existeActivo(self, b, id):
        if b==None:
            return False
        if b.id == id:
            return True
        elif b.id > id:
            if b.izquierdo:
                return self.existeActivo(b.izquierdo, id)
            else:
                return False
        else:
            if b.derecho:
                return self.existeActivo(b.derecho, id)
            else:
                return False





    def graficarAVL(self, iniciarRa):
        if iniciarRa==None:
            print("esta vacio :(")
            return
        file = open("avl.dot", "w")
        file.write("digraph G{\n")
        file.write(self.graficarNodoAVL(iniciarRa))
        file.write("}\n")
        file.close()
        os.system("dot -Tpng avl.dot > avl.png")


    def graficarNodoAVL(self, nodo):
        cadena = "nodo"+self.getDispersion(nodo)+"[label=\"<f0>|<f1>"+nodo.nombre+" \\n"+ "Datos....." +"|<f2>\", shape=record,style=filled,fillcolor=\"blue:cyan\", gradientangle=\"270\"]\n"
        if nodo.izquierdo:
            cadena+=self.graficarNodoAVL(nodo.izquierdo)
            cadena+= "nodo"+self.getDispersion(nodo)+":f0 -> "+"nodo"+self.getDispersion(nodo.izquierdo)+"\n"
        if nodo.derecho:
            cadena += self.graficarNodoAVL(nodo.derecho)
            cadena += "nodo" + self.getDispersion(nodo) + ":f2 -> " + "nodo" + self.getDispersion(nodo.derecho)+"\n"
        return cadena

    def getDispersion(self, objeto):
        id = hash(objeto)
        if int(id) < 0:
            return str((-1 * id))
        return str(id)






    def modificarActivo(self, id, nuevaD, iniciarRa):
        if iniciarRa==None:
            return iniciarRa
        if iniciarRa.id == id:
            iniciarRa.descripcion = nuevaD
            return iniciarRa
        if iniciarRa.id<id:
            iniciarRa.derecho = self.modificarActivo(id, nuevaD, iniciarRa.derecho)
            return iniciarRa
        if iniciarRa.id>id:
            iniciarRa.izquierdo = self.modificarActivo(id, nuevaD, iniciarRa.izquierdo)
            return iniciarRa
        return iniciarRa






    def retornarIzDer(self, iniciarRa):
        cadena = ""
        if iniciarRa==None:
            return cadena
        cadena+= iniciarRa.id+","+iniciarRa.nombre+","+iniciarRa.descripcion
        if iniciarRa.derecho:
            cadena+=","+self.retornarIzDer(iniciarRa.derecho)
        if iniciarRa.izquierdo:
            cadena+=","+self.retornarIzDer(iniciarRa.izquierdo)
        print (cadena)
        return cadena







    def retornarDesripcion(self, iniciarRa, id):
        if iniciarRa==None:
            return "No existe, nada"
        if iniciarRa.id == id:
            return iniciarRa.descripcion+","+iniciarRa.nombre
        if iniciarRa.id<id:
            return self.retornarDesripcion(iniciarRa.derecho, id)
        if iniciarRa.id>id:
            return self.retornarDesripcion(iniciarRa.izquierdo, id)



class Principal2:
    b = AVL()

    a = NodoAvl("samuel4")
    b.cabeza = b.insertarActivo(a,b.cabeza)
    b.cabeza, val = b.BalanceFactor(b.cabeza)
    b.cabeza = b.ArbolCorre(b.cabeza)

    a = NodoAvl("samuel6")
    b.cabeza = b.insertarActivo(a,b.cabeza)
    b.cabeza, val = b.BalanceFactor(b.cabeza)
    b.cabeza = b.ArbolCorre(b.cabeza)

    a = NodoAvl("samuel1")
    b.cabeza = b.insertarActivo(a,b.cabeza)
    b.cabeza, val = b.BalanceFactor(b.cabeza)
    b.cabeza = b.ArbolCorre(b.cabeza)

    a = NodoAvl("samuel7")
    b.cabeza = b.insertarActivo(a,b.cabeza)
    b.cabeza, val = b.BalanceFactor(b.cabeza)
    b.cabeza = b.ArbolCorre(b.cabeza)

    a = NodoAvl("samuel21")
    b.cabeza = b.insertarActivo(a,b.cabeza)
    b.cabeza, val = b.BalanceFactor(b.cabeza)
    b.cabeza = b.ArbolCorre(b.cabeza)

    a = NodoAvl("samuel3")
    b.cabeza = b.insertarActivo(a,b.cabeza)
    b.cabeza, val = b.BalanceFactor(b.cabeza)
    b.cabeza = b.ArbolCorre(b.cabeza)

    a = NodoAvl("samuel55")
    b.cabeza = b.insertarActivo(a,b.cabeza)
    b.cabeza, val = b.BalanceFactor(b.cabeza)
    b.cabeza = b.ArbolCorre(b.cabeza)


    a = NodoAvl("alberto43")
    b.cabeza = b.insertarActivo(a,b.cabeza)
    b.cabeza, val = b.BalanceFactor(b.cabeza)
    b.cabeza = b.ArbolCorre(b.cabeza)

    a = NodoAvl("perez")
    b.cabeza = b.insertarActivo(a,b.cabeza)
    b.cabeza, val = b.BalanceFactor(b.cabeza)
    b.cabeza = b.ArbolCorre(b.cabeza)

    a = NodoAvl("jimenez")
    b.cabeza = b.insertarActivo(a,b.cabeza)
    b.cabeza, val = b.BalanceFactor(b.cabeza)
    b.cabeza = b.ArbolCorre(b.cabeza)


    b.graficarAVL(b.cabeza)

    print ("casa")