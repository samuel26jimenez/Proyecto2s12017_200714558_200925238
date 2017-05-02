import os

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
    def __init__(self, carpeta):
        self.Carpeta = carpeta

    def getCarpeta(self):
        return self.Carpeta

#--------------- Estructura  del B interno metodo -------
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
            print("---->Aqui")
        else:
            print("-----> TAMBIEN")
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
                    #os.write("Salir")
                    print("Salir")
                if self.EmpA:
                    if raiz.Cuentas < 4:
                        self.EmpA = False
                        self.MeterHoja(self.X, raiz, k)
                    else:
                        self.EmpA = True
                        self.DividirN(self.X, raiz, k)

    def DividirN(self, Clave, Raiz, k): #NodoPr, Bnodo y int k
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
                    #os.write("Sin Caso")
                    print("finalizo")
                    break
            elif Posmda == 3:
                if vale == 0:
                    s.Clave0 = Raiz.Clave3
                    s.Rama1 = Raiz.Rama4
                else:
                    break
            pos+=1

        s.Cuentas = 4 - Posmda
        Raiz.Cuentas = Posmda
        if k <= 2:
            self.MeterHoja(Clave, Raiz,k)
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

#-------------------------------->
    def MeterHoja(self, clave, raiz, k): # NodoPr Bnodo int
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
            for ii in range(j, 0) :
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
        si  = False
        j = 0
        if self.Vacio(self.p) == False: #<----Aqui tengo duda
            if clave.Carpeta.CompareTo(raiz.Clave0.Carpeta) < 0:
                si = False
                j = 0
            else:
                j = raiz.Cuentas
                for ii in [0,j]:
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

        while c<4:
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
                    elif c ==3:
                        if nodo.Clave3 == None:
                            break
                if c == 0:
                    if nodo.Clave0.getCarpeta() == identi:
                        os.write("Caso 0")
                        break
                elif c == 1:
                    if nodo.Clave1.getCarpeta()== identi:
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
            elif k == 4: # aqui voy
                if nodo.Rama4 == None:
                    return
                if nodo.Rama4.Cuentas == 0:
                    return

                self.val +=1
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
                k += 1

        self.nodo_ = None

    def Buscar_Posicion(self, clave, raiz):
        if self.nodo_ != None:
            return self.nodo_

        k = 0
        self.Esta = False
        if self.Vacio(raiz) == False: #<--------------- Aqui tengo duda
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
        if clave.CompareTo(raiz.Clave0.getCarpeta()) < 0:
            self.Esta = False
            j = 0
        else:
            j = raiz.Cuentas
            for ii in [j, 0]: #<------------- Aqui tengo duda
                if raiz.Clave3 != None and ii ==4:
                    if clave == raiz.Clave3.getCarpeta() and j > 1:
                        j -= 1
                if raiz.Clave2 != None and ii == 3:
                    if clave == raiz.Clave2.getCarpeta() and  j > 1:
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
        except(Exception ):
            self.Esta = False
            if self.Esta == False: # <--------- Aqui tengo duda
                print("Esta")
            else:
                if self.Raiz.Cuentas == 0:
                    Raiz = self.Raiz.Rama0
                self.p = Raiz

    def EliminarRegistro(self, raiz, c):
        self.pos = 0
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
                        elif pos == 3:
                            self.EliminarRegistro(raiz.Rama3, raiz.Clave2)
                        elif pos == 2:
                            self.EliminarRegistro(raiz.Rama2, raiz.Clave1)
                        elif pos == 1:
                            self.EliminarRegistro(raiz.Rama1, raiz.Clave0)
                elif (pos -1) == 3:
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
                elif (pos-1) == 2:
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
                elif (pos-1) == 1:
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
                elif (pos-1) == 0:
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

    def Sucesor(self, raiz, k): # Bnodo, int
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

        while self.Vacio(q.Rama0) != False:            # <------------- Con el desigual
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


        #if (pos - 1):
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



        #if self.Xizq.Cuentas - 1:
        if (self.Xizq.Cuentas -1) == 3:
            if (pos-1) == 3:
                self.Xizq.Clave3 = raiz.Clave3
            elif (pos-1) == 2:
                self.Xizq.Clave3 = raiz.Clave2
            elif (pos-1) == 1:
                self.Xizq.Clave3 = raiz.Clave1
            elif (pos-1) == 0:
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
            self.Xizq.Cuentas += 1
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
                break

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
                break

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
                break

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
                break
            j += 1
        self.Quitar(raiz, pos)

    def MoverDer(self, raiz, pos): # Bnodo, int
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

        if pos == 4: # por aqui voy---------------
            raiz.Rama4.Cuentas += 1
            raiz.Rama4.Rama1 = raiz.Rama4.Rama0
            raiz.Rama4.Clave0 = raiz.Clave3
            if (raiz.Rama3.Cuentas -1) == 3:
                raiz.Clave3 = raiz.Rama3.Clave3
            elif (raiz.Rama3.Cuentas -1) == 2:
                raiz.Clave3 = raiz.Rama3.Clave2
            elif (raiz.Rama3.Cuentas -1) == 1:
                raiz.Clave3 = raiz.Rama3.Clave1
            elif (raiz.Rama3.Cuentas -1) == 0:
                raiz.Clave3 = raiz.Rama3.Clave0

            if(raiz.Rama3.Cuentas -1) == 3:
                raiz.Clave3 = raiz.Rama3.Clave3
            elif(raiz.Rama3.Cuentas -1) == 2:
                raiz.Clave3 = raiz.Rama3.Clave2
            elif(raiz.Rama3.Cuentas -1) == 1:
                raiz.Clave3 = raiz.Rama3.Clave1
            elif(raiz.Rama3.Cuentas -1) == 0:
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
            raiz.Rama3.Cuentas = raiz.Rama3.Cuentas +1
            raiz.Rama3.Rama1 = raiz.Rama3.Rama0
            raiz.Rama3.Clave0 = raiz.Clave2
            if (raiz.Rama2.Cuentas -1) == 3:
                raiz.Clave2 = raiz.Rama2.Clave3
            elif (raiz.Rama2.Cuentas -1) == 2:
                raiz.Clave2 = raiz.Rama2.Clave3
            elif (raiz.Rama2.Cuentas -1) == 1:
                raiz.Clave2 = raiz.Rama2.Clave1
            elif (raiz.Rama2.Cuentas -1) == 0:
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
            raiz.Rama2.Cuentas = raiz.Rama2.Cuentas +1
            raiz.Rama2.Rama1 = raiz.Rama2.Rama0
            raiz.Rama2.Clave0 = raiz.Clave1
            if (raiz.Rama1.Cuentas -1) ==3:
                raiz.Clave1 = raiz.Rama1.Clave3
            elif (raiz.Rama1.Cuentas -1) ==2:
                raiz.Clave1 = raiz.Rama1.Clave2
            elif (raiz.Rama1.Cuentas -1) ==1:
                raiz.Clave1 = raiz.Rama1.Clave1
            elif (raiz.Rama1.Cuentas -1) ==0:
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
            if (raiz.Rama0.Cuentas -1) == 3:
                raiz.Clave0 = raiz.Rama0.Clave3
            elif (raiz.Rama0.Cuentas -1) == 2:
                raiz.Clave0 = raiz.Rama0.Clave2
            elif (raiz.Rama0.Cuentas -1) == 1:
                raiz.Clave0 = raiz.Rama0.Clave1
            elif (raiz.Rama0.Cuentas -1) == 0:
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
            raiz.Rama4.Cuentas = raiz.Rama4.Cuentas +1
            if (raiz.Rama3.Cuentas -1) == 3:
                raiz.Rama3.Clave3 = raiz.Clave3
                raiz.Rama3.Rama4 = raiz.Rama4.Rama0
            elif (raiz.Rama3.Cuentas -1) == 2:
                raiz.Rama3.Clave2 = raiz.Clave3
                raiz.Rama3.Rama2 = raiz.Rama4.Rama0
            elif (raiz.Rama3.Cuentas -1) == 1:
                raiz.Rama3.Clave1 = raiz.Clave3
                raiz.Rama3.Rama1 = raiz.Rama4.Rama0
            elif (raiz.Rama3.Cuentas -1) == 0:
                raiz.Rama3.Clave0 = raiz.Clave3
                raiz.Rama3.Rama0 = raiz.Rama4.Rama0
            raiz.Clave3 = raiz.Rama4.Clave0
            raiz.Rama4.Rama0 = raiz.Rama4.Rama1
            raiz.Rama4.Cuentas -= 1
            i =1

        elif pos == 3:
            posv = raiz.Rama3.Cuentas + 1
            raiz.Rama3.Cuentas = raiz.Rama3.Cuentas +1
            if (raiz.Rama2.Cuentas -1) == 3:
                raiz.Rama2.Clave3 = raiz.Clave2
                raiz.Rama2.Rama4 = raiz.Rama3.Rama0
            elif (raiz.Rama2.Cuentas -1) == 2:
                raiz.Rama2.Clave2 = raiz.Clave2
                raiz.Rama2.Rama2 = raiz.Rama3.Rama0
            elif (raiz.Rama2.Cuentas -1) == 1:
                raiz.Rama2.Clave1 = raiz.Clave2
                raiz.Rama2.Rama1 = raiz.Rama3.Rama0
            elif (raiz.Rama2.Cuentas -1) == 0:
                raiz.Rama2.Clave0 = raiz.Clave2
                raiz.Rama2.Rama0 = raiz.Rama3.Rama0
            raiz.Clave2 = raiz.Rama3.Clave0
            raiz.Rama3.Rama0 = raiz.Rama3.Rama1
            raiz.Rama3.Cuentas -= 1
            i =1

        elif pos == 2:
            posv = raiz.Rama2.Cuentas +1
            raiz.Rama2.Cuentas = raiz.Rama.Cuentas +1
            if (raiz.Rama1.Cuentas -1)  == 3:
                raiz.Rama1.Clave3 = raiz.Clave1
                raiz.Rama1.Rama4 = raiz.Rama2.Rama0
            elif (raiz.Rama1.Cuentas -1) == 2:
                raiz.Rama1.Clave2 = raiz.Clave1
                raiz.Rama1.Rama2 = raiz.Rama2.Rama0
            elif (raiz.Rama1.Cuentas -1) == 1:
                raiz.Rama1.Clave1 = raiz.Clave1
                raiz.Rama1.Rama1 = raiz.Rama2.Rama0
            elif (raiz.Rama1.Cuentas -1) == 0:
                raiz.Rama1.Clave0 = raiz.Clave1
                raiz.Rama1.Rama0 = raiz.Rama2.Rama0
            raiz.Clave1 = raiz.Rama2.Clave0
            raiz.Rama2.Rama0 = raiz.Rama2.Rama1
            raiz.Rama2.Cuentas -= 1
            i =1
        elif pos == 1:
            posv = raiz.Rama1.Cuentas +1
            raiz.Rama1.Cuentas = raiz.Rama1.Cuentas + 1
            if (raiz.Rama0.Cuentas -1) == 3:
                raiz.Rama0.Clave3 = raiz.Clave1
                raiz.Rama0.Rama4 = raiz.Rama1.Rama0
            elif (raiz.Rama0.Cuentas -1) == 2:
                raiz.Rama0.Clave2 = raiz.Clave1
                raiz.Rama0.Rama2 = raiz.Rama1.Rama0
            elif (raiz.Rama0.Cuentas -1) == 1:
                raiz.Rama0.Clave1 = raiz.Clave1
                raiz.Rama0.Rama1 = raiz.Rama1.Rama0
            elif (raiz.Rama0.Cuentas -1) == 0:
                raiz.Rama0.Clave0 = raiz.Clave1
                raiz.Rama0.Rama0 = raiz.Rama1.Rama0
            raiz.Clave0 = raiz.Rama1.Clave0
            raiz.Rama1.Rama0 = raiz.Rama1.Rama1
            raiz.Rama1.Cuentas -= 1
            i =1
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
            i = i +1

    def Quitar(self, raiz, pos):
        j = pos +1
        while(j != raiz.self.Cuentas +1):
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

#---------------- Grafico del Arbol B ---------------
class Graficar_Arbol_B:



    def __init__(self):
        self.lista = []
        self.desktop = None
        self.contador = 0
        self.ruta_file = ""
        self.val = 0
        self.raiz = None



    def Graficar_File(self, nodo): #Bnodo
        #self.a = ArbolB()
        self.val = 0
        global archivo
        #if self.Vacio(self.raiz) == True:
         #   return
        #else:
        archivo = open("grafica_BCarpeta.dot", "w")
        archivo.write("\ndigraph G{\r\n node [shape=record] ;\n")

        #Graficar_Arbol_B()
        self.Graficar_B(nodo)
        archivo.write("}")
        archivo.close()
        os.system("dot -Tpng grafica_BCarpeta.dot > grafica_BCarpeta.png")


    def Graficar_B(self, nodo):
        k =0
        c =0
        archivo.write( "Nodo" + str(self.val) + "[label=\"<P1>")
        while(c < 4):
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
                archivo.write("|<P" + str(c+1) + ">")
            elif c == 1:
                archivo.write("|" + nodo.Clave1.getCarpeta())
                archivo.write("|<P" + str(c+1) + ">")
            elif c == 2:
                archivo.write("|" + nodo.Clave2.getCarpeta())
                archivo.write("|<P" + str(c+1) + ">")
            elif c == 3:
                archivo.write("|" + nodo.Clave3.getCarpeta())
                archivo.write("|<P" + str(c+1) + ">")
            c += 1

        archivo.write("\"];\n")
        pasa = "Nodo" +  str(self.val)
        while(k < 5 and nodo.Cuentas >= k):
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
                    archivo.write("|<P" + str(c+1) + ">")
                elif c == 1:
                    archivo.write("|" + nodo.Clave1.getCarpeta())
                    archivo.write("|<P" + str(c+1) + ">")
                elif c == 2:
                    archivo.write("|" + nodo.Clave2.getCarpeta())
                    archivo.write("|<P" + str(c+1) + ">")
                elif c == 3:
                    archivo.write("|" + nodo.Clave3.getCarpeta())
                    archivo.write("|<P" + str(c+1) + ">")
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

    #Falta Graficar_FileII(usuario, dpto, nodo )



    def Graficar_FileII(self, carpeta, nodo): #Bnodo
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









    #global nodoB
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
            elif  c == 3:
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

        while(k < 5 and nodo.Cuentas >= k):
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
                #self.RecursivoGrafica(carpeta, nodo.Rama0)
                self.RecursivoListado(carpeta, nodo.Rama0)
                break
            elif k == 1:
                #self.RecursivoGrafica(carpeta, nodo.Rama1)
                self.RecursivoListado(carpeta, nodo.Rama1)
                break
            elif k == 2:
                #self.RecursivoGrafica(carpeta, nodo.Rama2)
                self.RecursivoListado(carpeta, nodo.Rama2)
                break
            elif k == 3:
                #self.RecursivoGrafica(carpeta, nodo.Rama3)
                self.RecursivoListado(carpeta, nodo.Rama3)
                break
            elif k == 4:
                #self.RecursivoGrafica(carpeta, nodo.Rama4)
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
                        archivo.write("Node"  + str(self.nodoB) +  "[label=\"" + nodo.Clave2.getCarpeta())
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
                c +=1

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

class Principal:

    llama = ArbolB()

    a = NodoProyec("carpeta1")
    llama.Inserta(a)

    s = NodoProyec("carpeta2")
    llama.Inserta(s)

    w = NodoProyec("carpeta3")
    llama.Inserta(w)

    r = NodoProyec("carpeta4")
    llama.Inserta(r)

    x = NodoProyec("carpeta5")
    llama.Inserta(x)

    j = NodoProyec("carpeta6")
    llama.Inserta(j)

    t = NodoProyec("carpeta7")
    llama.Inserta(t)

    u = NodoProyec("carpeta8")
    llama.Inserta(u)

    w = NodoProyec("carpeta9")
    llama.Inserta(w)




    q = NodoProyec("carpeta10")
    llama.Inserta(q)

    u = NodoProyec("carpeta11")
    llama.Inserta(u)

    g = NodoProyec("carpeta12")
    llama.Inserta(g)

    k = NodoProyec("carpeta13")
    llama.Inserta(k)

    n = NodoProyec("carpeta14")
    llama.Inserta(n)

    m = NodoProyec("carpeta15")
    llama.Inserta(m)

    d = NodoProyec("carpeta16")
    llama.Inserta(d)






    ca = NodoProyec("carpeta17")
    llama.Inserta(ca)
    #
    pu = NodoProyec("carpeta18")
    llama.Inserta(pu)
    #
    pi = NodoProyec("carpeta19")
    llama.Inserta(pi)
    #
    # cu = NodoProyec("carpeta20")
    # llama.Inserta(cu)
    #
    # pe = NodoProyec("carpeta21")
    # llama.Inserta(pe)
    #
    # xo = NodoProyec("carpeta22")
    # llama.Inserta(xo)
    #
    # fi = NodoProyec("carpeta23")
    # llama.Inserta(fi)





    ss = Graficar_Arbol_B()

    ss.Graficar_File(llama.p)

#    ss.Graficar_FileII("carpeta98", llama.p)


#puta me salio :P

