import os

#NODO ROOT
class nodo_root:
    def __init__(self, arbolB, avl):
        self.texto = "/root"
        self.arbolB = arbolB
        self.avl = avl

    def set_arbolB(self, arbolB):
        self.arbolB = arbolB

    def get_arbolB(self):
        return self.arbolB

    def set_avl(self, avl):
        self.avl = avl

    def get_avl(self):
        return self.avl

    def get_texto(self):
        return self.texto


#NODO LISTA USUARIOS
class nodo_lista:
    def __init__(self, usuario, contrasena, root):
        self.usuario = usuario
        self.contrasena = contrasena
        self.root = root
        self.siguiente = None
        self.anterior = None

    def get_user(self):
        return self.usuario

    def get_contra(self):
        return self.contrasena

    def get_root(self):
        return self.root

#LISTA USUARIOS
class lista_usuarios:
    def __init__(self):
        self.inicio = None

    def ingresar(self, usu, passw):
        aB = ArbolB()
        avl = AVL()
        nodoRoot = nodo_root(aB, avl)
        nuevoNodo = nodo_lista(usu, passw, nodoRoot)

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


#NODO LISTA BITACORA
class nodo_listaBitacora:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.siguiente = None

    def get_descripcion(self):
        return self.descripcion

#LISTA BITACORA
class lista_bitacora:
    def __init__(self):
        self.inicio = None

    def ingresar(self, descrip):
        nuevoNodo = nodo_listaBitacora(descrip)

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

#NODO AVL
class NodoAvl:
    activos = None

    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano
        self.derecho = None
        self.izquierdo = None
        self.fe = 0

    def insertaNombre(self, nombre, tamano):
        nuevo = NodoUsar(nombre, tamano)
        self.activos.cabeza = self.activos.insertarActivo(nuevo, self.activos.cabeza)
        self.activos.cabeza, val = self.activos.BalanceFactor(self.activos.cabeza)
        self.activos.cabeza = self.activos.ArbolCorre(self.activos.cabeza)

#NODO
class NodoUsar:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano
        self.fe = 0

############################
########  AVL
############################
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
        cadena = "nodo"+self.getDispersion(nodo)+"[label=\"<f0>|<f1>"+nodo.nombre+" \\n"+ nodo.tamano +"|<f2>\", shape=record,style=filled,fillcolor=\"blue:cyan\", gradientangle=\"270\"]\n"
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


##############################

#NODO ARBOL B
class Bnodo:
    def __init__(self):
        self.Rama0 = None
        self.Rama1 = None
        self.Rama2 = None
        self.Rama3 = None
        self.Rama4 = None

        self.Clave0 = None
        self.Clave1 = None
        self.Clave2 = None
        self.Clave3 = None
        self.Cuentas = 0


class NodoProyec:
    def __init__(self, carpeta, arbolB, avl):
        self.Carpeta = carpeta
        self.arbolB = arbolB
        self.avl = avl

    def getCarpeta(self):
        return self.Carpeta

    def getB(self):
        return self.arbolB

    def getAVL(self):
        return self.avl


# --------------- Estructura  del B interno metodo -------
class ArbolB:
    def __init__(self):
        self.p = Bnodo()
        self.Xder = Bnodo()
        self.Xizq = Bnodo()
        self.X = None
        self.Xr = None
        self.EmpA = False
        self.Esta = False
        self.val = 0
        self.buffer = ""

    def Inserta(self, clave):
        self.Insertaa(clave, self.p)

    def Insertaa(self, clave, raiz):
        self.Empujar(clave, raiz)
        if self.EmpA:
            self.p = Bnodo()
            self.p.Cuentas = 1
            self.p.Clave0 = self.X
            self.p.Rama0 = raiz
            self.p.Rama1 = self.Xr

    def Empujar(self, clave, raiz):
        k = 0
        self.Esta = False

        if self.Vacio(raiz):
            self.EmpA = True
            self.X = clave
            self.Xr = None
        else:
            k = self.BuscarNodo(clave, raiz)
            if self.Esta:
                self.EmpA = False
            else:
                if k == 4:
                    self.Empujar(clave, raiz.Rama4)

                elif k == 3:
                    self.Empujar(clave, raiz.Rama3)

                elif k == 2:
                    self.Empujar(clave, raiz.Rama2)
                elif k == 1:
                    self.Empujar(clave, raiz.Rama1)
                elif k == 0:
                    self.Empujar(clave, raiz.Rama0)
                else:
                    # os.write("Salir")
                    print("Salir")
                if self.EmpA:
                    if raiz.Cuentas < 4:
                        self.EmpA = False
                        self.MeterHoja(self.X, raiz, k)
                    else:
                        self.EmpA = True
                        self.DividirN(self.X, raiz, k)

    def DividirN(self, Clave, Raiz, k):  # NodoPr, Bnodo y int k
        pos = 0
        Posmda = 0
        if k <= 2:
            Posmda = 2
        else:
            Posmda = 3
        s = Bnodo()
        pos = Posmda + 1

        vale = 0
        while pos != 5:
            vale = (pos - Posmda) - 1
            if Posmda == 2:
                if vale == 1:
                    s.Clave1 = Raiz.Clave3
                    s.Rama2 = Raiz.Rama4
                    break
                elif vale == 0:
                    s.Clave0 = Raiz.Clave2
                    s.Rama1 = Raiz.Rama3
                    break
                else:
                    # os.write("Sin Caso")
                    print("finalizo")
                    break
            elif Posmda == 3:
                if vale == 0:
                    s.Clave0 = Raiz.Clave3
                    s.Rama1 = Raiz.Rama4
                else:
                    break
            pos += 1

        s.Cuentas = 4 - Posmda
        Raiz.Cuentas = Posmda
        if k <= 2:
            self.MeterHoja(Clave, Raiz, k)
        else:
            self.MeterHoja(Clave, s, (k - Posmda))
        vale = Raiz.Cuentas - 1

        if vale == 3:
            self.X = Raiz.Clave3
        elif vale == 2:
            self.X = Raiz.Clave2
        elif vale == 1:
            self.X = Raiz.Clave1
        elif vale == 0:
            self.X = Raiz.Clave0

        vale = Raiz.Cuentas
        if vale == 4:
            s.Rama0 = Raiz.Rama4

        elif vale == 3:
            s.Rama0 = Raiz.Rama3
        elif vale == 2:
            s.Rama0 = Raiz.Rama2
        elif vale == 1:
            s.Rama0 = Raiz.Rama1
        elif vale == 0:
            s.Rama0 = Raiz.Rama0

        Raiz.Cuentas -= 1
        self.Xr = s

    # -------------------------------->
    def MeterHoja(self, clave, raiz, k):  # NodoPr Bnodo int
        i = raiz.Cuentas
        while i != k:
            if i == 3:
                raiz.Clave3 = raiz.Clave2
                raiz.Rama4 = raiz.Rama3
            elif i == 2:
                raiz.Clave2 = raiz.Clave1
                raiz.Rama3 = raiz.Rama2
            elif i == 1:
                raiz.Clave1 = raiz.Clave0
                raiz.Rama2 = raiz.Rama1
            i -= 1

        if k == 3:
            raiz.Clave3 = clave
            raiz.Rama4 = self.Xr
        elif k == 2:
            raiz.Clave2 = clave
            raiz.Rama3 = self.Xr
        elif k == 1:
            raiz.Clave1 = clave
            raiz.Rama2 = self.Xr
        elif k == 0:
            raiz.Clave0 = clave
            raiz.Rama1 = self.Xr
        raiz.Cuentas += 1

    def BuscarNodo(self, clave, raiz):
        j = 0
        if (clave.getCarpeta() == raiz.Clave0.getCarpeta()):
            self.Esta = False
            j = 0
        else:
            j = raiz.Cuentas
            for ii in range(j, 0):
                if raiz.Clave3 != None and ii == 4:
                    if clave.getCarpeta() == raiz.Clave3.getCarpeta() and j > 1:
                        j -= 1
                if raiz.Clave2 != None and ii == 3:
                    if clave.getCarpeta() == raiz.Clave2.getCarpeta() and j > 1:
                        j -= 1
                if raiz.Clave1 != None and ii == 2:
                    if clave.getCarpeta() == raiz.Clave1.getCarpeta() and j > 1:
                        j -= 1
                if raiz.Clave0 != None and ii == 1:
                    if clave.getCarpeta() == raiz.Clave0.getCarpeta() and j > 1:
                        j -= 1
            if j == 4:
                if (raiz.Clave3 != None):
                    self.Esta = (clave.getCarpeta() == raiz.Clave3.getCarpeta())
            elif j == 3:
                if (raiz.Clave2 != None):
                    self.Esta = (clave.getCarpeta() == raiz.Clave2.getCarpeta())
            elif j == 2:
                if (raiz.Clave1 != None):
                    self.Esta = (clave.getCarpeta() == raiz.Clave1.getCarpeta())
            elif j == 1:
                if (raiz.Clave0 != None):
                    self.Esta = (clave.getCarpeta() == raiz.Clave0.getCarpeta())
        return j

    def Miembro(self, clave, raiz):
        si = False
        j = 0
        if self.Vacio(self.p) == False:  # <----Aqui tengo duda
            if clave.Carpeta.CompareTo(raiz.Clave0.Carpeta) < 0:
                si = False
                j = 0
            else:
                j = raiz.Cuentas
                for ii in [0, j]:
                    if raiz.Clave3 != None and ii == 4:
                        if clave.getCarpeta() == raiz.Clave3.getCarpeta() and j > 1:
                            j -= 1
                    if raiz.Clave2 != None and ii == 3:
                        if clave.getCarpeta() == raiz.Clave2.getCarpeta() and j > 1:
                            j -= 1
                    if raiz.Clave1 != None and ii == 2:
                        if clave.getCarpeta() == raiz.Clave1.getCarpeta() and j > 1:
                            j -= 1
                if j == 4:
                    si = (clave.getCarpeta() == raiz.Clave3.getCarpeta())
                elif j == 3:
                    si = (clave.getCarpeta() == raiz.Clave2.getCarpeta())
                elif j == 2:
                    si = (clave.getCarpeta() == raiz.Clave1.getCarpeta())
                elif j == 1:
                    si = (clave.getCarpeta() == raiz.Clave0.getCarpeta())
        return si

    def BusquedaNum(self, identi):
        p = self.p
        k = 0
        c = 0

        while c < 4:
            if c == 0:
                if p.Clave0 == None:
                    break
            elif c == 1:
                if p.Clave1 == None:
                    break
            elif c == 2:
                if p.Clave2 == None:
                    break
            elif c == 3:
                if p.Clave3 == None:
                    break
            if c == 0:
                if p.Clave0.getCarpeta() == identi:
                    os.write("Encontro1")
                    break
            elif c == 1:
                if p.Clave1.getCarpeta() == identi:
                    os.write("Encontro2")
                    break
            elif c == 2:
                if p.Clave2.getCarpeta() == identi:
                    os.write("Encontro3")
                    break
            elif c == 3:
                if p.Clave3.getCarpeta() == identi:
                    os.write("Encontro4")
                    break
            c += 1

        while k < 5 and p.Cuentas >= k:
            if k == 0:
                if p.Rama0 == None:
                    return
                if p.Rama0.Cuentas == 0:
                    return
                elif k == 1:
                    if p.Rama1 == None:
                        return
                    if p.Rama1.Cuentas == 0:
                        return
                elif k == 2:
                    if p.Rama2 == None:
                        return
                    if p.Rama2.Cuentas == 0:
                        return
                elif k == 3:
                    if p.Rama3 == None:
                        return
                    if p.Rama3.Cuentas == 0:
                        return
                elif k == 4:
                    if p.Rama4 == None:
                        return
                    if p.Rama4.Cuentas == 0:
                        return
            self.val += 1
            if k == 0:
                self.RecursivoBusquedaNum(p.Rama0, identi)
                break
            elif k == 1:
                self.RecursivoBusquedaNum(p.Rama1, identi)
                break
            elif k == 2:
                self.RecursivoBusquedaNum(p.Rama2, identi)
                break
            elif k == 3:
                self.RecursivoBusquedaNum(p.Rama3, identi)
                break
            elif k == 4:
                self.RecursivoBusquedaNum(p.Rama4, identi)
                break
            k += 1

    def RecursivoBusquedaNum(self, nodo, identi):
        k = 0
        c = 0
        while c < 4:
            if c != nodo.Cuentas and nodo.Cuentas != 0:
                if c == 0:
                    if nodo.Clave0 == None:
                        break
                    elif c == 1:
                        if nodo.Clave1 == None:
                            break
                    elif c == 2:
                        if nodo.Clave2 == None:
                            break
                    elif c == 3:
                        if nodo.Clave3 == None:
                            break
                if c == 0:
                    if nodo.Clave0.getCarpeta() == identi:
                        os.write("Caso 0")
                        break
                elif c == 1:
                    if nodo.Clave1.getCarpeta() == identi:
                        os.write("Caso 1")
                        break
                elif c == 2:
                    if nodo.Clave2.getCarpeta() == identi:
                        os.write("Caso 2")
                        break
                elif c == 3:
                    if nodo.Clave3.getCarpeta() == identi:
                        os.write("Caso 3")
                        break
                c += 1
            else:
                break
        while k < 5 and nodo.Cuentas >= k:
            if k == 0:
                if nodo.Rama0 == None:
                    return
                if nodo.Rama0.Cuentas == 0:
                    return
            elif k == 1:
                if nodo.Rama1 == None:
                    return
                if nodo.Rama1.Cuentas == 0:
                    return
            elif k == 2:
                if nodo.Rama2 == None:
                    return
                if nodo.Rama2.Cuentas == 0:
                    return
            elif k == 3:
                if nodo.Rama3 == None:
                    return
                if nodo.Rama3.Cuentas == 0:
                    return
            elif k == 4:  # aqui voy
                if nodo.Rama4 == None:
                    return
                if nodo.Rama4.Cuentas == 0:
                    return

                self.val += 1
                if k == 0:
                    self.RecursivoBusquedaNum(nodo.Rama0, identi)
                    break
                elif k == 1:
                    self.RecursivoBusquedaNum(nodo.Rama1, identi)
                    break
                elif k == 2:
                    self.RecursivoBusquedaNum(nodo.Rama2, identi)
                    break
                elif k == 3:
                    self.RecursivoBusquedaNum(nodo.Rama3, identi)
                    break
                elif k == 4:
                    self.RecursivoBusquedaNum(nodo.Rama4, identi)
                    break
                k += 1

        self.nodo_ = None

    def Buscar_Posicion(self, clave, raiz):
        if self.nodo_ != None:
            return self.nodo_

        k = 0
        self.Esta = False
        if self.Vacio(raiz) == False:  # <--------------- Aqui tengo duda
            k = self.BuscarNodo_Val(clave, raiz)
            if self.Esta:
                if k == 4:
                    if raiz.Clave3 != None:
                        return raiz.Clave3
                        # break
                if k == 3:
                    if raiz.Clave2 != None:
                        return raiz.Clave2
                        # break
                if k == 2:
                    if raiz.Clave1 != None:
                        return raiz.Clave1
                        # break
                if k == 1:
                    if raiz.Clave0 != None:
                        return raiz.Clave0
                return self.nodo_
            else:
                if k == 4:
                    self.nodo_ = self.Buscar_Posicion(clave, raiz.Rama4)
                elif k == 3:
                    self.nodo_ = self.Buscar_Posicion(clave, raiz.Rama3)
                elif k == 2:
                    self.nodo_ = self.Buscar_Posicion(clave, raiz.Rama2)
                elif k == 1:
                    self.nodo_ = self.Buscar_Posicion(clave, raiz.Rama1)
                elif k == 0:
                    self.nodo_ = self.Buscar_Posicion(clave, raiz.Rama0)
            return self.nodo_

    def BuscarNodo_Val(self, clave, raiz):
        j = 0
        if clave.CompareTo(raiz.Clave0.getCarpeta()) < 0:
            self.Esta = False
            j = 0
        else:
            j = raiz.Cuentas
            for ii in [j, 0]:  # <------------- Aqui tengo duda
                if raiz.Clave3 != None and ii == 4:
                    if clave == raiz.Clave3.getCarpeta() and j > 1:
                        j -= 1
                if raiz.Clave2 != None and ii == 3:
                    if clave == raiz.Clave2.getCarpeta() and j > 1:
                        j -= 1
                if raiz.Clave1 != None and ii == 2:
                    if clave == raiz.Clave1.getCarpeta() and j > 1:
                        j -= 1
                if raiz.Clave0 != None and ii == 1:
                    if clave == raiz.Clave0.getCarpeta() and j > 1:
                        j -= 1
            if j == 4:
                if raiz.Clave3 != None:
                    self.Esta = (clave == raiz.Clave3.getCarpeta())
            elif j == 3:
                if raiz.Clave2 != None:
                    self.Esta = (clave == raiz.Clave2.getCarpeta())
            elif j == 2:
                if raiz.Clave1 != None:
                    self.Esta = (clave == raiz.Clave1.getCarpeta())
            elif j == 1:
                if raiz.Clave0 != None:
                    self.Esta = (clave == raiz.Clave0.getCarpeta())
        return j

    def Eliminar(self, clave):
        if self.Vacio(self.p):  # Falta agg un parametro
            os.write("Elimina")
        else:
            self.Eliminara(self.p, clave)

    def Eliminara(self, Raiz, clave):
        try:
            self.EliminarRegistro(Raiz, clave)
        except(Exception):
            self.Esta = False
            if self.Esta == False:  # <--------- Aqui tengo duda
                print("Esta")
            else:
                if self.Raiz.Cuentas == 0:
                    Raiz = self.Raiz.Rama0
                self.p = Raiz

    def EliminarRegistro(self, raiz, c):
        self.pos = 0
        # NodoProyec sucesor
        if self.Vacio(raiz):
            Esta = False
        else:
            pos = self.BuscarNodo(c, raiz)
            if self.Esta:
                if (pos - 1) == 4:
                    if (self.Vacio(self.raiz.Rama4)):
                        self.Quitar(self.raiz, pos)
                    else:
                        self.Sucesor(raiz, pos)
                        if pos == 4:
                            self.EliminarRegistro(raiz.Rama4, raiz.Clave3)
                        elif pos == 3:
                            self.EliminarRegistro(raiz.Rama3, raiz.Clave2)
                        elif pos == 2:
                            self.EliminarRegistro(raiz.Rama2, raiz.Clave1)
                        elif pos == 1:
                            self.EliminarRegistro(raiz.Rama1, raiz.Clave0)
                elif (pos - 1) == 3:
                    if self.Vacio(raiz.Rama3):
                        self.Quitar(self.raiz, pos)
                    else:
                        self.Sucesor(raiz, pos)
                        if pos == 4:
                            self.EliminarRegistro(raiz.Rama4, raiz.Clave3)
                        elif pos == 3:
                            self.EliminarRegistro(raiz.Rama3, raiz.Clave2)
                        elif pos == 2:
                            self.EliminarRegistro(raiz.Rama2, raiz.Clave1)
                        elif pos == 1:
                            self.EliminarRegistro(raiz.Rama1, raiz.Clave0)
                elif (pos - 1) == 2:
                    if self.Vacio(raiz.Rama2):
                        self.Quitar(self.raiz, pos)
                    else:
                        self.Sucesor(raiz, pos)
                        if pos == 4:
                            self.EliminarRegistro(raiz.Rama4, raiz.Clave3)
                        elif pos == 3:
                            self.EliminarRegistro(raiz.Rama3, raiz.Clave2)
                        elif pos == 2:
                            self.EliminarRegistro(raiz.Rama2, raiz.Clave1)
                        elif pos == 1:
                            self.EliminarRegistro(raiz.Rama1, raiz.Clave0)
                elif (pos - 1) == 1:
                    if self.Vacio(raiz.Rama1):
                        self.Quitar(self.raiz, pos)
                    else:
                        self.Sucesor(raiz, pos)
                        if pos == 4:
                            self.EliminarRegistro(raiz.Rama4, raiz.Clave3)
                        elif pos == 3:
                            self.EliminarRegistro(raiz.Rama3, raiz.Clave2)
                        elif pos == 2:
                            self.EliminarRegistro(raiz.Rama2, raiz.Clave1)
                        elif pos == 1:
                            self.EliminarRegistro(raiz.Rama1, raiz.Clave0)
                elif (pos - 1) == 0:
                    if self.Vacio(raiz.Rama1):
                        self.Quitar(self.raiz, pos)
                    else:
                        self.Sucesor(raiz, pos)
                        if pos == 4:
                            self.EliminarRegistro(raiz.Rama4, raiz.Clave3)
                        elif pos == 3:
                            self.EliminarRegistro(raiz.Rama3, raiz.Clave2)
                        elif pos == 2:
                            self.EliminarRegistro(raiz.Rama2, raiz.Clave2)
                        elif pos == 1:
                            self.EliminarRegistro(raiz.Rama1, raiz.Clave1)
            else:
                if pos == 4:
                    self.EliminarRegistro(raiz.Rama4, c)
                elif pos == 3:
                    self.EliminarRegistro(raiz.Rama3, c)
                elif pos == 2:
                    self.EliminarRegistro(raiz.Rama2, c)
                elif pos == 1:
                    self.EliminarRegistro(raiz.Rama1, c)
                elif pos == 0:
                    self.EliminarRegistro(raiz.Rama0, c)

                if pos == 4:
                    if raiz.Rama4 != None and raiz.Rama4.Cuentas < 2:
                        self.Restablecer(self.raiz, pos)
                elif pos == 3:
                    if raiz.Rama3 != None and raiz.Rama3.Cuentas < 2:
                        self.Restablecer(self.raiz, pos)
                elif pos == 2:
                    if raiz.Rama2 != None and raiz.Rama2.Cuentas < 2:
                        self.Restablecer(self.raiz, pos)
                elif pos == 1:
                    if raiz.Rama1 != None and raiz.Rama1.Cuentas < 2:
                        self.Restablecer(self.raiz, pos)
                elif pos == 0:
                    if raiz.Rama0 != None and raiz.Rama0.Cuentas < 2:
                        self.Restablecer(self.raiz, pos)

    def Sucesor(self, raiz, k):  # Bnodo, int
        self.q = None
        if k == 4:
            self.q = raiz.Rama4
        elif k == 3:
            self.q = raiz.Rama3
        elif k == 2:
            self.q = raiz.Rama2
        elif k == 1:
            self.q = raiz.Rama1
        elif k == 0:
            self.q = raiz.Rama0

        while self.Vacio(q.Rama0) != False:  # <------------- Con el desigual
            self.q = self.q.Rama0

        if k == 4:
            raiz.Clave3 = self.q.Clave0
        elif k == 3:
            raiz.Clave2 = self.q.Clave0
        elif k == 2:
            raiz.Clave1 = self.q.Clave0
        elif k == 1:
            raiz.Clave0 = self.q.Clave0

    def Combina(self, raiz, pos):
        j = 0
        if pos == 4:
            self.Xder = raiz.Rama4
        elif pos == 3:
            self.Xder = raiz.Rama3
        elif pos == 2:
            self.Xder = raiz.Rama2
        elif pos == 1:
            self.Xder = raiz.Rama1
        elif pos == 0:
            self.Xder = raiz.Rama0

        # if (pos - 1):
        if (pos - 1) == 4:
            self.Xder = raiz.Rama4
        elif (pos - 1) == 3:
            self.Xder = raiz.Rama3
        elif (pos - 1) == 2:
            self.Xder = raiz.Rama2
        elif (pos - 1) == 1:
            self.Xder = raiz.Rama1
        elif (pos - 1) == 0:
            self.Xder = raiz.Rama0
        self.Xizq.Cuentas += 1

        # if self.Xizq.Cuentas - 1:
        if (self.Xizq.Cuentas - 1) == 3:
            if (pos - 1) == 3:
                self.Xizq.Clave3 = raiz.Clave3
            elif (pos - 1) == 2:
                self.Xizq.Clave3 = raiz.Clave2
            elif (pos - 1) == 1:
                self.Xizq.Clave3 = raiz.Clave1
            elif (pos - 1) == 0:
                self.Xizq.Clave3 = raiz.Clave0

        if (self.Xizq.Cuentas - 1) == 2:
            if (pos - 1) == 3:
                self.Xizq.Clave2 = raiz.Clave3
            if (pos - 1) == 2:
                self.Xizq.Clave2 = raiz.Clave2
            if (pos - 1) == 1:
                self.Xizq.Clave2 = raiz.Clave1
            if (pos - 1) == 0:
                self.Xizq.Clave2 = raiz.Clave0

        if (self.Xizq.Cuentas - 1) == 1:
            if (pos - 1) == 3:
                self.Xizq.Clave1 = raiz.Clave3
            if (pos - 1) == 2:
                self.Xizq.Clave1 = raiz.Clave2
            if (pos - 1) == 1:
                self.Xizq.Clave1 = raiz.Clave1
            if (pos - 1) == 0:
                self.Xizq.Clave1 = raiz.Clave0

        if (self.Xizq.Cuentas - 1) == 0:
            if (pos - 1) == 3:
                self.Xizq.Clave0 = raiz.Clave3
            if (pos - 1) == 2:
                self.Xizq.Clave0 = raiz.Clave2
            if (pos - 1) == 1:
                self.Xizq.Clave0 = raiz.Clave1
            if (pos - 1) == 1:
                self.Xizq.Clave0 = raiz.Clave0

        if self.Xizq.Cuentas == 4:
            self.Xizq.Rama4 = self.Xder.Rama0
        if self.Xizq.Cuentas == 3:
            self.Xizq.Rama3 = self.Xder.Rama0
        if self.Xizq.Cuentas == 2:
            self.Xizq.Rama2 = self.Xder.Rama0
        if self.Xizq.Cuentas == 1:
            self.Xizq.Rama1 = self.Xder.Rama0
        if self.Xizq.Cuentas == 0:
            self.Xizq.Rama0 = self.Xder.Rama0

        j = 1
        while (j != self.Xder.Cuentas + 1):
            self.Xizq.Cuentas += 1
            if (self.Xizq.Cuentas - 1) == 3:
                if (j - 1) == 3:
                    self.Xizq.Clave3 = self.Xder.Clave3
                    self.Xizq.Rama4 = self.Xder.Rama4
                if (j - 1) == 2:
                    self.Xizq.Clave3 = self.Xder.Clave2
                    self.Xizq.Rama4 = self.Xder.Rama3
                if (j - 1) == 1:
                    self.Xizq.Clave3 = self.Xder.Clave1
                    self.Xizq.Rama4 = self.Xder.Rama2
                if (j - 1) == 0:
                    self.Xizq.Clave3 = self.Xder.Clave0
                    self.Xizq.Rama4 = self.Xder.Rama1
                break

            if (self.Xizq.Cuentas - 1) == 2:
                if (j - 1) == 3:
                    self.Xizq.Clave2 = self.Xder.Clave3
                    self.Xizq.Rama3 = self.Xder.Rama4
                if (j - 1) == 2:
                    self.Xizq.Clave2 = self.Xder.Clave2
                    self.Xizq.Rama3 = self.Xder.Rama3
                if (j - 1) == 1:
                    self.Xizq.Clave2 = self.Xder.Clave1
                    self.Xizq.Rama3 = self.Xder.Rama2
                if (j - 1) == 0:
                    self.Xizq.Clave2 = self.Xder.Clave0
                    self.Xizq.Rama3 = self.Xder.Rama1
                break

            if (self.Xizq.Cuentas - 1) == 1:
                if (pos - 1) == 3:
                    self.Xizq.Clave1 = self.Xder.Clave3
                    self.Xizq.Rama2 = self.Xder.Rama4
                if (pos - 1) == 2:
                    self.Xizq.Clave1 = self.Xder.Clave2
                    self.Xizq.Rama2 = self.Xder.Rama3
                if (pos - 1) == 1:
                    self.Xizq.Clave1 = self.Xder.Clave1
                    self.Xizq.Rama2 = self.Xder.Rama2
                if (pos - 1) == 0:
                    self.Xizq.Clave1 = self.Xder.Clave0
                    self.Xizq.Rama2 = self.Xder.Rama1
                break

            if (self.Xizq.Cuentas - 1) == 0:
                if (pos - 1) == 3:
                    self.Xizq.Clave0 = self.Xder.Clave3
                    self.Xizq.Rama1 = self.Xder.Rama4
                if (pos - 1) == 2:
                    self.Xizq.Clave0 = self.Xder.Clave2
                    self.Xizq.Rama1 = self.Xder.Rama3
                if (pos - 1) == 1:
                    self.Xizq.Clave0 = self.Xder.Clave1
                    self.Xizq.Rama1 = self.Xder.Rama2
                if (pos - 1) == 0:
                    self.Xizq.Clave0 = self.Xder.Clave0
                    self.Xizq.Rama1 = self.Xder.Rama1
                break
            j += 1
        self.Quitar(raiz, pos)

    def MoverDer(self, raiz, pos):  # Bnodo, int
        self.i = 0
        if pos == 4:
            self.i = raiz.Rama4.Cuentas
        elif pos == 3:
            self.i = raiz.Rama3.Cuentas
        elif pos == 2:
            self.i = raiz.Rama2.Cuentas
        elif pos == 1:
            self.i = raiz.Rama1.Cuentas
        elif pos == 0:
            self.i = raiz.Rama0.Cuentas

        while self.i != 0:
            if self.i == 3:
                if pos == 4:
                    raiz.Rama4.Clave3 = raiz.Rama4.Clave2
                    raiz.Rama4.Rama4 = raiz.Rama4.Rama3
                elif pos == 3:
                    raiz.Rama3.Clave3 = raiz.Rama3.Clave2
                    raiz.Rama3.Rama4 = raiz.Rama3.Rama3
                elif pos == 2:
                    raiz.Rama2.Clave3 = raiz.Rama2.Clave2
                    raiz.Rama2.Rama4 = raiz.Rama2.Rama3
                elif pos == 1:
                    raiz.Rama1.Clave3 = raiz.Rama1.Clave2
                    raiz.Rama1.Rama4 = raiz.Rama1.Rama3
                elif pos == 0:
                    raiz.Rama0.Clave3 = raiz.Rama0.Clave2
                    raiz.Rama0.Rama4 = raiz.Rama0.Rama3
                break

            if self.i == 2:
                if pos == 4:
                    raiz.Rama4.Clave2 = raiz.Rama4.Clave1
                    raiz.Rama4.Rama3 = raiz.Rama4.Rama2
                elif pos == 3:
                    raiz.Rama3.Clave2 = raiz.Rama3.Clave1
                    raiz.Rama3.Rama3 = raiz.Rama3.Rama2
                elif pos == 2:
                    raiz.Rama2.Clave2 = raiz.Rama2.Clave1
                    raiz.Rama2.Rama3 = raiz.Rama2.Rama2
                elif pos == 1:
                    raiz.Rama1.Clave2 = raiz.Rama1.Clave1
                    raiz.Rama1.Rama3 = raiz.Rama1.Rama2
                elif pos == 0:
                    raiz.Rama0.Clave2 = raiz.Rama0.Clave1
                    raiz.Rama0.Rama3 = raiz.Rama0.Rama2
                break

            if self.i == 1:
                if pos == 4:
                    raiz.Rama4.Clave1 = raiz.Rama4.Clave0
                    raiz.Rama4.Rama2 = raiz.Rama4.Rama1
                elif pos == 3:
                    raiz.Rama3.Clave1 = raiz.Rama3.Clave0
                    raiz.Rama3.Rama2 = raiz.Rama3.Rama1
                elif pos == 2:
                    raiz.Rama2.Clave1 = raiz.Rama2.Clave0
                    raiz.Rama2.Rama2 = raiz.Rama2.Rama1
                elif pos == 1:
                    raiz.Rama1.Clave1 = raiz.Rama1.Clave0
                    raiz.Rama1.Rama2 = raiz.Rama1.Rama1
                elif pos == 0:
                    raiz.Rama0.Clave1 = raiz.Rama0.Clave0
                    raiz.Rama0.Rama2 = raiz.Rama0.Rama1
                break
        self.i -= 1

        if pos == 4:  # por aqui voy---------------
            raiz.Rama4.Cuentas += 1
            raiz.Rama4.Rama1 = raiz.Rama4.Rama0
            raiz.Rama4.Clave0 = raiz.Clave3
            if (raiz.Rama3.Cuentas - 1) == 3:
                raiz.Clave3 = raiz.Rama3.Clave3
            elif (raiz.Rama3.Cuentas - 1) == 2:
                raiz.Clave3 = raiz.Rama3.Clave2
            elif (raiz.Rama3.Cuentas - 1) == 1:
                raiz.Clave3 = raiz.Rama3.Clave1
            elif (raiz.Rama3.Cuentas - 1) == 0:
                raiz.Clave3 = raiz.Rama3.Clave0

            if (raiz.Rama3.Cuentas - 1) == 3:
                raiz.Clave3 = raiz.Rama3.Clave3
            elif (raiz.Rama3.Cuentas - 1) == 2:
                raiz.Clave3 = raiz.Rama3.Clave2
            elif (raiz.Rama3.Cuentas - 1) == 1:
                raiz.Clave3 = raiz.Rama3.Clave1
            elif (raiz.Rama3.Cuentas - 1) == 0:
                raiz.Clave3 = raiz.Rama3.Clave0

            if (raiz.Rama3.Cuentas) == 4:
                raiz.Rama4.Rama0 = raiz.Rama3.Rama4
            elif (raiz.Rama3.Cuentas) == 3:
                raiz.Rama4.Rama0 = raiz.Rama3.Rama3
            elif (raiz.Rama3.Cuentas) == 2:
                raiz.Rama4.Rama0 = raiz.Rama3.Rama2
            elif (raiz.Rama3.Cuentas) == 1:
                raiz.Rama4.Rama0 = raiz.Rama3.Rama1
            elif (raiz.Rama4.Cuentas) == 0:
                raiz.Rama4.Rama0 = raiz.Rama3.Rama0
            self.raiz.Rama3.Cuentas -= 1

        elif pos == 3:
            raiz.Rama3.Cuentas = raiz.Rama3.Cuentas + 1
            raiz.Rama3.Rama1 = raiz.Rama3.Rama0
            raiz.Rama3.Clave0 = raiz.Clave2
            if (raiz.Rama2.Cuentas - 1) == 3:
                raiz.Clave2 = raiz.Rama2.Clave3
            elif (raiz.Rama2.Cuentas - 1) == 2:
                raiz.Clave2 = raiz.Rama2.Clave3
            elif (raiz.Rama2.Cuentas - 1) == 1:
                raiz.Clave2 = raiz.Rama2.Clave1
            elif (raiz.Rama2.Cuentas - 1) == 0:
                raiz.Clave2 = raiz.Rama2.Clave0

            if (raiz.Rama2.Cuentas) == 4:
                raiz.Rama3.Rama0 = raiz.Rama2.Rama4
            elif (raiz.Rama2.Cuentas) == 3:
                raiz.Rama3.Rama0 = raiz.Rama2.Rama3
            elif (raiz.Rama2.Cuentas) == 2:
                raiz.Rama3.Rama0 = raiz.Rama2.Rama2
            elif (raiz.Rama2.Cuentas) == 1:
                raiz.Rama3.Rama0 = raiz.Rama2.Rama1
            elif (raiz.Rama2.Cuentas) == 0:
                raiz.Rama3.Rama0 = raiz.Rama2.Rama0
            self.raiz.Rama2.Cuentas -= 1

        elif pos == 2:
            raiz.Rama2.Cuentas = raiz.Rama2.Cuentas + 1
            raiz.Rama2.Rama1 = raiz.Rama2.Rama0
            raiz.Rama2.Clave0 = raiz.Clave1
            if (raiz.Rama1.Cuentas - 1) == 3:
                raiz.Clave1 = raiz.Rama1.Clave3
            elif (raiz.Rama1.Cuentas - 1) == 2:
                raiz.Clave1 = raiz.Rama1.Clave2
            elif (raiz.Rama1.Cuentas - 1) == 1:
                raiz.Clave1 = raiz.Rama1.Clave1
            elif (raiz.Rama1.Cuentas - 1) == 0:
                raiz.Clave1 = raiz.Rama1.Clave0

            if (raiz.Rama1.Cuentas) == 4:
                raiz.Rama2.Rama0 = raiz.Rama1.Rama4
            elif (raiz.Rama1.Cuentas) == 3:
                raiz.Rama2.Rama0 = raiz.Rama1.Rama3
            elif (raiz.Rama1.Cuentas) == 2:
                raiz.Rama2.Rama0 = raiz.Rama1.Rama2
            elif (raiz.Rama2.Cuentas) == 1:
                raiz.Rama2.Rama0 = raiz.Rama1.Rama1
            elif (raiz.Rama2.Cuentas) == 0:
                raiz.Rama2.Rama0 = raiz.Rama1.Rama0
            raiz.Rama1.Cuentas -= 1

        elif pos == 1:
            raiz.Rama1.Cuentas = raiz.Rama1.Cuentas + 1
            raiz.Rama1.Rama1 = raiz.Rama1.Rama0
            raiz.Rama1.Clave0 = raiz.Clave0
            if (raiz.Rama0.Cuentas - 1) == 3:
                raiz.Clave0 = raiz.Rama0.Clave3
            elif (raiz.Rama0.Cuentas - 1) == 2:
                raiz.Clave0 = raiz.Rama0.Clave2
            elif (raiz.Rama0.Cuentas - 1) == 1:
                raiz.Clave0 = raiz.Rama0.Clave1
            elif (raiz.Rama0.Cuentas - 1) == 0:
                raiz.Clave0 = raiz.Rama0.Clave0

            if (raiz.Rama0.Cuentas) == 4:
                raiz.Rama1.Rama0 = raiz.Rama0.Rama4
            elif (raiz.Rama0.Cuentas) == 3:
                raiz.Rama1.Rama0 = raiz.Rama0.Rama3
            elif (raiz.Rama0.Cuentas) == 2:
                raiz.Rama1.Rama0 = raiz.Rama0.Rama2
            elif (raiz.Rama0.Cuentas) == 1:
                raiz.Rama1.Rama0 = raiz.Rama0.Rama1
            elif (raiz.Rama0.Cuentas) == 0:
                raiz.Rama1.Rama0 = raiz.Rama0.Rama0
            raiz.Rama0.Cuentas -= 1

    def MoverIzq(self, raiz, pos):
        i = 0
        posv = 0
        if pos == 4:
            posv = raiz.Rama4.Cuentas + 1
            raiz.Rama4.Cuentas = raiz.Rama4.Cuentas + 1
            if (raiz.Rama3.Cuentas - 1) == 3:
                raiz.Rama3.Clave3 = raiz.Clave3
                raiz.Rama3.Rama4 = raiz.Rama4.Rama0
            elif (raiz.Rama3.Cuentas - 1) == 2:
                raiz.Rama3.Clave2 = raiz.Clave3
                raiz.Rama3.Rama2 = raiz.Rama4.Rama0
            elif (raiz.Rama3.Cuentas - 1) == 1:
                raiz.Rama3.Clave1 = raiz.Clave3
                raiz.Rama3.Rama1 = raiz.Rama4.Rama0
            elif (raiz.Rama3.Cuentas - 1) == 0:
                raiz.Rama3.Clave0 = raiz.Clave3
                raiz.Rama3.Rama0 = raiz.Rama4.Rama0
            raiz.Clave3 = raiz.Rama4.Clave0
            raiz.Rama4.Rama0 = raiz.Rama4.Rama1
            raiz.Rama4.Cuentas -= 1
            i = 1

        elif pos == 3:
            posv = raiz.Rama3.Cuentas + 1
            raiz.Rama3.Cuentas = raiz.Rama3.Cuentas + 1
            if (raiz.Rama2.Cuentas - 1) == 3:
                raiz.Rama2.Clave3 = raiz.Clave2
                raiz.Rama2.Rama4 = raiz.Rama3.Rama0
            elif (raiz.Rama2.Cuentas - 1) == 2:
                raiz.Rama2.Clave2 = raiz.Clave2
                raiz.Rama2.Rama2 = raiz.Rama3.Rama0
            elif (raiz.Rama2.Cuentas - 1) == 1:
                raiz.Rama2.Clave1 = raiz.Clave2
                raiz.Rama2.Rama1 = raiz.Rama3.Rama0
            elif (raiz.Rama2.Cuentas - 1) == 0:
                raiz.Rama2.Clave0 = raiz.Clave2
                raiz.Rama2.Rama0 = raiz.Rama3.Rama0
            raiz.Clave2 = raiz.Rama3.Clave0
            raiz.Rama3.Rama0 = raiz.Rama3.Rama1
            raiz.Rama3.Cuentas -= 1
            i = 1

        elif pos == 2:
            posv = raiz.Rama2.Cuentas + 1
            raiz.Rama2.Cuentas = raiz.Rama.Cuentas + 1
            if (raiz.Rama1.Cuentas - 1) == 3:
                raiz.Rama1.Clave3 = raiz.Clave1
                raiz.Rama1.Rama4 = raiz.Rama2.Rama0
            elif (raiz.Rama1.Cuentas - 1) == 2:
                raiz.Rama1.Clave2 = raiz.Clave1
                raiz.Rama1.Rama2 = raiz.Rama2.Rama0
            elif (raiz.Rama1.Cuentas - 1) == 1:
                raiz.Rama1.Clave1 = raiz.Clave1
                raiz.Rama1.Rama1 = raiz.Rama2.Rama0
            elif (raiz.Rama1.Cuentas - 1) == 0:
                raiz.Rama1.Clave0 = raiz.Clave1
                raiz.Rama1.Rama0 = raiz.Rama2.Rama0
            raiz.Clave1 = raiz.Rama2.Clave0
            raiz.Rama2.Rama0 = raiz.Rama2.Rama1
            raiz.Rama2.Cuentas -= 1
            i = 1
        elif pos == 1:
            posv = raiz.Rama1.Cuentas + 1
            raiz.Rama1.Cuentas = raiz.Rama1.Cuentas + 1
            if (raiz.Rama0.Cuentas - 1) == 3:
                raiz.Rama0.Clave3 = raiz.Clave1
                raiz.Rama0.Rama4 = raiz.Rama1.Rama0
            elif (raiz.Rama0.Cuentas - 1) == 2:
                raiz.Rama0.Clave2 = raiz.Clave1
                raiz.Rama0.Rama2 = raiz.Rama1.Rama0
            elif (raiz.Rama0.Cuentas - 1) == 1:
                raiz.Rama0.Clave1 = raiz.Clave1
                raiz.Rama0.Rama1 = raiz.Rama1.Rama0
            elif (raiz.Rama0.Cuentas - 1) == 0:
                raiz.Rama0.Clave0 = raiz.Clave1
                raiz.Rama0.Rama0 = raiz.Rama1.Rama0
            raiz.Clave0 = raiz.Rama1.Clave0
            raiz.Rama1.Rama0 = raiz.Rama1.Rama1
            raiz.Rama1.Cuentas -= 1
            i = 1
        elif pos == 0:
            print("Salta -> jmp")

        while i != posv:
            if pos == 0:
                if i == 1:
                    raiz.Rama0.Clave0 = raiz.Rama0.Clave1
                    raiz.Rama0.Rama1 = raiz.Rama0.Rama2
                    break
                elif i == 2:
                    raiz.Rama0.Clave1 = raiz.Rama0.Clave2
                    raiz.Rama0.Rama2 = raiz.Rama0.Rama3
                    break
                elif i == 3:
                    raiz.Rama0.Clave2 = raiz.Rama0.Clave3
                    raiz.Rama0.Rama3 = raiz.Rama0.Rama4
                    break
            elif pos == 1:
                if i == 1:
                    raiz.Rama1.Clave0 = raiz.Rama1.Clave1
                    raiz.Rama1.Rama1 = raiz.Rama1.Rama2
                    break
                elif i == 2:
                    raiz.Rama1.Clave1 = raiz.Rama1.Clave2
                    raiz.Rama1.Rama2 = raiz.Rama1.Rama3
                    break
                elif i == 3:
                    raiz.Rama1.Clave2 = raiz.Rama1.Clave3
                    raiz.Rama1.Rama3 = raiz.Rama1.Rama4
                    break
            elif pos == 2:
                if i == 1:
                    raiz.Rama2.Clave0 = raiz.Rama2.Clave1
                    raiz.Rama2.Rama1 = raiz.Rama2.Rama2
                    break
                elif i == 2:
                    raiz.Rama2.Clave1 = raiz.Rama2.Clave2
                    raiz.Rama2.Rama2 = raiz.Rama2.Rama3
                    break
                elif i == 3:
                    raiz.Rama2.Clave2 = raiz.Rama2.Clave3
                    raiz.Rama2.Rama3 = raiz.Rama2.Rama4
                    break

            elif pos == 3:
                if i == 1:
                    raiz.Rama3.Clave0 = raiz.Rama3.Clave1
                    raiz.Rama3.Rama1 = raiz.Rama3.Rama2
                    break
                elif i == 2:
                    raiz.Rama3.Clave1 = raiz.Rama3.Clave2
                    raiz.Rama3.Rama2 = raiz.Rama3.Rama3
                    break
                elif i == 3:
                    raiz.Rama3.Clave2 = raiz.Rama3.Clave3
                    raiz.Rama3.Rama3 = raiz.Rama3.Rama4
                    break
            elif pos == 4:
                if i == 1:
                    raiz.Rama4.Clave0 = raiz.Rama4.Clave1
                    raiz.Rama4.Rama1 = raiz.Rama4.Rama2
                    break
                elif i == 2:
                    raiz.Rama4.Clave1 = raiz.Rama4.Clave2
                    raiz.Rama4.Rama2 = raiz.Rama4.Rama3
                    break
                elif i == 3:
                    raiz.Rama4.Clave2 = raiz.Rama4.Clave3
                    raiz.Rama4.Rama3 = raiz.Rama4.Rama4
                    break
            i = i + 1

    def Quitar(self, raiz, pos):
        j = pos + 1
        while (j != raiz.self.Cuentas + 1):
            if j == 4:
                raiz.Clave2 = raiz.Clave3
                raiz.Rama3 = raiz.Rama4
                break
            elif j == 3:
                raiz.Clave1 = raiz.Clave2
                raiz.Rama2 = raiz.Rama3
                break
            elif j == 2:
                raiz.Clave0 = raiz.Clave1
                raiz.Rama1 = raiz.Rama2
                break
            elif j == 1:
                break
            elif j == 0:
                break
        j += 1
        raiz.Cuentas -= 1

    def Restablecer(self, raiz, pos):
        if pos > 0:
            if pos == 4:
                if raiz.Rama3.Cuentas > 2:
                    self.MoverDer(raiz, pos)
                else:
                    self.Combina(raiz, pos)
            elif pos == 3:
                if raiz.Rama2.Cuentas > 2:
                    self.MoverDer(raiz, pos)
                else:
                    self.Combina(raiz, pos)
            elif pos == 2:
                if raiz.Rama1.Cuentas > 2:
                    self.MoverDer(raiz, pos)
                else:
                    self.Combina(raiz, pos)
            elif pos == 1:
                if raiz.Rama0.Cuentas > 2:
                    self.MoverDer(raiz, pos)
                else:
                    self.Combina(raiz, pos)
        elif raiz.Rama1.Cuentas > 2:
            self.MoverIzq(raiz, 1)
        else:
            self.Combina(raiz, 1)

    def Vacio(self, raiz):
        return raiz is None or raiz.Cuentas == 0


# ---------------- Grafico del Arbol B ---------------
class Graficar_Arbol_B:
    def __init__(self):
        self.lista = []
        self.desktop = None
        self.contador = 0
        self.ruta_file = ""
        self.val = 0
        self.raiz = None

    def Graficar_File(self, nodo):  # Bnodo
        # self.a = ArbolB()
        self.val = 0
        global archivo
        # if self.Vacio(self.raiz) == True:
        #   return
        # else:
        archivo = open("grafica_BCarpeta.dot", "w")
        archivo.write("\ndigraph G{\r\n node [shape=record] ;\n")

        # Graficar_Arbol_B()
        self.Graficar_B(nodo)
        archivo.write("}")
        archivo.close()
        os.system("dot -Tpng grafica_BCarpeta.dot > grafica_BCarpeta.png")

    def Graficar_B(self, nodo):
        k = 0
        c = 0
        archivo.write("Nodo" + str(self.val) + "[label=\"<P1>")
        while (c < 4):
            if c == 0:
                if (nodo.Clave0 == None):
                    break
            elif c == 1:
                if (nodo.Clave1 == None):
                    break
            elif c == 2:
                if (nodo.Clave2 == None):
                    break
            elif c == 3:
                if (nodo.Clave3 == None):
                    break
            if c == 0:
                archivo.write("|" + nodo.Clave0.getCarpeta())
                archivo.write("|<P" + str(c + 1) + ">")
            elif c == 1:
                archivo.write("|" + nodo.Clave1.getCarpeta())
                archivo.write("|<P" + str(c + 1) + ">")
            elif c == 2:
                archivo.write("|" + nodo.Clave2.getCarpeta())
                archivo.write("|<P" + str(c + 1) + ">")
            elif c == 3:
                archivo.write("|" + nodo.Clave3.getCarpeta())
                archivo.write("|<P" + str(c + 1) + ">")
            c += 1

        archivo.write("\"];\n")
        pasa = "Nodo" + str(self.val)
        while (k < 5 and nodo.Cuentas >= k):
            if k == 0:
                if nodo.Rama0 == None:
                    return
                if nodo.Rama0.Cuentas == 0:
                    return
            elif k == 1:
                if nodo.Rama1 == None:
                    return
                if nodo.Rama1.Cuentas == 0:
                    return
            elif k == 2:
                if nodo.Rama2 == None:
                    return
                if nodo.Rama2.Cuentas == 0:
                    return
            elif k == 3:
                if nodo.Rama3 == None:
                    return
                if nodo.Rama3.Cuentas == 0:
                    return
            elif k == 4:
                if nodo.Rama4 == None:
                    return
                if nodo.Rama4.Cuentas == 0:
                    return
            self.val += 1
            archivo.write(pasa + ":P" + str(k) + " -> " + "Nodo" + str(self.val) + ";\n")
            if k == 0:
                self.RecursivoGrafica(nodo.Rama0)
            elif k == 1:
                self.RecursivoGrafica(nodo.Rama1)
            elif k == 2:
                self.RecursivoGrafica(nodo.Rama2)
            elif k == 3:
                self.RecursivoGrafica(nodo.Rama3)
            elif k == 4:
                self.RecursivoGrafica(nodo.Rama4)
            k += 1

    def RecursivoGrafica(self, nodo):
        k = 0
        c = 0
        archivo.write("Nodo" + str(self.val) + "[label=\"<PO>")

        while (c < 4):
            if c != nodo.Cuentas and nodo.Cuentas != 0:
                if (c == 0):
                    if (nodo.Clave0 == None):
                        break
                elif (c == 1):
                    if (nodo.Clave1 == None):
                        break
                elif (c == 2):
                    if (nodo.Clave2 == None):
                        break
                elif (c == 3):
                    if (nodo.Clave3 == None):
                        break

                if c == 0:
                    archivo.write("|" + nodo.Clave0.getCarpeta())
                    archivo.write("|<P" + str(c + 1) + ">")
                elif c == 1:
                    archivo.write("|" + nodo.Clave1.getCarpeta())
                    archivo.write("|<P" + str(c + 1) + ">")
                elif c == 2:
                    archivo.write("|" + nodo.Clave2.getCarpeta())
                    archivo.write("|<P" + str(c + 1) + ">")
                elif c == 3:
                    archivo.write("|" + nodo.Clave3.getCarpeta())
                    archivo.write("|<P" + str(c + 1) + ">")
                c += 1

            else:
                break
        archivo.write("\"];\n")
        self.pasa = "Nodo" + str(self.val)
        while k < 5 and nodo.Cuentas >= k:
            if k == 0:
                if nodo.Rama0 == None:
                    return
                if nodo.Rama0.Cuentas == 0:
                    return
            elif (k == 1):
                if nodo.Rama1 == None:
                    return
                if nodo.Rama1.Cuentas == 0:
                    return
            elif (k == 2):
                if nodo.Rama2 == None:
                    return
                if nodo.Rama2.Cuentas == 0:
                    return
            elif (k == 3):
                if nodo.Rama3 == None:
                    return
                if nodo.Rama3.Cuentas == 0:
                    return
            elif (k == 4):
                if nodo.Rama4 == None:
                    return
                if nodo.Rama4.Cuentas == 0:
                    return

            self.val += 1
            archivo.write(self.pasa + ":P" + str(k) + " -> " + "Nodo" + str(self.val) + ";\n")
            if k == 0:
                self.RecursivoGrafica(nodo.Rama0)
            elif k == 1:
                self.RecursivoGrafica(nodo.Rama1)
            elif k == 2:
                self.RecursivoGrafica(nodo.Rama2)
            elif k == 3:
                self.RecursivoGrafica(nodo.Rama3)
            elif k == 4:
                self.RecursivoGrafica(nodo.Rama4)
            k += 1

    # Falta Graficar_FileII(usuario, dpto, nodo )



    def Graficar_FileII(self, carpeta, nodo):  # Bnodo
        global archivo
        #  if self.Vacio(self.raiz) == True:
        #      return
        #  else:
        archivo = open("grafica_BCarpeta.dot", "w")
        archivo.write("\ndigraph G{\r\n node [shape=record] ;\n")
        self.GraficarListadoB(nodo, carpeta)
        archivo.write("}")
        archivo.close()
        os.system("dot -Tpng grafica_BCarpeta.dot > grafica_BCarpeta.png")

    # global nodoB
    def GraficarListadoB(self, nodo, carpeta):
        k = 0
        c = 0
        while (c < 4):
            if c == 0:
                if nodo.Clave0 == None:
                    break
            elif c == 1:
                if nodo.Clave1 == None:
                    break
            elif c == 2:
                if nodo.Clave2 == None:
                    break
            elif c == 3:
                if nodo.Clave3 == None:
                    break
            if c == 0:
                if carpeta == (nodo.Clave0.getCarpeta()):
                    archivo.write("Node" + str(self.nodoB) + "[label=\"" + nodo.Clave0.getCarpeta())
                    archivo.write("\", shape=\"box\", style=filled ];")
                    self.lista.append(nodo.Clave0.getCarpeta())
                    self.nodoB += 1
                    break
            elif c == 1:
                if carpeta == nodo.Clave1.getCarpeta():
                    archivo.write("Node" + str(self.nodoB) + "[label=\"" + nodo.Clave1.getCarpeta())
                    archivo.write("\", shape=\"box\", style=filled ];")
                    self.lista.append(nodo.Clave1.getCarpeta())
                    self.nodoB += 1
                    break
            elif c == 2:
                if carpeta == nodo.Clave2.getCarpeta():
                    archivo.write("Node" + str(self.nodoB) + "[label=\"" + nodo.Clave2.getCarpeta())
                    archivo.write("\", shape=\"box\", style=filled ];")
                    self.lista.append(nodo.Clave2.getCarpeta())
                    self.nodoB += 1
                    break
            elif c == 3:
                if carpeta == nodo.Clave3.getCarpeta():
                    archivo.write("Node" + str(self.nodoB) + "[label=\"" + nodo.Clave3.getCarpeta())
                    archivo.write("\", shape=\"box\", style=filled];")
                    self.lista.append(nodo.Clave3.getCarpeta())
                    self.nodoB += 1
                    break
            c += 1
        self.pasa = "Nodo" + str(self.val)

        while (k < 5 and nodo.Cuentas >= k):
            if k == 0:
                if (nodo.Rama0 == None):
                    return
                if (nodo.Rama0.Cuentas == None):
                    return
            elif k == 1:
                if (nodo.Rama1 == None):
                    return
                if (nodo.Rama1.Cuentas == 0):
                    return
            elif k == 2:
                if (nodo.Rama2 == None):
                    return
                if (nodo.Rama2.Cuentas == 0):
                    return
            elif (k == 3):
                if (nodo.Rama3 == None):
                    return
                if (nodo.Rama3.Cuentas == 0):
                    return
            elif (k == 4):
                if (nodo.Rama4 == None):
                    break
                if (nodo.Rama4.Cuentas == 0):
                    return

            self.val += 1
            if k == 0:
                # self.RecursivoGrafica(carpeta, nodo.Rama0)
                self.RecursivoListado(carpeta, nodo.Rama0)
                break
            elif k == 1:
                # self.RecursivoGrafica(carpeta, nodo.Rama1)
                self.RecursivoListado(carpeta, nodo.Rama1)
                break
            elif k == 2:
                # self.RecursivoGrafica(carpeta, nodo.Rama2)
                self.RecursivoListado(carpeta, nodo.Rama2)
                break
            elif k == 3:
                # self.RecursivoGrafica(carpeta, nodo.Rama3)
                self.RecursivoListado(carpeta, nodo.Rama3)
                break
            elif k == 4:
                # self.RecursivoGrafica(carpeta, nodo.Rama4)
                self.RecursivoListado(carpeta, nodo.Rama4)
                break
            k += 1

    def RecursivoListado(self, carpeta, nodo):
        k = 0
        c = 0
        while (c < 4):
            if (c != nodo.Cuentas and nodo.Cuentas != 0):
                if c == 0:
                    if nodo.Clave0 == None:
                        break
                elif c == 1:
                    if nodo.Clave1 == None:
                        break
                elif c == 2:
                    if nodo.Clave2 == None:
                        break
                elif c == 3:
                    if nodo.Clave3 == None:
                        break
                if c == 0:
                    if carpeta.Equals(nodo.Clave0.getCarpeta()):
                        archivo.write("Node" + str(self.nodoB) + "[label=\"" + nodo.Clave0.getCarpeta())
                        archivo.write("\", shape=\"box\", style=filled ];")
                        self.lista.append(nodo.Clave0.getCarpeta())
                        self.nodoB += 1
                        break
                elif c == 1:
                    if carpeta.Equals(nodo.Clave1.getCarpeta()):
                        archivo.write("Node" + str(self.nodoB) + "[label=\"" + nodo.Clave1.getCarpeta())
                        archivo.write("\", shape=\"box\", style=filled];")
                        self.lista.append(nodo.Clave1.getCarpeta())
                        self.nodoB += 1
                        break
                elif c == 2:
                    if carpeta.Equals(nodo.Clave2.getCarpeta()):
                        archivo.write("Node" + str(self.nodoB) + "[label=\"" + nodo.Clave2.getCarpeta())
                        archivo.write("\", shape=\"box\", style=filled];")
                        self.lista.append(nodo.Clave2.getCarpeta())
                        self.nodoB += 1
                        break
                elif c == 3:
                    if carpeta.Equals(nodo.Clave3.getCarpeta()):
                        archivo.write("Node" + str(self.nodoB) + "[label=\"" + nodo.Clave3.getCarpeta())
                        archivo.write("\", shape=\"box\", style=filled];")
                        self.lista.append(nodo.Clave3.getCarpeta())
                        self.nodoB += 1
                        break
                c += 1

            else:
                break

        while (k < 5 and nodo.Cuentas >= k):
            if (k == 0):
                if (nodo.Rama0 == None):
                    return
                if (nodo.Rama0.Cuentas == 0):
                    return
            elif (k == 1):
                if (nodo.Rama1 == None):
                    return
                if (nodo.Rama1.Cuentas == 0):
                    return
            elif (k == 2):
                if nodo.Rama2 == None:
                    return
                if nodo.Rama2.Cuentas == 0:
                    return
            elif (k == 3):
                if (nodo.Rama3 == None):
                    return
                if (nodo.Rama3.Cuentas == 0):
                    return
            elif (k == 4):
                if (nodo.Rama4 == None):
                    return
                if (nodo.Rama4.Cuentas == 0):
                    return

            self.val += 1
            if k == 0:
                self.RecursivoListado(carpeta, nodo.Rama0)
                break
            elif k == 1:
                self.RecursivoListado(carpeta, nodo.Rama1)
                break
            elif k == 2:
                self.RecursivoListado(carpeta, nodo.Rama2)
                break
            elif k == 3:
                self.RecursivoListado(carpeta, nodo.Rama3)
                break
            elif k == 4:
                self.RecursivoListado(carpeta, nodo.Rama4)
                break
            k += 1


# #########################################################################3
# bb = ArbolB()
# cc = ArbolB()
# dd = AVL()
# a = NodoProyec("Carpeta3", cc, dd)
# cc= ArbolB()
# dd = AVL()
# b = NodoProyec("Carpeta9", cc, dd)
# cc= ArbolB()
# dd = AVL()
# c = NodoProyec("Carpeta6", cc, dd)
# cc= ArbolB()
# dd = AVL()
# d = NodoProyec("Carpeta2", cc, dd)
# cc= ArbolB()
# dd = AVL()
# e = NodoProyec("Carpeta15", cc, dd)
# cc= ArbolB()
# dd = AVL()
# f = NodoProyec("Carpeta1", cc, dd)
# bb.Inserta(a)
# bb.Inserta(b)
# bb.Inserta(c)
# bb.Inserta(d)
# bb.Inserta(e)
# bb.Inserta(f)
# graph = Graficar_Arbol_B()
# graph.Graficar_File(bb.p)
#
# j = NodoAvl("putas", "25 Kb")
# k = NodoAvl("ricas", "250 Kb")
# l = NodoAvl("que", "33 Kb")
# m = NodoAvl("vivan", "2 Kb")
# n = NodoAvl("por", "7 Kb")
# o = NodoAvl("siempre", "9 Kb")
# AAVVLL = a.getAVL()
# AAVVLL.cabeza = AAVVLL.insertarActivo(j, AAVVLL.cabeza)
# AAVVLL.cabeza, val = AAVVLL.BalanceFactor(AAVVLL.cabeza)
# AAVVLL.cabeza = AAVVLL.ArbolCorre(AAVVLL.cabeza)
#
# AAVVLL.cabeza = AAVVLL.insertarActivo(k, AAVVLL.cabeza)
# AAVVLL.cabeza, val = AAVVLL.BalanceFactor(AAVVLL.cabeza)
# AAVVLL.cabeza = AAVVLL.ArbolCorre(AAVVLL.cabeza)
#
# AAVVLL.cabeza = AAVVLL.insertarActivo(l, AAVVLL.cabeza)
# AAVVLL.cabeza, val = AAVVLL.BalanceFactor(AAVVLL.cabeza)
# AAVVLL.cabeza = AAVVLL.ArbolCorre(AAVVLL.cabeza)
#
# AAVVLL.cabeza = AAVVLL.insertarActivo(m, AAVVLL.cabeza)
# AAVVLL.cabeza, val = AAVVLL.BalanceFactor(AAVVLL.cabeza)
# AAVVLL.cabeza = AAVVLL.ArbolCorre(AAVVLL.cabeza)
#
# AAVVLL.cabeza = AAVVLL.insertarActivo(n, AAVVLL.cabeza)
# AAVVLL.cabeza, val = AAVVLL.BalanceFactor(AAVVLL.cabeza)
# AAVVLL.cabeza = AAVVLL.ArbolCorre(AAVVLL.cabeza)
#
# AAVVLL.cabeza = AAVVLL.insertarActivo(o, AAVVLL.cabeza)
# AAVVLL.cabeza, val = AAVVLL.BalanceFactor(AAVVLL.cabeza)
# AAVVLL.cabeza = AAVVLL.ArbolCorre(AAVVLL.cabeza)
#
# AAVVLL.graficarAVL(AAVVLL.cabeza)