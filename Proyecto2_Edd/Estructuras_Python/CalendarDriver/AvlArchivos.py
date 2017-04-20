__author__ = 'Samuel'
import os
escritorio = os.path.expanduser("~/Desktop")

class AVL:
    def __init__(self):
        self.raizG=None

    def esHoja(self, nodo):
        if nodo==None:
            return False
        if nodo.derecho!=None or nodo.izquierdo!=None:
            return False
        return True

    def factorEquilibrio(self, raiz):
        if raiz==None:
            return raiz, 0
        if self.esHoja(raiz):
            raiz.fe = 0
            return raiz, 1
        elif raiz.izquierdo and raiz.derecho:
            raiz.izquierdo, valorIz = self.factorEquilibrio(raiz.izquierdo)
            raiz.derecho, valorDer = self.factorEquilibrio(raiz.derecho)
            raiz.fe = valorDer - valorIz
            if valorDer> valorIz:
                return raiz, (1+valorDer)
            else:
                return raiz, (1+valorIz)
        elif raiz.izquierdo:
            raiz.izquierdo, valorIz = self.factorEquilibrio(raiz.izquierdo)
            raiz.fe = valorIz*(-1)
            return raiz, (1+ valorIz)
        elif raiz.derecho:
            raiz.derecho, valorDer = self.factorEquilibrio(raiz.derecho)
            raiz.fe = valorDer
            return raiz, (1+ valorDer)
        return raiz

    def rotacionII(self, rai):
        n0 = rai
        n1 = rai.izquierdo
        n0.izquierdo = n1.derecho
        n1.derecho = n0
        return n1

    def rotacionID(self, rai):
        n0 = rai
        n1 = rai.izquierdo
        n2 = rai.izquierdo.derecho
        n0.izquierdo = n2.derecho
        n1.derecho = n2.izquierdo
        n2.derecho = n0
        n2.izquierdo = n1
        return n2

    def rotacionDD(self, rai):
        n0 = rai
        n1 = rai.derecho
        n0.derecho = n1.izquierdo
        n1.izquierdo = n0
        return n1

    def rotacionDI(self, rai):
        n0 = rai
        n1 = rai.derecho
        n2 = rai.derecho.izquierdo
        n0.derecho = n2.izquierdo
        n1.izquierdo = n2.derecho
        n2.derecho = n1
        n2.izquierdo = n0
        return n2

    def evaluarCasosAVL(self, ra):
        if ra.fe==-2:
            if ra.izquierdo.fe==-1:
                ra = self.rotacionII(ra)
            else:
                ra = self.rotacionID(ra)
        if ra.fe==2:
            if ra.derecho.fe==1:
                ra = self.rotacionDD(ra)
            else:
                ra = self.rotacionDI(ra)
        return ra

    def recorrerArbol(self, ra):
        if ra==None:
            return
        if ra.izquierdo:
           ra.izquierdo = self.recorrerArbol(ra.izquierdo)
        if ra.derecho:
            ra.derecho = self.recorrerArbol(ra.derecho)
        if ra.fe == 2 or ra.fe==-2:
            ra = self.evaluarCasosAVL(ra)
            ra, val = self.factorEquilibrio(ra)
        return ra

    def insertarActivo(self, nodoN, raiz):
        if raiz==None:
            raiz = nodoN

        else:
            if raiz.id > nodoN.id:
                raiz.izquierdo = self.insertarActivo(nodoN, raiz.izquierdo)
            else:
                raiz.derecho = self.insertarActivo(nodoN,raiz.derecho)
        return raiz

    def eliminarActivo(self, raiz, id):
        if raiz == None:
            return
        elif raiz.id > id:
            raiz.izquierdo = self.eliminarActivo(raiz.izquierdo, id)
        elif raiz.id < id:
            raiz.derecho = self.eliminarActivo(raiz.derecho, id)
        else:
            q = raiz
            if q.izquierdo == None:
                raiz = q.derecho
            elif q.derecho== None:
                raiz = q.izquierdo
            else:
                self.reemplazar(q)
            q = None
        return raiz



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





    def graficarAVL(self, raiz):
        if raiz==None:
            print"esta vacio :("
            return
        file = open(escritorio+"\\avl.dot", "w")
        file.write("digraph G{\n")
        file.write(self.graficarNodoAVL(raiz))
        file.write("}\n")
        file.close()
        os.system("dot -Tpng "+escritorio+"\\avl.dot > "+escritorio+"\\avl.png")






    def graficarNodoAVL(self, nodo):
        cadena = "nodo"+self.obtenerHASH(nodo)+"[label=\"<f0>|<f1>"+nodo.nombre+" \\n"+nodo.descripcion+"|<f2>\", shape=record,style=filled,fillcolor=\"blue:cyan\", gradientangle=\"270\"]\n"
        if nodo.izquierdo:
            cadena+=self.graficarNodoAVL(nodo.izquierdo)
            cadena+= "nodo"+self.obtenerHASH(nodo)+":f0 -> "+"nodo"+self.obtenerHASH(nodo.izquierdo)+"\n"
        if nodo.derecho:
            cadena += self.graficarNodoAVL(nodo.derecho)
            cadena += "nodo" + self.obtenerHASH(nodo) + ":f2 -> " + "nodo" + self.obtenerHASH(nodo.derecho)+"\n"
        return cadena






    def obtenerHASH(self, objeto):
        id = hash(objeto)
        if int(id) < 0:
            return str((-1 * id))
        return str(id)



    def modificarActivo(self, id, nuevaD, raiz):
        if raiz==None:
            return raiz
        if raiz.id == id:
            raiz.descripcion = nuevaD
            return raiz
        if raiz.id<id:
            raiz.derecho = self.modificarActivo(id, nuevaD, raiz.derecho)
            return raiz
        if raiz.id>id:
            raiz.izquierdo = self.modificarActivo(id, nuevaD, raiz.izquierdo)
            return raiz
        return raiz






    def retornarID(self, raiz):
        cadena = ""
        if raiz==None:
            return cadena
        cadena+= raiz.id+","+raiz.nombre+","+raiz.descripcion
        if raiz.derecho:
            cadena+=","+self.retornarID(raiz.derecho)
        if raiz.izquierdo:
            cadena+=","+self.retornarID(raiz.izquierdo)
        print cadena
        return cadena





    def retornarDesripcion(self, raiz, id):
        if raiz==None:
            return "No existe, nada"
        if raiz.id == id:
            return raiz.descripcion+","+raiz.nombre
        if raiz.id<id:
            return self.retornarDesripcion(raiz.derecho, id)
        if raiz.id>id:
            return self.retornarDesripcion(raiz.izquierdo, id)


class Principal2:
    b = AVL()
    b.insertarActivo()
    b.graficarAVL()
    b.graficarNodoAVL()