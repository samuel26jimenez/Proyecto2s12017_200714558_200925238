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
                elif k ==1:
                    if p.Rama1 == None:
                        return
                    if p.Rama1.Cuentas ==0:
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
            val= val+1
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
            k = k+1

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
                    elif c ==3:
                        if nodo.Clave3 == None:
                            break
                if c == 0:
                    if nodo.Clave0.Carpeta.Equals(identi):
                        os.write("Caso 0")
                        break
                if c ==1:
                    if nodo.Clave1.Carpeta.Equals(identi):
                        os.write("Caso 1")
                        break
                if c == 2:
                    if nodo.Clave2.Carpeta.Equals(identi):
                        os.write("Caso 2")
                        break
                if c == 3:
                    if nodo.Clave.Carpeta.Equals(identi):
                        os.write("Caso 3")
                        break
                c = c+1
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
                elif k == 4:
                    if nodo.Rama4 == None:
                        return
                    if nodo.Rama4.Cuentas == 0:
                        return

                val = val +1
                if k == 0:
                    self.RecursivoBusquedaNum(nodo.Rama0, identi)
                    break
                elif k == 1:
                    self.RecursivoBusquedaNum(nodo.Rama1, identi)
                    break
                elif k == 2:
                    self.RecursivoBusquedaNum(nodo.Rama2, identi)
                    break
                elif k ==3:
                    self.RecursivoBusquedaNum(nodo.Rama3, identi)
                    break
                elif k ==4:
                    self.RecursivoBusquedaNum(nodo.Rama4, identi)
                    break
                k = k +1

    nodo_ = None
    def Buscar_Posicion(self, clave, raiz):
        if self.nodo_ != None:
            return self.nodo_

        k = 0
        self.Esta = False
        if self.Vacio(raiz):
            k = self.BuscarNodo_Val(clave, raiz)
            if self.Esta:
                if k == 4:
                    if raiz.Clave3 != None:
                        return raiz.Clave3
                    #break
                if k == 3:
                    if raiz.Clave2 != None:
                        return raiz.Clave2
                    #break
                if k == 2:
                    if raiz.Clave1 != None:
                        return raiz.Clave1
                    #break
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
        if clave.CompareTo(raiz.Clave0.Carpeta) < 0:
            self.Esta = False
            j = 0
        else:
            j = raiz.Cuentas
            for ii in [0,j]:
                if raiz.Clave3 != None and ii ==4:
                    if clave.CompareTo(raiz.Clave3.Carpeta) < 0 and j > 1:
                        j = j-1
                if raiz.Clave2 != None and ii == 3:
                    if clave.CompareTo(raiz.Clave2.Carpeta) < 0 and  j > 1:
                        j = j-1
                if raiz.Clave1 != None and ii == 2:
                    if clave.CompareTo(raiz.Clave1.Carpeta) < 0 and j > 1:
                        j = j-1
                if raiz.Clave0 != None and ii == 1:
                    if clave.CompareTo(raiz.Clave0.Carpeta) < 0 and j > 1:
                        j = j-1
            if j == 4:
                if raiz.Clave3 != None:
                    self.Esta = (clave.Equals(raiz.Clave3.Carpeta))
            if j == 3:
                if raiz.Clave2 != None:
                    self.Esta = (clave.Equals(raiz.Clave2.Carpeta))
            if j == 2:
                if raiz.Clave1 != None:
                    self.Esta = (clave.Equals(raiz.Clave1.Carpeta))
            if j == 1:
                if raiz.Clave0 != None:
                    self.Esta = (clave.Equals(raiz.Clave0.Carpeta))
        return j

    def Eliminar(self, clave):
        if self.Vacio(self.raiz):  # Falta agg un parametro
            os.write("Elimina")
        else:
            self.Eliminara(self.p, clave)

    def Eliminara(self, Raiz, clave):
        try:
            self.EliminarRegistro(self.Raiz, clave)
        except(Exception ):
            self.Esta = False
            if not self.Esta:
                os.write("Esta")
            else:
                if self.Raiz.Cuentas == 0:
                    Raiz = self.Raiz.Rama0
                p = Raiz

    def EliminarRegistro(self, raiz, c):
        pos = 0
        #NodoProyec sucesor
        if self.Vacio(raiz):
            Esta = False
        else:
            pos = self.BuscarNodo(c, raiz)
            if self.Esta:
                if (pos-1) == 4:
                    if (self.Vacio(self.raiz.Rama4)):
                        self.Quitar(self.raiz, pos)
                    else:
                        self.Sucesor(raiz, pos)
                        if pos == 4:
                            self.EliminarRegistro(raiz.Rama4, raiz.Clave3)
                        if pos == 3:
                            self.EliminarRegistro(raiz.Rama3, raiz.Clave2)
                        if pos == 2:
                            self.EliminarRegistro(raiz.Rama2, raiz.Clave1)
                        if pos == 1:
                            self.EliminarRegistro(raiz.Rama1, raiz.Clave0)
                if (pos -1) == 3:
                    if self.Vacio(raiz.Rama3):
                        self.Quitar(self.raiz, pos)
                    else:
                        self.Sucesor(raiz, pos)
                        if pos == 4:
                            self.EliminarRegistro(raiz.Rama4, raiz.Clave3)
                        if pos == 3:
                            self.EliminarRegistro(raiz.Rama3, raiz.Clave2)
                        if pos == 2:
                            self.EliminarRegistro(raiz.Rama2, raiz.Clave1)
                        if pos == 1:
                            self.EliminarRegistro(raiz.Rama1, raiz.Clave0)
                if (pos-1) == 2:
                    if self.Vacio(raiz.Rama2):
                        self.Quitar(self.raiz, pos)
                    else:
                        self.Sucesor(raiz,pos)
                        if pos == 4:
                            self.EliminarRegistro(raiz.Rama4, raiz.Clave3)
                        if pos == 3:
                            self.EliminarRegistro(raiz.Rama3, raiz.Clave2)
                        if pos == 2:
                            self.EliminarRegistro(raiz.Rama2, raiz.Clave1)
                        if pos == 1:
                            self.EliminarRegistro(raiz.Rama1, raiz.Clave0)
                if (pos-1) == 1:
                    if self.Vacio(raiz.Rama1):
                        self.Quitar(self.raiz, pos)
                    else:
                        self.Sucesor(raiz, pos)
                        if pos == 4:
                            self.EliminarRegistro(raiz.Rama4, raiz.Clave3)
                        if pos == 3:
                            self.EliminarRegistro(raiz.Rama3, raiz.Clave2)
                        if pos == 2:
                            self.EliminarRegistro(raiz.Rama2, raiz.Clave1)
                        if pos == 1:
                            self.EliminarRegistro(raiz.Rama1, raiz.Clave0)
                if (pos-1) == 0:
                    if self.Vacio(raiz.Rama1):
                        self.Quitar(self.raiz, pos)
                    else:
                        self.Sucesor(raiz, pos)
                        if pos == 4:
                            self.EliminarRegistro(raiz.Rama4, raiz.Clave3)
                        if pos == 3:
                            self.EliminarRegistro(raiz.Rama3, raiz.Clave2)
                        if pos == 2:
                            self.EliminarRegistro(raiz.Rama2, raiz.Clave2)
                        if pos == 1:
                            self.EliminarRegistro(raiz.Rama1, raiz.Clave1)
            else:
                if pos == 4:
                    self.EliminarRegistro(raiz.Rama4, c)
                if pos == 3:
                    self.EliminarRegistro(raiz.Rama3, c)
                if pos == 2:
                    self.EliminarRegistro(raiz.Rama2, c)
                if pos == 1:
                    self.EliminarRegistro(raiz.Rama1, c)


                if pos == 4:
                    if raiz.Rama4 != None and raiz.Rama4.Cuentas < 2:
                        self.Restablecer(self.raiz, pos)
                if pos == 3:
                    if raiz.Rama3 != None and raiz.Rama3.Cuentas < 2:
                        self.Restablecer(self.raiz, pos)
                if pos == 2:
                    if raiz.Rama2 != None and raiz.Rama2.Cuentas < 2:
                        self.Restablecer(self.raiz, pos)
                if pos == 1:
                    if raiz.Rama1 != None and raiz.Rama1.Cuentas < 2:
                        self.Restablecer(self.raiz, pos)
                if pos == 0:
                    if raiz.Rama0 != None and raiz.Rama0.Cuentas < 2:
                        self.Restablecer(self.raiz, pos)

    def Sucesor(self, raiz, k): # Bnodo, int
        self.q = None
        if k == 4:
            self.q = raiz.Rama4
        if k == 3:
            self.q = raiz.Rama3
        if k == 2:
            self.q = raiz.Rama2
        if k == 1:
            self.q = raiz.Rama1
        if k == 0:
            self.q = raiz.Rama0

        while self.Vacio(self.q.Rama0) != self.Vacio(self.q.Rama0):            # <------------- Con el desigual
            q = q.Rama0

        if k == 4:
            raiz.Clave3 = q.Clave0
        if k == 3:
            raiz.Clave2 = q.Clave0
        if k == 2:
            raiz.Clave1 = q.Clave0
        if k == 1:
            raiz.Clave0 = q.Clave0


    def Combina(self, raiz, pos):
        j = 0
        if pos == 4:
            self.Xder = raiz.Rama4
        if pos == 3:
            self.Xder = raiz.Rama3
        if pos == 2:
            self.Xder = raiz.Rama2
        if pos == 1:
            self.Xder = raiz.Rama1
        if pos == 0:
            self.Xder = raiz.Rama0


        if (pos - 1):
            if (pos - 1) == 4:
                self.Xder = raiz.Rama4
            if (pos - 1) == 3:
                self.Xder = raiz.Rama3
            if (pos - 1) == 2:
                self.Xder = raiz.Rama2
            if (pos - 1) == 1:
                self.Xder = raiz.Rama1
            if (pos - 1) == 0:
                self.Xder = raiz.Rama0
        self.Xizq.Cuentas = self.Xizq.Cuentas + 1

        if self.Xizq.Cuentas - 1:
            if (self.Xizq.Cuentas -1) == 3:
                if (pos-1) == 3:
                    self.Xizq.Clave3 = raiz.Clave3
                if (pos-1) == 2:
                    self.Xizq.Clave3 = raiz.Clave2
                if (pos-1) == 1:
                    self.Xizq.Clave3 = raiz.Clave1
                if (pos-1) == 0:
                    self.Xizq.Clave3 = raiz.Clave0

            if (self.Xizq.Cuentas -1) == 2:
                if (pos - 1) == 3:
                    self.Xizq.Clave2 = raiz.Clave3
                if (pos - 1) == 2:
                    self.Xizq.Clave2 = raiz.Clave2
                if (pos - 1) == 1:
                    self.Xizq.Clave2 = raiz.Clave1
                if (pos - 1) == 0:
                    self.Xizq.Clave2 = raiz.Clave0

            if (self.Xizq.Cuentas -1) == 1:
                if (pos -1) == 3:
                    self.Xizq.Clave1 = raiz.Clave3
                if (pos -1) == 2:
                    self.Xizq.Clave1 = raiz.Clave2
                if (pos -1) == 1:
                    self.Xizq.Clave1 = raiz.Clave1
                if (pos -1) == 0:
                    self.Xizq.Clave1 = raiz.Clave0

            if (self.Xizq.Cuentas -1) == 0:
                if (pos -1) == 3:
                    self.Xizq.Clave0 = raiz.Clave3
                if (pos -1) == 2:
                    self.Xizq.Clave0 = raiz.Clave2
                if (pos -1) == 1:
                    self.Xizq.Clave0 = raiz.Clave1
                if (pos -1) == 1:
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
        while(j != self.Xder.Cuentas +1):
            self.Xizq.Cuentas = self.Xizq.Cuentas + 1
            if (self.Xizq.Cuentas -1) == 3:
                if (j-1) == 3:
                    self.Xizq.Clave3 = self.Xder.Clave3
                    self.Xizq.Rama4 = self.Xder.Rama4
                if (j-1) == 2:
                    self.Xizq.Clave3 = self.Xder.Clave2
                    self.Xizq.Rama4 = self.Xder.Rama3
                if (j-1) == 1:
                    self.Xizq.Clave3 = self.Xder.Clave1
                    self.Xizq.Rama4 = self.Xder.Rama2
                if (j-1) == 0:
                    self.Xizq.Clave3 = self.Xder.Clave0
                    self.Xizq.Rama4 = self.Xder.Rama1

            if (self.Xizq.Cuentas-1) == 2:
                if (j-1) == 3:
                    self.Xizq.Clave2 = self.Xder.Clave3
                    self.Xizq.Rama3 = self.Xder.Rama4
                if (j-1) == 2:
                    self.Xizq.Clave2 = self.Xder.Clave2
                    self.Xizq.Rama3 = self.Xder.Rama3
                if (j-1) == 1:
                    self.Xizq.Clave2 = self.Xder.Clave1
                    self.Xizq.Rama3 = self.Xder.Rama2
                if (j-1) == 0:
                    self.Xizq.Clave2 = self.Xder.Clave0
                    self.Xizq.Rama3 = self.Xder.Rama1

            if (self.Xizq.Cuentas-1) == 1:
                if (pos-1) == 3:
                    self.Xizq.Clave1 = self.Xder.Clave3
                    self.Xizq.Rama2 = self.Xder.Rama4
                if (pos-1) == 2:
                    self.Xizq.Clave1 = self.Xder.Clave2
                    self.Xizq.Rama2 = self.Xder.Rama3
                if (pos-1) == 1:
                    self.Xizq.Clave1 = self.Xder.Clave1
                    self.Xizq.Rama2 = self.Xder.Rama2
                if (pos-1) == 0:
                    self.Xizq.Clave1 = self.Xder.Clave0
                    self.Xizq.Rama2 = self.Xder.Rama1

            if (self.Xizq.Cuentas-1) == 0:
                if (pos -1) == 3:
                    self.Xizq.Clave0 = self.Xder.Clave3
                    self.Xizq.Rama1 = self.Xder.Rama4
                if (pos -1) == 2:
                    self.Xizq.Clave0 = self.Xder.Clave2
                    self.Xizq.Rama1 = self.Xder.Rama3
                if (pos -1) == 1:
                    self.Xizq.Clave0 = self.Xder.Clave1
                    self.Xizq.Rama1 = self.Xder.Rama2
                if (pos -1) == 0:
                    self.Xizq.Clave0 = self.Xder.Clave0
                    self.Xizq.Rama1 = self.Xder.Rama1
            j = j+1
        self.Quitar(raiz, pos)

    def MoverDer(self, raiz, pos): # Bnodo, int
        self.i = 0
        if pos == 4:
            self.i = raiz.Rama4.Cuentas
        if pos == 3:
            self.i = raiz.Rama3.Cuentas
        if pos == 2:
            self.i = raiz.Rama2.Cuentas
        if pos == 1:
            self.i = raiz.Rama1.Cuentas
        if pos == 0:
            self.i = raiz.Rama0.Cuentas

        while self.i != 0:
            if self.i == 3:
                if pos == 4:
                    raiz.Rama4.Clave3 = raiz.Rama4.Clave2
                    raiz.Rama4.Rama4 = raiz.Rama4.Rama3
                if pos == 3:
                    raiz.Rama3.Clave3 = raiz.Rama3.Clave2
                    raiz.Rama3.Rama4 = raiz.Rama3.Rama3
                if pos == 2:
                    raiz.Rama2.Clave3 = raiz.Rama2.Clave2
                    raiz.Rama2.Rama4 = raiz.Rama2.Rama3
                if pos == 1:
                    raiz.Rama1.Clave3 = raiz.Rama1.Clave2
                    raiz.Rama1.Rama4 = raiz.Rama1.Rama3
                if pos == 0:
                    raiz.Rama0.Clave3 = raiz.Rama0.Clave2
                    raiz.Rama0.Rama4 = raiz.Rama0.Rama3

            if self.i == 2:
                if pos == 4:
                    raiz.Rama4.Clave2 = raiz.Rama4.Clave1
                    raiz.Rama4.Rama3 = raiz.Rama4.Rama2
                if pos == 3:
                    raiz.Rama3.Clave2 = raiz.Rama3.Clave1
                    raiz.Rama3.Rama3 = raiz.Rama3.Rama2
                if pos == 2:
                    raiz.Rama2.Clave2 = raiz.Rama2.Clave1
                    raiz.Rama2.Rama3 = raiz.Rama2.Rama2
                if pos == 1:
                    raiz.Rama1.Clave2 = raiz.Rama1.Clave1
                    raiz.Rama1.Rama3 = raiz.Rama1.Rama2
                if pos == 0:
                    raiz.Rama0.Clave2 = raiz.Rama0.Clave1
                    raiz.Rama0.Rama3 = raiz.Rama0.Rama2

            if self.i == 1:
                if pos == 4:
                    raiz.Rama4.Clave1 = raiz.Rama4.Clave0
                    raiz.Rama4.Rama2 = raiz.Rama4.Rama1
                if pos == 3:
                    raiz.Rama3.Clave1 = raiz.Rama3.Clave0
                    raiz.Rama3.Rama2 = raiz.Rama3.Rama1
                if pos == 2:
                    raiz.Rama2.Clave1 = raiz.Rama2.Clave0
                    raiz.Rama2.Rama2 = raiz.Rama2.Rama1
                if pos == 1:
                    raiz.Rama1.Clave1 = raiz.Rama1.Clave0
                    raiz.Rama1.Rama2 = raiz.Rama1.Rama1
                if pos == 0:
                    raiz.Rama0.Clave1 = raiz.Rama0.Clave0
                    raiz.Rama0.Rama2 = raiz.Rama0.Rama1
        --self.i

        if pos == 4:
            raiz.Rama4.Cuentas = raiz.Rama4.Cuentas + 1
            raiz.Rama4.Rama1 = raiz.Rama4.Rama0
            raiz.Rama4.Clave0 = raiz.Clave3
            if (raiz.Rama3.Cuentas -1) == 3:
                raiz.Clave3 = raiz.Rama3.Clave3
            if (raiz.Rama3.Cuentas -1) == 2:
                raiz.clave3 = raiz.Rama3.Clave2
            if (raiz.Rama3.Cuentas -1) == 1:
                raiz.Clave3 = raiz.Rama3.Clave1
            if (raiz.Rama3.Cuentas -1) == 0:
                raiz.Clave3 = raiz.Rama3.Clave0

            if(raiz.Rama3.Cuentas -1) == 3:
                raiz.Clave3 = raiz.Rama3.Clave3
            if(raiz.Rama3.Cuentas -1) == 2:
                raiz.Clave3 = raiz.Rama3.Clave2
            if(raiz.Rama3.Cuentas -1) == 1:
                raiz.Clave3 = raiz.Rama3.Clave1
            if(raiz.Rama3.Cuentas -1) == 0:
                raiz.Clave3 = raiz.Rama3.Clave0

            if (raiz.Rama3.Cuentas) == 4:
                raiz.Rama4.Rama0 = raiz.Rama3.Rama4
            if (raiz.Rama3.Cuentas) == 3:
                raiz.Rama4.Rama0 = raiz.Rama3.Rama3
            if (raiz.Rama3.Cuentas) == 2:
                raiz.Rama4.Rama0 = raiz.Rama3.Rama2
            if (raiz.Rama3.Cuentas) == 1:
                raiz.Rama4.Rama0 = raiz.Rama3.Rama1
            if (raiz.Rama4.Cuentas) == 0:
                raiz.Rama4.Rama0 = raiz.Rama3.Rama0
            self.raiz.Rama3.Cuentas= self.raiz.Rama3.Cuentas-1

        if pos == 3:
            raiz.Rama3.Cuentas = raiz.Rama3.Cuentas +1
            raiz.Rama3.Rama1 = raiz.Rama3.Rama0
            raiz.Rama3.Clave0 = raiz.Clave2
            if (raiz.Rama2.Cuentas -1) == 3:
                raiz.Clave2 = raiz.Rama2.Clave3
            if (raiz.Rama2.Cuentas -1) == 2:
                raiz.Clave2 = raiz.Rama2.Clave3
            if (raiz.Rama2.Cuentas -1) == 1:
                raiz.Clave2 = raiz.Rama2.Clave1
            if (raiz.Rama2.Cuentas -1) == 0:
                raiz.Clave2 = raiz.Rama2.Clave0

            if (raiz.Rama2.Cuentas) == 4:
                raiz.Rama3.Rama0 = raiz.Rama2.Rama4
            if (raiz.Rama2.Cuentas) == 3:
                raiz.Rama3.Rama0 = raiz.Rama2.Rama3
            if (raiz.Rama2.Cuentas) == 2:
                raiz.Rama3.Rama0 = raiz.Rama2.Rama2
            if (raiz.Rama2.Cuentas) == 1:
                raiz.Rama3.Rama0 = raiz.Rama2.Rama1
            if (raiz.Rama2.Cuentas) == 0:
                raiz.Rama3.Rama0 = raiz.Rama2.Rama0
            self.raiz.Rama2.Cuentas = self.raiz.Rama2.Cuentas -1

        if pos == 2:
            raiz.Rama2.Cuentas = raiz.Rama2.Cuentas +1
            raiz.Rama2.Rama1 = raiz.Rama2.Rama0
            raiz.Rama2.Clave0 = raiz.Clave1
            if (raiz.Rama1.Cuentas -1) ==3:
                raiz.Clave1 = raiz.Rama1.Clave3
            if (raiz.Rama1.Cuentas -1) ==2:
                raiz.clave1 = raiz.Rama1.Clave2
            if (raiz.Rama1.Cuentas -1) ==1:
                raiz.Clave1 = raiz.Rama1.Clave1
            if (raiz.Rama1.Cuentas -1) ==0:
                raiz.Clave1 = raiz.Rama1.Clave0

            if (raiz.Rama1.Cuentas) == 4:
                raiz.Rama2.Rama0 = raiz.Rama1.Rama4
            if (raiz.Rama1.Cuentas) == 3:
                raiz.Rama2.Rama0 = raiz.Rama1.Rama3
            if (raiz.Rama1.Cuentas) == 2:
                raiz.Rama2.Rama0 = raiz.Rama1.Rama2
            if (raiz.Rama2.Cuentas) == 1:
                raiz.Rama2.Rama0 = raiz.Rama1.Rama1
            if (raiz.Rama2.Cuentas) == 0:
                raiz.Rama2.Rama0 = raiz.Rama1.Rama0
            raiz.Rama1.Cuentas = raiz.Rama1.Cuentas -1

        if pos == 1:
            raiz.Rama1.Cuentas = raiz.Rama1.Cuentas + 1
            raiz.Rama1.Rama1 = raiz.Rama1.Rama0
            raiz.Rama1.Clave0 = raiz.Clave0
            if (raiz.Rama0.Cuentas -1) == 3:
                raiz.Clave0 = raiz.Rama0.Clave3
            if (raiz.Rama0.Cuentas -1) == 2:
                raiz.Clave0 = raiz.Rama0.Clave2
            if (raiz.Rama0.Cuentas -1) == 1:
                raiz.Clave0 = raiz.Rama0.Clave1
            if (raiz.Rama0.Cuentas -1) == 0:
                raiz.Clave0 = raiz.Rama0.Clave0

            if (raiz.Rama0.Cuentas) == 4:
                raiz.Rama1.Rama0 = raiz.Rama0.Rama4
            if (raiz.Rama0.Cuentas) == 3:
                raiz.Rama1.Rama0 = raiz.Rama0.Rama3
            if (raiz.Rama0.Cuentas) == 2:
                raiz.Rama1.Rama0 = raiz.Rama0.Rama2
            if (raiz.Rama0.Cuentas) == 1:
                raiz.Rama1.Rama0 = raiz.Rama0.Rama1
            if (raiz.Rama0.Cuentas) == 0:
                raiz.Rama1.Rama0 = raiz.Rama0.Rama0
            raiz.Rama0.Cuentas = raiz.Rama0.Cuentas -1

    def MoverIzq(self, raiz, pos):
        i = 0
        posv = 0
        if pos == 4:
            posv = raiz.Rama4.Cuentas + 1
            raiz.Rama4.Cuentas = raiz.Rama4.Cuentas +1
            if (raiz.Rama3.Cuentas -1) == 3:
                raiz.Rama3.Clave3 = raiz.Clave3
                raiz.Rama3.Rama4 = raiz.Rama4.Rama0
            if (raiz.Rama3.Cuentas -1) == 2:
                raiz.Rama3.Clave2 = raiz.Clave3
                raiz.Rama3.Rama2 = raiz.Rama4.Rama0
            if (raiz.Rama3.Cuentas -1) == 1:
                raiz.Rama3.Clave1 = raiz.Clave3
                raiz.Rama3.Rama1 = raiz.Rama4.Rama0
            if (raiz.Rama3.Cuentas -1) == 0:
                raiz.Rama3.Clave0 = raiz.Clave3
                raiz.Rama3.Rama0 = raiz.Rama4.Rama0
            raiz.Clave3 = raiz.Rama4.Clave0
            raiz.Rama4.Rama0 = raiz.Rama4.Rama1
            raiz.Rama4.Cuentas = raiz.Rama4.Cuentas -1
            i =1
        if pos == 3:
            posv = raiz.Rama3.Cuentas + 1
            raiz.Rama3.Cuentas = raiz.Rama3.Cuentas +1
            if (raiz.Rama2.Cuentas -1) == 3:
                raiz.Rama2.Clave3 = raiz.Clave2
                raiz.Rama2.Rama4 = raiz.Rama3.Rama0
            if (raiz.Rama2.Cuentas -1) == 2:
                raiz.Rama2.Clave2 = raiz.Clave2
                raiz.Rama2.Rama2 = raiz.Rama3.Rama0
            if (raiz.Rama2.Cuentas -1) == 1:
                raiz.Rama2.Clave1 = raiz.Clave2
                raiz.Rama2.Rama1 = raiz.Rama3.Rama0
            if (raiz.Rama2.Cuentas -1) == 0:
                raiz.Rama2.Clave0 = raiz.Clave2
                raiz.Rama2.Rama0 = raiz.Rama3.Rama0
            raiz.Clave2 = raiz.Rama3.Clave0
            raiz.Rama3.Rama0 = raiz.Rama3.Rama1
            raiz.Rama3.Cuentas = raiz.Rama3.Cuentas -1
            i =1
        if pos == 2:
            posv = raiz.Rama2.Cuentas +1
            raiz.Rama2.Cuentas = raiz.Rama.Cuentas +1
            if (raiz.Rama1.Cuentas -1)  == 3:
                raiz.Rama1.Clave3 = raiz.Clave1
                raiz.Rama1.Rama4 = raiz.Rama2.Rama0
            if (raiz.Rama1.Cuentas -1) == 2:
                raiz.Rama1.Clave2 = raiz.Clave1
                raiz.Rama1.Rama2 = raiz.Rama2.Rama0
            if (raiz.Rama1.Cuentas -1) == 1:
                raiz.Rama1.Clave1 = raiz.Clave1
                raiz.Rama1.Rama1 = raiz.Rama2.Rama0
            if (raiz.Rama1.Cuentas -1) == 0:
                raiz.Rama1.Clave0 = raiz.Clave1
                raiz.Rama1.Rama0 = raiz.Rama2.Rama0
            raiz.Clave1 = raiz.Rama2.Clave0
            raiz.Rama2.Rama0 = raiz.Rama2.Rama1
            raiz.Rama2.Cuentas = raiz.Rama2.Cuentas -1
            i =1
        if pos == 1:
            posv = raiz.Rama1.Cuentas +1
            raiz.Rama1.Cuentas = raiz.Rama1.Cuentas + 1
            if (raiz.Rama0.Cuentas -1) == 3:
                raiz.Rama0.Clave3 = raiz.Clave1
                raiz.Rama0.Rama4 = raiz.Rama1.Rama0
            if (raiz.Rama0.Cuentas -1) == 2:
                raiz.Rama0.Clave2 = raiz.Clave1
                raiz.Rama0.Rama2 = raiz.Rama1.Rama0
            if (raiz.Rama0.Cuentas -1) == 1:
                raiz.Rama0.Clave1 = raiz.Clave1
                raiz.Rama0.Rama1 = raiz.Rama1.Rama0
            if (raiz.Rama0.Cuentas -1) == 0:
                raiz.Rama0.Clave0 = raiz.Clave1
                raiz.Rama0.Rama0 = raiz.Rama1.Rama0
            raiz.Clave0 = raiz.Rama1.Clave0
            raiz.Rama1.Rama0 = raiz.Rama1.Rama1
            raiz.Rama1.Cuentas = raiz.Rama1.Cuentas -1
            i =1
        if pos == 0:
            os.write("Salta -> jmp")

        while i != posv:
            if pos == 0:
                if i == 1:
                    raiz.Rama0.Clave0 = raiz.Rama0.Clave1
                    raiz.Rama0.Rama1 = raiz.Rama0.Rama2
                if i == 2:
                    raiz.Rama0.Clave1 = raiz.Rama0.Clave2
                    raiz.Rama0.Rama2 = raiz.Rama0.Rama3
                if i == 3:
                    raiz.Rama0.Clave2 = raiz.Rama0.Clave3
                    raiz.Rama0.Rama3 = raiz.Rama0.Rama4
            if pos == 1:
                if i == 1:
                    raiz.Rama1.Clave0 = raiz.Rama1.Clave1
                    raiz.Rama1.Rama1 = raiz.Rama1.Rama3
                if i == 2:
                    raiz.Rama1.Clave1 = raiz.Rama1.Clave2
                    raiz.Rama1.Rama2 = raiz.Rama1.Rama3
                if i == 3:
                    raiz.Rama1.Clave1 = raiz.Rama1.Clave2
                    raiz.Rama1.Rama3 = raiz.Rama1.Rama4
            if pos == 2:
                if i == 1:
                    raiz.Rama2.Clave0 = raiz.Rama2.Clave1
                    raiz.Rama2.Rama1 = raiz.Rama2.Rama2
                if i == 2:
                    raiz.Rama2.Clave1 = raiz.Rama2.Clave2
                    raiz.Rama2.Rama2 = raiz.Rama2.Rama3
                if i == 3:
                    raiz.Rama2.Clave2 = raiz.Rama2.Clave3
                    raiz.Rama2.Rama3 = raiz.Rama2.Rama4
            if pos == 3:
                if i == 1:
                    raiz.Rama3.Clave0 = raiz.Rama3.Clave1
                    raiz.Rama3.Rama1 = raiz.Rama3.Rama2
                if i == 2:
                    raiz.Rama3.Clave1 = raiz.Rama3.Clave2
                    raiz.Rama3.Rama2 = raiz.Rama3.Rama3
                if i == 3:
                    raiz.Rama3.Clave2 = raiz.Rama3.Clave3
                    raiz.Rama3.Rama3 = raiz.Rama3.Rama4
            if pos == 4:
                if i == 1:
                    raiz.Rama4.Clave0 = raiz.Rama4.Clave1
                    raiz.Rama4.Rama1 = raiz.Rama4.Rama2
                if i == 2:
                    raiz.Rama4.Clave1 = raiz.Rama4.Clave2
                    raiz.Rama4.Rama2 = raiz.Rama4.Rama3
                if i == 3:
                    raiz.Rama4.Clave2 = raiz.Rama4.Clave3
                    raiz.Rama4.Rama3 = raiz.Rama4.Rama4
            i = i +1

    def Quitar(self, raiz, pos):
        j = pos +1
        while(j != raiz.self.Cuentas +1):
            if j == 4:
                raiz.Clave2 = raiz.Clave3
                raiz.Rama3 = raiz.Rama4
            if j == 3:
                raiz.Clave1 = raiz.Clave2
                raiz.Rama2 = raiz.Rama3
            if j == 2:
                raiz.Clave0 = raiz.Clave1
                raiz.Rama1 = raiz.Rama2
            if j == 1:
                break
            if j == 0:
                break
        j = j+1
        raiz.Cuentas = raiz.Cuentas -1

    def Restablecer(self, raiz, pos):
        if pos > 0:
            if pos == 4:
                if raiz.Rama3.Cuentas > 2:
                    self.MoverDer(raiz, pos)
                else:
                    self.Combina(raiz, pos)
            if pos == 3:
                if raiz.Rama2.Cuentas > 2:
                    self.MoverDer(raiz, pos)
                else:
                    self.Combina(raiz, pos)
            if pos == 2:
                if raiz.Rama1.Cuentas > 2:
                    self.MoverDer(raiz, pos)
                else:
                    self.Combina(raiz, pos)
            if pos == 1:
                if raiz.Rama0.Cuentas > 2:
                    self.MoverDer(raiz, pos)
                else:
                    self.Combina(raiz, pos)
        elif raiz.Rama1.Cuentas > 2:
            self.MoverIzq(raiz, 1)
        else:
            self.Combina(raiz, 1)

    def Vacio(self, raiz):
        return raiz is None or raiz.a.Cuentas == 0











