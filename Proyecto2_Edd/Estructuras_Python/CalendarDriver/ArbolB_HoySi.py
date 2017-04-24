__author__ = 'Samuel'
import os
#---------------- Determino Orden 5 por cada nodo ------
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

    Cuentas = 0
    def __init__(self, clave):
        self.Clave0 = clave



#---------------- Se especifica el dato por Nodo --------
class NodoProyec:
    def __init__(self, carpeta ):
        self.Carpeta = carpeta

#--------------- Estructura  del B interno metodo -------
class ArbolB:
    a = Bnodo()
    Xder = Bnodo()
    Xizq = Bnodo()
    global x #tipo de NodoProyec
    global Xr #tipo de Bnodo

    EmpA = False
    Esta = False

    # creo un fichero
    val = 0
    buffer # tipo StrinBuilder



    def __init__(self):
        self.s = None
        self.Xder = self.Xizq = None
        X = None
        Xr = None

    def Inserta(self, clave, p):
        self.Insertaa(clave, p)

    def Insertaa(self, clave, raiz ): #NodoPr Bnodo
        self.Empujar(clave,raiz)
        if self.EmpA:
            p = Bnodo()
            p.Cuentas = 1
            p.Clave0 = self.X
            p.Rama0 = raiz
            p.Rama1 = self.Xr



    def Empujar(self, clave, raiz):
        k = 0
        Esta = False
        if self.Vacio(raiz):
            EmpA = True
            X = clave
            Xr = None
        else:
            k = self.BuscarNodo(clave, raiz)
            if Esta:
                EmpA = False
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
                    os.write("Salir")
                if self.EmpA:
                    if raiz.a.Cuentas < 4:
                        self.EmpA = False
                        self.MeterHoja(self.X,raiz,k)
                    else:
                        EmpA = True
                        self.DividirN(self.X,raiz,k)

    def DividirN(self,Clave, Raiz, k): #NodoPr, Bnodo y int k
        pos = 0
        Posmda = 0
        if k <= 2:
            Posmda = 2
        else:
            Posmda = 3
        s = Bnodo()
        pos  = Posmda +1

        vale = 0
        while pos != 5:
            vale = (pos -Posmda) -1
            if Posmda == 2:
                if vale == 1:
                    s.Clave1 = Raiz.a.Clave3
                    s.Rama2 = Raiz.a.Rama4
                elif vale == 0:
                    s.Clave0 = Raiz.a.Clave2
                    s.Rama1 = Raiz.a.Rama3
                else:
                    os.write("Sin Caso")
            elif Posmda == 3:
                if vale == 0:
                    s.Clave0 = Raiz.a.Clave3
                    s.Rama1 = Raiz.a.Rama4
            ++pos
        s.Cuentas = 4 -Posmda
        Raiz.a.Cuentas = Posmda
        if k <= 2:
            self.MeterHoja(Clave, Raiz,k)
        else:
            self.MeterHoja(Clave, s, (k-Posmda))
        if vale == 3:
            self.X = Raiz.a.Clave3
        elif vale == 2:
            self.X = Raiz.a.Clave2
        elif vale == 1:
            self.X = Raiz.a.Clave1
        elif vale == 0:
            self.X = Raiz.a.Clave0


        vale = Raiz.a.Cuentas
        if vale == 4:
            s.Rama0 = Raiz.a.Rama4
        elif vale == 3:
            s.Rama0 = Raiz.a.Rama3
        elif vale == 2:
            s.Rama0 = Raiz.a.Rama2
        elif vale == 1:
            s.Rama0 = Raiz.a.Rama1
        elif vale == 0:
            s.Rama0 = Raiz.a.Rama0
        Raiz.a.Cuentas = --Raiz.a.Cuentas
        self.Xr = s


    def MeterHoja(clave, raiz, k): # NodoPr Bnodo int
        i = raiz.a.Cuentas
        while i != k:
            if i == 3:
                raiz.Clave3 = raiz.Clave2
                raiz.Rama4 = raiz.Rama3
            elif i == 2:
                raiz.Clave1 = raiz.Clave0
                raiz.Rama3 = raiz.Rama2
            elif i == 1:
                raiz.Clave1 = raiz.Clave0
                raiz.Rama2 = raiz.Rama1
        --i
        if k == 3:
            raiz.Clave3 = clave
            raiz.Rama4 = Xr
        elif k == 2:
            raiz.Clave2 = clave
            raiz.Rama3 = Xr
        elif k == 1:
            raiz.Clave1 = clave
            raiz.Rama2 = Xr
        elif k == 0:
            raiz.Clave0 = clave
            raiz.Rama1 = Xr
        raiz.Cuentas = ++raiz.Cuentas

    def BuscarNodo(self, clave, raiz):
        j = 0
        if (clave.Carpeta.CompareTo(raiz.Clave0.Carpeta) < 0):
            self.Esta = False
            j = 0
        else:
            j = raiz.Cuentas
            for ii in [0, j] :
                if raiz.Clave3 != None and ii == 4:
                    if clave.Carpeta.CompareTo(raiz.Clave3.Carpeta) < 0 and j > 1:
                        j = j-1
                if raiz.Clave2 != None and ii == 3:
                    if clave.Carpeta.CompareTo(raiz.Clave2.Carpeta) < 0 and j > 1:
                        j = j-1
                if raiz.Clave1 != None and ii == 2:
                    if clave.Carpeta.CompareTo(raiz.Clave1.Carpeta) < 0 and j > 1:
                        j = j-1
                if raiz.Clave0 != None and ii == 1:
                    if clave.Carpeta.CompareTo(raiz.Clave0.Carpeta) < 0 and j > 1:
                        j = j-1
            if j == 4:
                raiz.Clave3 != None
            elif j == 3:
                raiz.Clave2 != None
            elif j == 2:
                raiz.Clave1 != None
            elif j == 1:
                raiz.Clave0 != None
            return j

    def Miembro(self, clave, raiz):
        si  = False
        j = 0
        if self.Vacio(self.p):
            if clave.Carpeta.CompareTo(raiz.Clave0.Carpeta) < 0:
                si = False
                j = 0
            else:
                j = raiz.Cuentas
                for ii in [0,j]:
                    if raiz.Clave3 != None and ii == 4:
                        if clave.Carpeta.CompareTo(raiz.Clave3.Carpeta) < 0 and j > 1:
                            --j
                    if raiz.Clave2 != None and ii == 3:
                        if clave.Carpeta.CompareTo(raiz.Clave2.Carpeta) < 0 and j > 1:
                            --j
                    if raiz.Clave1 != None and ii == 2:
                        if clave.Carpeta.CompareTo(raiz.Clave1.Carpeta) < 0 and j > 1:
                            --j
                if j == 4:
                    si = clave.Carpeta.CompareTo(raiz.Clave3.Carpeta) < 0
                elif j == 3:
                    si = clave.Carpeta.CompareTo(raiz.Clave2.Carpeta) < 0
                elif j == 2:
                    si = clave.Carpeta.CompareTo(raiz.Clave1.Carpeta) < 0
                elif j == 1:
                    si = clave.Carpeta.CompareTo(raiz.Clave0.Carpeta) < 0
        return si

    def BusquedaNum(self, identi):
        p = Bnodo()
        k = 0
        c = 0

        while c<4:
            if c == 0:
                if p.Clave0 == None:
                    break
            elif c ==1:
                if p.Clave1 == None:
                    break
                elif c == 2:
                    if p.Clave2 == None:
                        break
                    elif c == 3:
                        if p.Clave3 == None:
                            break
            if c == 0:
                if p.Clave0.Carpeta.Equals(identi):
                    os.write("Encontro1")
                    break
                elif p.Clave1.Carpeta.Equals(identi):
                    os.write("Encontro2")
                    break
                elif p.Clave2.Carpeta.Equals(identi):
                    os.write("Encontro3")
                    break
                elif p.Clave3.Carpeta.Equals(identi):
                    os.write("Encontro4")
                    break
            c = c+1

        while k < 5 and p.Cuentas >= k:
            if k == 0:
                if p.Rama0 == None:
                    return
                if p.Rama0.Cuentas == 0:
                    return





























    def Vacio(self, raiz):
        return raiz is None or raiz.a.Cuentas == 0








