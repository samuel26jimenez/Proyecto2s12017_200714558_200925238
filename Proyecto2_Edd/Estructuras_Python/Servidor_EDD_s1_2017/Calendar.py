import os

#NODO LISTA USUARIOS
class nodo_lista:
    def __init__(self, matriz, usuario, contrasena):
        self.usuario = usuario
        self.contrasena = contrasena
        self.siguiente = None
        self.anterior = None
        self.matrix = matriz

    def set_matrix(self, matriz):
        self.matrix = matriz

    def get_matrix(self):
        return self.matrix

    def get_user(self):
        return self.usuario

    def get_contra(self):
        return self.contrasena

#LISTA USUARIOS
class lista_usuarios:
    def __init__(self):
        self.inicio = None

    def ingresar(self, usu, passw):
        matrix = Matriz()
        nuevoNodo = nodo_lista(matrix, usu, passw)

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

    def llenarMatriz(self, usuario, dia, nombre, direccion, descripcion, hora, mes, ano):
        aux = self.inicio
        while aux != None:
            if aux.get_user() == usuario:
                aux.get_matrix().ingresarDisp(dia, nombre, direccion, descripcion, hora, mes, ano)
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


#NODO HASH
class nodo_hash:
    def __init__(self, nombre, direccion, descripcion, hora):
        self.nombre = nombre
        self.direccion = direccion
        self.descripcion = descripcion
        self.hora = hora

    def set_name(self, nombre):
        self.nombre = nombre

    def get_name(self):
        return self.nombre

    def set_dir(self, direccion):
        self.direccion = direccion

    def get_dir(self):
        return self.direccion

    def set_descrip(self, descripcion):
        self.descripcion = descripcion

    def get_descrip(self):
        return self.descripcion

    def set_hora(self, hora):
        self.hora = hora

    def get_hora(self):
        return self.hora

#TABLA HASH
class tablaHasssh:
    def __init__(self):
        self.tamano = 7
        self.cantidad = 0
        self.nodoHash = [None] * self.tamano

    def position(self, nombre):
        pos = ""
        asciiCode = 0
        for a in nombre:
            asciiCode += (ord(a))

        asciiCode = asciiCode.__pow__(2)

        return (asciiCode % self.tamano)

    def insertar(self, nombre, direccion, descripcion, hora):
        nuevoNodo = nodo_hash(nombre, direccion, descripcion, hora)
        posicion = int(self.position(nombre))
        colision = 0
        ingresa = False

        while (ingresa == False):
            # print(self.nodoHash[posicion].get_name())
            if (posicion < len(self.nodoHash)):
                if (self.nodoHash[posicion] == None):
                    self.nodoHash[posicion] = nuevoNodo
                    self.cantidad.__add__(1)
                    ingresa = True

                elif (self.nodoHash[posicion] != None):
                    posicion = self.seChoco(posicion)
                    colision += 1

            else:
                self.REhash()

    def numeroPrimo(self, dato):
        numero = 2
        siEs = True

        while (siEs == True) and (numero != dato):
            if (dato % numero == 0):
                siEs = False
            numero += 1

        return siEs

    def seChoco(self, num):
        return (num + 1)  # lineal

    def REhash(self):
        print("ENTRA REHASH")
        tamano2 = self.tamano + 1
        SiEsPrimo = self.numeroPrimo(tamano2)

        while (SiEsPrimo == False):
            tamano2 += 1
            SiEsPrimo = self.numeroPrimo(tamano2)

        otroHash = [None] * tamano2

        for a in range(0, self.tamano):
            if (self.nodoHash[a] != None):
                otroHash[a] = self.nodoHash[a]

        self.tamano = tamano2
        self.nodoHash = [None] * self.tamano
        self.nodoHash = otroHash

    def delete(self, nombre):
        tamano = 0
        for i in range(0, self.tamano):
            if ((self.nodoHash[i] != None) and (self.nodoHash[i].get_name() == nombre)):
                self.nodoHash[i] = None
                self.cantidad = self.cantidad - 1

    def imprimir(self):
        for i in range(0, self.tamano):
            if (self.nodoHash[i] != None):
                print(self.nodoHash[i].get_name() + "")
                print(str(len(self.nodoHash)))

    def modificar(self, nombre, nuevoNombre, direccion, descripcion):
        for i in range(0, self.tamano):
            if (nombre == self.nodoHash[i].get_name()):
                if direccion != "":
                    self.nodoHash[i].set_dir(direccion)
                if descripcion != "":
                    self.nodoHash[i].set_descrip(descripcion)
                if nuevoNombre != "":
                    self.nodoHash[i].set_name(nuevoNombre)
                return

    def hacerGrafica(self):
        file = open("hash.dot", "w")
        file.write("digraph G\n{\n")
        file.write("rankdir = LR;\n")
        file.write("node [shape=none];\n")
        file.write("splines=false; \n")
        file.write("a[label = <<TABLE border=\"0\" cellborder=\"1\" cellspacing=\"0\">\n")
        file.write("<tr><td colspan=\"2\" port=\"nodoCabeza\"> POSICION </td></tr>\n")

        for i in range(0, self.tamano):
            if self.nodoHash[i] != None:
                file.write("<tr><td colspan=\"2\" port=\"nodo" + str(i) + "\">" + str(i) + "</td></tr>\n")

        file.write("</TABLE>>];\n")
        file.write("a2[label=<<TABLE border=\"0\" cellborder=\"1\" cellspacing=\"0\" >\n")
        file.write("<tr>\n")
        file.write("<td colspan=\"2\" port=\"nodoCabeza\"> Nombre </td>\n")
        file.write("<td colspan=\"2\"> Direccion </td>\n")
        file.write("<td colspan=\"2\"> Descripcion </td>\n")
        file.write("<td colspan=\"2\"> Hora </td>\n")
        file.write("</tr>\n")
        file.write("</TABLE>>];\n")

        for i in range(0, self.tamano):
            if self.nodoHash[i] != None:
                file.write("b" + str(i) + "[label=<<TABLE border=\"0\" cellborder=\"1\" cellspacing=\"0\" >\n")
                file.write("<tr>\n")
                file.write("<td port=\"nodoA" + str(i) + "\">" + self.nodoHash[i].get_name() + "</td>\n")
                file.write("<td>" + self.nodoHash[i].get_dir() + "</td>\n")
                file.write("<td>" + self.nodoHash[i].get_descrip() + "</td>\n")
                file.write("<td>" + self.nodoHash[i].get_hora() + "</td>\n")
                file.write("</tr>\n")
                file.write("</TABLE>>];\n")

        file.write("a:nodoCabeza -> a2:nodoCabeza\n")

        for i in range(0, self.tamano):
            if self.nodoHash[i] != None:
                file.write("a:nodo" + str(i) + " -> b" + str(i) + ":nodoA" + str(i) + ";\n")

        file.write("}")
        file.close()
        os.system("dot -Tjpg hash.dot > hash.jpg")




#NODO MATRIZ
class NodoMatriz:

    def __init__(self, hashEventos, dia, mes, ano):
        self.hashEventos = hashEventos
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.arriba = None
        self.abajo = None
        self.derecha = None
        self.izquierda = None
        self.atras = None
        self.adelante = None

    def getNombre(self):
        return self.dia

    def setNombre(self, nCorreo):
        self.dia = nCorreo

    def getHash(self):
        return self.hashEventos

    def getLetra(self):
        return self.mes

    def getDominio(self):
        return self.ano

#MATRIZ
class Matriz:

    def __init__(self):
        self.inicioHorizontal = None
        self.inicioVertical = None

    def ingresar(self, nombre, nam, direccion, descripcion, hora, letra, dominio):
        #nombre = dia
        #nam = nombre
        #letra = mes
        #dominio = año
        hash = tablaHasssh()
        hash.insertar(nam,direccion,descripcion,hora)

        nuevoNodoMatriz = NodoMatriz(hash, nombre, letra, dominio)

        if self.vacioHorizont() == True:
            nuevoNodoHorizontal = NodoMatriz("","","",dominio)
            self.inicioHorizontal = nuevoNodoHorizontal

        if self.vacioVerti() == True:
            nuevoNodoVertical = NodoMatriz("","",letra,"")
            self.inicioVertical = nuevoNodoVertical

        ################# CREACION CABECERA HORIZONTAL #################

        tempHorizont = self.inicioHorizontal

        if self.existeHorizont(dominio) == True:
            while tempHorizont.getDominio() != dominio:
                tempHorizont = tempHorizont.derecha

        else:
            nuevoNodoHorizontal = NodoMatriz("","","",dominio)
            temp2 = None
            while tempHorizont != None and tempHorizont.getDominio() < dominio:
                temp2 = tempHorizont
                tempHorizont = tempHorizont.derecha

            if tempHorizont != None and tempHorizont.getDominio() > dominio:

                if tempHorizont == self.inicioHorizontal:
                    temp4 = self.inicioHorizontal
                    tempHorizont = nuevoNodoHorizontal
                    tempHorizont.izquierda = None
                    tempHorizont.derecha = temp4
                    temp4.izquierda = tempHorizont
                    self.inicioHorizontal = tempHorizont

                else:
                    temp4 = tempHorizont
                    tempHorizont = nuevoNodoHorizontal
                    temp2.derecha = tempHorizont
                    tempHorizont.derecha = temp4
                    temp4.izquierda = tempHorizont
                    tempHorizont.izquierda = temp2

            else:
                tempHorizont = nuevoNodoHorizontal
                temp2.derecha = tempHorizont
                tempHorizont.izquierda = temp2

        ################# APUNTADORES CON CABECERA HORIZONTAL #################

        if tempHorizont.abajo != None:
            temp5 = None
            while tempHorizont.abajo != None:
                temp5 = tempHorizont
                tempHorizont = tempHorizont.abajo
                if  tempHorizont.getLetra() == letra or tempHorizont.getLetra() > letra:
                    break

        if tempHorizont.getLetra() == letra:
            if tempHorizont.atras != None:
                while tempHorizont.atras != None:
                    tempHorizont = tempHorizont.atras
            tempHorizont.atras = nuevoNodoMatriz
            nuevoNodoMatriz.adelante = tempHorizont

        elif tempHorizont.abajo != None and tempHorizont.abajo.getLetra() > letra:
            temp6 = tempHorizont.abajo
            tempHorizont = nuevoNodoMatriz
            temp5.abajo = tempHorizont
            tempHorizont.abajo = temp6
            temp6.arriba = tempHorizont
            tempHorizont.arriba = temp5

        elif tempHorizont != None and tempHorizont.getLetra() > letra:
            temp6 = tempHorizont
            tempHorizont = nuevoNodoMatriz
            temp5.abajo = tempHorizont
            tempHorizont.abajo = temp6
            temp6.arriba = tempHorizont
            tempHorizont.arriba = temp5

        else:
            tempHorizont.abajo = nuevoNodoMatriz
            nuevoNodoMatriz.arriba = tempHorizont

        ################# CREACION DE CABECERA VERTICAL #################

        tempVerti = self.inicioVertical

        if self.existeVerti(letra) == True:
            while tempVerti.getLetra() != letra:
                tempVerti = tempVerti.abajo

        else:
            nuevoNodoVertical = NodoMatriz("","", letra, "")
            temp3 = None
            while tempVerti != None and tempVerti.getLetra() < letra:
                temp3 = tempVerti
                tempVerti = tempVerti.abajo

            if tempVerti != None and tempVerti.getLetra() > letra:
                if tempVerti == self.inicioVertical:
                    temp4 = self.inicioVertical
                    tempVerti = nuevoNodoVertical
                    tempVerti.arriba = None
                    tempVerti.abajo = temp4
                    temp4.arriba = tempVerti
                    self.inicioVertical = tempVerti

                else:
                    temp4 = tempVerti
                    tempVerti = nuevoNodoVertical
                    temp3.abajo = tempVerti
                    tempVerti.abajo = temp4
                    temp4.arriba = tempVerti
                    tempVerti.arriba = temp3

            else:
                tempVerti = nuevoNodoVertical
                temp3.abajo = tempVerti
                tempVerti.arriba = temp3

        ################# INICIA APUNTADORES CON CABECERA VERTICAL #################

        if tempVerti.derecha != None:
            temp5 = None
            while tempVerti.derecha != None:
                temp5 = tempVerti
                tempVerti = tempVerti.derecha
                if  tempVerti.getDominio() == dominio or tempVerti.getDominio() > dominio:
                    break

        if tempVerti.getDominio() == dominio and tempVerti.getNombre() != nombre:
            return

        elif tempVerti.derecha != None and tempVerti.derecha.getDominio() > dominio:
            temp6 = tempVerti
            tempVerti = nuevoNodoMatriz
            temp5.derecha = tempVerti
            tempVerti.derecha = temp6
            temp6.izquierda = tempVerti
            tempVerti.izquierda = temp5

        elif tempVerti != None and  tempVerti.getDominio() != "" and tempVerti.getDominio() > dominio:
            temp6 = tempVerti
            tempVerti = nuevoNodoMatriz
            temp5.derecha = tempVerti
            tempVerti.derecha = temp6
            temp6.izquierda = tempVerti
            tempVerti.izquierda = temp5

        else:
            tempVerti.derecha = nuevoNodoMatriz
            nuevoNodoMatriz.izquierda = tempVerti

    def vacioHorizont(self):
        if self.inicioHorizontal == None:
            return True
        else:
            return False

    def vacioVerti(self):
        if self.inicioVertical == None:
            return True
        else:
            return False

    def existeVerti(self, letra):
        temporal = self.inicioVertical
        while temporal != None:
            if temporal.getLetra() == letra:
                return True
            else:
                temporal = temporal.abajo

        return False

    def existeHorizont(self, dominio):
        temp = self.inicioHorizontal

        while temp != None:
            if temp.getDominio() == dominio:
                return True
            else:
                temp = temp.derecha

        return False

    def buscarPorLetra(self, letra):
        if self.vacioVerti() == False:
            aux = self.inicioVertical
            while aux != None and aux.getLetra() != letra:
                aux = aux.abajo

            if aux.getLetra() == letra:
                if aux.derecha != None:
                    cadena = ""
                    aux = aux.derecha
                    while aux != None:
                        cadena = cadena + aux.getNombre() + "@" + aux.getDominio() +"\n"
                        if aux.atras != None:
                            aux2 = aux.atras
                            while aux2 != None:
                                cadena = cadena + aux2.getNombre() + "@" + aux2.getDominio() + "\n"
                                aux2 = aux2.atras
                        aux = aux.derecha

                    return cadena


    def buscarPorDominio(self, dominio):
        if self.vacioHorizont() == False:
            aux = self.inicioHorizontal
            while aux != None and aux.getDominio() != dominio:
                aux = aux.derecha

            if aux.getDominio() == dominio:
                if aux.abajo != None:
                    cadena = ""
                    aux = aux.abajo
                    while aux != None:
                        cadena = cadena + aux.getNombre() + "@" + aux.getDominio() +" || Letra = "+ aux.getLetra()+"\n"
                        if aux.atras != None:
                            aux2 = aux.atras
                            while aux2 != None:
                                cadena = cadena + aux2.getNombre() + "@" + aux2.getDominio() +" || Letra = "+ aux.getLetra()+"\n"
                                aux2 = aux2.atras
                        aux = aux.abajo

                    return cadena

    def eliminar(self, nombre, letra, dominio):
        tempHorizont = self.inicioHorizontal
        tempVerti = self.inicioVertical
        temp1 = temp2 = None

        while tempHorizont != None and tempHorizont.getDominio() != dominio:
            temp1 = tempHorizont
            tempHorizont = tempHorizont.derecha

        while tempVerti != None and tempVerti.getLetra() != letra:
            temp2 = tempVerti
            tempVerti = tempVerti.abajo

        if tempHorizont != None and tempVerti != None and tempHorizont.getDominio() == dominio and tempVerti.getLetra() == letra:

            while tempHorizont != None and tempHorizont.getLetra() != letra:
                temp3 = tempHorizont
                tempHorizont = tempHorizont.abajo

            while tempVerti != None and tempVerti.getDominio() != dominio:
                temp4 = tempVerti
                tempVerti = tempVerti.derecha

            if tempHorizont != None and tempHorizont.atras != None:
                while tempHorizont.atras != None and tempHorizont.getNombre() != nombre:
                    temp3 = tempHorizont
                    tempHorizont = tempHorizont.atras

            if tempVerti != None and tempVerti.atras != None:
                while tempVerti.atras != None and tempVerti.getNombre() != nombre:
                    temp4 = tempVerti
                    tempVerti = tempVerti.atras

            ################ EMPIEZA ELIMINACION DE NODOS EN CABECERA HORIZONTAL
            if tempHorizont != None and tempHorizont.getNombre() == nombre:
                if temp3 != None and temp3.getNombre() == "":
                    if tempHorizont.atras != None:
                        temp3.abajo = tempHorizont.atras
                        tempHorizont.atras.arriba = temp3
                        if tempHorizont.abajo != None:
                            tempHorizont.atras.abajo = tempHorizont.abajo
                            tempHorizont.abajo.arriba = tempHorizont.atras
                    elif tempHorizont.abajo != None:
                        temp3.abajo = tempHorizont.abajo
                        tempHorizont.abajo.arriba = temp3
                    else:
                        temp3.abajo = None
                        if temp1 != None and temp3.derecha != None:
                            temp1.derecha = temp3.derecha
                            temp3.derecha.izquierda = temp1
                            temp3 = None
                        elif temp1 != None:
                            temp1.derecha = None
                            temp3 = None
                        elif temp3.derecha != None:
                            temp3.derecha.izquierda = None
                            self.inicioHorizontal = temp3.derecha
                            temp3 = None
                        else:
                            temp3 = self.inicioHorizontal = None

                elif temp3 != None:
                    if tempHorizont.adelante != None:
                        if tempHorizont.atras != None:
                            temp3.atras = tempHorizont.atras
                            tempHorizont.atras.adelante = temp3
                        else:
                            temp3.atras = None
                    elif tempHorizont.atras != None:
                        temp3.abajo = tempHorizont.atras
                        if tempHorizont.abajo != None:
                            tempHorizont.atras.abajo = tempHorizont.abajo
                            tempHorizont.abajo.arriba = tempHorizont.atras
                        tempHorizont.atras.arriba = temp3
                    elif tempHorizont.abajo != None:
                        temp3.abajo = tempHorizont.abajo
                        tempHorizont.abajo.arriba = temp3
                    else:
                        temp3.abajo = None

            ################ EMPIEZA ELIMINACION DE NODOS EN CABECERA VERTICAL
            if tempVerti != None and tempVerti.getNombre() == nombre:
                if temp4 != None and temp4.getNombre() == "":
                    if tempVerti.atras != None:
                        temp4.derecha = tempVerti.atras
                        tempVerti.atras.izquierda = temp4
                        if tempVerti.derecha != None:
                            tempVerti.atras.derecha = tempVerti.derecha
                            tempVerti.derecha.izquierda = tempVerti.atras
                    elif tempVerti.derecha != None:
                        temp4.derecha = tempVerti.derecha
                        tempVerti.derecha.izquierda = temp4
                    else:
                        temp4.derecha = None
                        if temp2 != None and temp4.abajo != None:
                            temp2.abajo = temp4.abajo
                            temp4.abajo.arriba = temp2
                            temp4 = None
                        elif temp2 != None:
                            temp2.abajo = None
                            temp4 = None
                        elif temp4.abajo != None:
                            temp4.abajo.arriba = None
                            self.inicioVertical = temp4.abajo
                            temp4 = None
                        else:
                            temp4 = self.inicioVertical = None
                elif temp4 != None:
                    if tempVerti.adelante != None:
                        if tempVerti.atras != None:
                            temp4.atras = tempVerti.atras
                            tempVerti.atras.adelante = temp4
                        else:
                            temp4.atras = None
                    elif tempVerti.atras != None:
                        temp4.derecha = tempVerti.atras
                        if tempVerti.derecha != None:
                            tempVerti.atras.derecha = tempVerti.derecha
                            tempVerti.derecha.izquierda = tempVerti.atras
                        tempVerti.atras.izquierda = temp4
                    elif tempVerti.derecha != None:
                        temp4.derecha = tempVerti.derecha
                        tempVerti.derecha.izquierda = temp4
                    else:
                        temp4.derecha = None

    def hacerGrafica(self):
        if self.vacioHorizont() == True or self.vacioVerti() == True:
            return
        else:
            file = open("matriz.dot", "w")
            file.write("digraph G\n{\n")
            tempHorizont = self.inicioHorizontal
            tempVerti = self.inicioVertical
            file.write("\"INICIO\"[label = \"Inicio\", style = filled, fillcolor=\"#0D5A73\", fontcolor=\"#A2E7FF\", shape=box]\n")
            file.write("\"INICIO\" -> \"n" + str(tempVerti.getLetra()) + "\"\n")
            while tempVerti != None:
                file.write("\"n" + str(tempVerti.getLetra()) + "\"[label = \"" + str(tempVerti.getLetra()) + "\", style = filled, fillcolor=\"#E1E16E\", fontcolor=\"#040404\", shape=box]\n")
                if (tempVerti.abajo != None):
                    file.write("\"n" + str(tempVerti.getLetra()) + "\" -> \"n" + str(tempVerti.abajo.getLetra()) + "\"[rankdir=UD];\n")
                    file.write("\"n" + str(tempVerti.abajo.getLetra()) + "\" -> \"n" + str(tempVerti.getLetra()) + "\"\n")

                if (tempVerti.derecha != None):
                    file.write("\"n" + str(tempVerti.derecha.getLetra()) + "," + str(
                        tempVerti.derecha.getNombre()) + "," + str(
                        tempVerti.derecha.getDominio()) + "\"[label = \"" + str(
                        tempVerti.derecha.getNombre()) + "\", style = filled, fillcolor=\"#5C5C5A\", fontcolor=\"#FCFC29\", shape=circle]\n")
                    file.write("\"n" + str(tempVerti.getLetra()) + "\" -> \"n" + str(tempVerti.derecha.getLetra()) + ","+ str(tempVerti.derecha.getNombre()) +","+ str(tempVerti.derecha.getDominio()) + "\"[constraint=false];\n")
                    file.write("\"n" + str(tempVerti.derecha.getLetra()) + ","+ str(tempVerti.derecha.getNombre()) +","+ str(tempVerti.derecha.getDominio()) + "\" -> \"n" + str(tempVerti.getLetra()) + "\"[constraint=false];\n")
                    file.write("{rank=same; \"n" + str(tempVerti.getLetra()) + "\"  \"n" + str(tempVerti.derecha.getLetra()) + ","+ str(tempVerti.derecha.getNombre()) +","+ str(tempVerti.derecha.getDominio()) + "\"}\n")
                    file.write("{rank=same; \"n" + str(tempVerti.derecha.getLetra()) + ","+ str(tempVerti.derecha.getNombre()) +","+ str(tempVerti.derecha.getDominio()) + "\"  \"n" + str(tempVerti.getLetra()) + "\"}\n")
                    AUXtempVerti = tempVerti.derecha

                while (AUXtempVerti.derecha != None):
                    file.write("\"n" + str(AUXtempVerti.derecha.getLetra()) + ","+ str(AUXtempVerti.derecha.getNombre()) +","+ str(AUXtempVerti.derecha.getDominio()) +"\"[label = \""
                               + str(AUXtempVerti.derecha.getNombre()) + "\", style = filled, fillcolor=\"#5C5C5A\", fontcolor=\"#FCFC29\", shape=circle]\n")
                    file.write("\"n" + str(AUXtempVerti.getLetra()) + ","+ str(AUXtempVerti.getNombre()) +","+ str(AUXtempVerti.getDominio()) + "\" -> \"n"
                               + str(AUXtempVerti.derecha.getLetra()) + ","+ str(AUXtempVerti.derecha.getNombre()) +","+ str(AUXtempVerti.derecha.getDominio()) + "\"[constraint=false];\n")
                    file.write("\"n" + str(AUXtempVerti.derecha.getLetra()) + ","+ str(AUXtempVerti.derecha.getNombre()) +","+ str(AUXtempVerti.derecha.getDominio())
                               + "\" -> \"n" + str(AUXtempVerti.getLetra()) + ","+ str(AUXtempVerti.getNombre()) +","+ str(AUXtempVerti.getDominio()) + "\"[constraint=false];\n")
                    file.write("{rank=same; \"n" + str(AUXtempVerti.getLetra()) + ","+ str(AUXtempVerti.getNombre()) +","+ str(AUXtempVerti.getDominio()) + "\" \"n" + str(AUXtempVerti.derecha.getLetra())
                               + ","+ str(AUXtempVerti.derecha.getNombre()) +","+ str(AUXtempVerti.derecha.getDominio()) + "\"}\n");
                    file.write("{rank=same; \"n" + str(AUXtempVerti.derecha.getLetra()) + ","+ str(AUXtempVerti.derecha.getNombre()) +","+ str(AUXtempVerti.derecha.getDominio()) + "\" \"n"
                               + str(AUXtempVerti.getLetra()) + ","+ str(AUXtempVerti.getNombre()) +","+ str(AUXtempVerti.getDominio()) + "\"}\n");

                    AUXtempVerti = AUXtempVerti.derecha

                tempVerti = tempVerti.abajo


            file.write("\"INICIO\" -> \"n" + str(tempHorizont.getDominio()) + "\"\n")
            file.write("{rank=same; \"INICIO\"  \"n" + str(tempHorizont.getDominio()) + "\"}\n")
            while tempHorizont != None:
                file.write("\"n" + str(tempHorizont.getDominio()) + "\"[label = \"" + str(tempHorizont.getDominio()) + "\", style = filled, fillcolor=\"#E1E16E\", fontcolor=\"#040404\", shape=box]\n")
                if (tempHorizont.derecha != None):
                    file.write("\"n" + str(tempHorizont.getDominio()) + "\" -> \"n" + str(tempHorizont.derecha.getDominio()) + "\"\n")
                    file.write("\"n" + str(tempHorizont.derecha.getDominio()) + "\" -> \"n" + str(tempHorizont.getDominio()) + "\"\n")
                    file.write("{rank=same; \"n" + str(tempHorizont.getDominio()) + "\"  \"n" + str(tempHorizont.derecha.getDominio()) + "\"}\n")
                    file.write("{rank=same; \"n" + str(tempHorizont.derecha.getDominio()) + "\"  \"n" + str(tempHorizont.getDominio()) + "\"}\n")

                if (tempHorizont.abajo != None):
                    file.write("\"n" + str(tempHorizont.getDominio()) + "\" -> \"n" + str(tempHorizont.abajo.getLetra()) + ","+ str(tempHorizont.abajo.getNombre()) +","+ str(tempHorizont.abajo.getDominio()) + "\"[rankdir=UD];\n")
                    file.write("\"n" + str(tempHorizont.abajo.getLetra()) + ","+ str(tempHorizont.abajo.getNombre()) +","+ str(tempHorizont.abajo.getDominio()) + "\" -> \"n" + str(tempHorizont.getDominio()) + "\"\n")
                    AUXtempHorizont = tempHorizont.abajo

                while (AUXtempHorizont.abajo != None):
                    file.write("\"n" + str(AUXtempHorizont.getLetra()) + ","+ str(AUXtempHorizont.getNombre()) +","+ str(AUXtempHorizont.getDominio()) + "\" -> \"n"
                               + str(AUXtempHorizont.abajo.getLetra()) + ","+ str(AUXtempHorizont.abajo.getNombre()) +","+ str(AUXtempHorizont.abajo.getDominio()) + "\"[rankdir=UD];\n")
                    file.write("\"n" + str(AUXtempHorizont.abajo.getLetra()) + ","+ str(AUXtempHorizont.abajo.getNombre()) +","+ str(AUXtempHorizont.abajo.getDominio())
                               + "\" -> \"n" + str(AUXtempHorizont.getLetra()) + ","+ str(AUXtempHorizont.getNombre()) +","+ str(AUXtempHorizont.getDominio()) + "\"\n")

                    AUXtempHorizont = AUXtempHorizont.abajo

                tempHorizont = tempHorizont.derecha

            file.write("subgraph cluster_0 {\n")
            file.write("style=filled;\n")
            file.write("color=grey;\n")
            file.write("node [style=filled,color=white];\n")

            tempVerti = self.inicioVertical
            while tempVerti != None:

                if (tempVerti.derecha != None):
                    AUXtempVerti = tempVerti.derecha

                while (AUXtempVerti.derecha != None):
                    if AUXtempVerti.atras != None:
                        file.write("\"extra" + str(AUXtempVerti.getDominio()) + "\"[label = \"" + str(AUXtempVerti.derecha.getDominio()) + "\", style = filled, shape=box]\n")

                    if AUXtempVerti.atras != None:
                        file.write("\"extra" + str(AUXtempVerti.getDominio()) + "\"[label = \"" + str(
                            AUXtempVerti.getDominio()) + "\", style = filled, shape=box]\n")
                        file.write("\"n" + str(AUXtempVerti.atras.getLetra()) + "," + str(
                            AUXtempVerti.atras.getNombre()) + "," + str(
                            AUXtempVerti.atras.getDominio()) + "\"[label = \"" + str(
                            AUXtempVerti.atras.getNombre())  + "\", style = filled, shape=circle]\n")
                        file.write("\"extra" + str(AUXtempVerti.getDominio()) + "\" -> \"n" + str(AUXtempVerti.atras.getLetra()) + "," + str(
                            AUXtempVerti.atras.getNombre()) + "," + str(
                            AUXtempVerti.atras.getDominio()) +"\"\n")
                        file.write("\"n" + str(AUXtempVerti.atras.getLetra()) + "," + str(
                            AUXtempVerti.atras.getNombre()) + "," + str(
                            AUXtempVerti.atras.getDominio()) + "\" -> \"extra" + str(AUXtempVerti.getDominio()) +"\"\n")
                        AUX2Verti = AUXtempVerti.atras

                        while (AUX2Verti.atras != None):
                            file.write("\"n" + str(AUX2Verti.atras.getLetra()) + ","+ str(AUX2Verti.atras.getNombre()) +","+ str(AUX2Verti.atras.getDominio()) +"\"[label = \"" + str(AUX2Verti.atras.getNombre()) + "\", style = filled, shape=circle]\n")
                            file.write("\"n" + str(AUX2Verti.getLetra()) + ","+ str(AUX2Verti.getNombre()) +","+ str(AUX2Verti.getDominio()) + "\" -> \"n"
                                       + str(AUX2Verti.atras.getLetra()) + ","+ str(AUX2Verti.atras.getNombre()) +","+ str(AUX2Verti.atras.getDominio()) + "\"\n")
                            file.write("\"n" + str(AUX2Verti.atras.getLetra()) + ","+ str(AUX2Verti.atras.getNombre()) +","+ str(AUX2Verti.atras.getDominio())
                                       + "\" -> \"n" + str(AUX2Verti.getLetra()) + ","+ str(AUX2Verti.getNombre()) +","+ str(AUX2Verti.getDominio()) + "\"\n")

                            AUX2Verti = AUX2Verti.atras

                    AUXtempVerti = AUXtempVerti.derecha


                if AUXtempVerti.atras != None:
                    file.write("\"extra" + str(AUXtempVerti.getDominio()) + "\"[label = \"" + str(
                        AUXtempVerti.getDominio()) + "\", style = filled, shape=box]\n")
                    file.write("\"n" + str(AUXtempVerti.atras.getLetra()) + "," + str(
                            AUXtempVerti.atras.getNombre()) + "," + str(
                            AUXtempVerti.atras.getDominio()) + "\"[label = \"" + str(
                            AUXtempVerti.atras.getNombre())  + "\", style = filled, shape=circle]\n")
                    file.write("\"extra" + str(AUXtempVerti.getDominio()) + "\" -> \"n" + str(AUXtempVerti.atras.getLetra()) + "," + str(
                            AUXtempVerti.atras.getNombre()) + "," + str(
                            AUXtempVerti.atras.getDominio()) + "\"\n")
                    file.write("\"n" + str(AUXtempVerti.atras.getLetra()) + "," + str(
                            AUXtempVerti.atras.getNombre()) + "," + str(
                            AUXtempVerti.atras.getDominio()) + "\" -> \"extra" + str(AUXtempVerti.getDominio()) +"\"\n")
                    AUX2Verti = AUXtempVerti.atras

                    while (AUX2Verti.atras != None):
                        file.write("\"n" + str(AUX2Verti.atras.getLetra()) + ","+ str(AUX2Verti.atras.getNombre()) +","+ str(AUX2Verti.atras.getDominio()) +"\"[label = \"" + str(AUX2Verti.atras.getNombre()) + "\", style = filled, shape=circle]\n")
                        file.write("\"n" + str(AUX2Verti.getLetra()) + ","+ str(AUX2Verti.getNombre()) +","+ str(AUX2Verti.getDominio()) + "\" -> \"n"
                            + str(AUX2Verti.atras.getLetra()) + ","+ str(AUX2Verti.atras.getNombre()) +","+ str(AUX2Verti.atras.getDominio()) + "\"\n")
                        file.write("\"n" + str(AUX2Verti.atras.getLetra()) + ","+ str(AUX2Verti.atras.getNombre()) +","+ str(AUX2Verti.atras.getDominio())
                            + "\" -> \"n" + str(AUX2Verti.getLetra()) + ","+ str(AUX2Verti.getNombre()) +","+ str(AUX2Verti.getDominio()) + "\"\n")

                        AUX2Verti = AUX2Verti.atras

                tempVerti = tempVerti.abajo

            file.write("label = \"PROFUNDIDAD\";\n")
            file.write("}\n")
            file.write("}")
            file.close()
            os.system("dot -Tjpg matriz.dot > matriz.jpg")

    def modificarEvento(self, dia, nombre, nuevoNombre, direccion, descripcion, mes, ano):
        if self.vacioHorizont() == False:
            aux = self.inicioHorizontal
            while aux.derecha != None and aux.getDominio() != ano:
                aux = aux.derecha

            if aux.getDominio() == ano:
                if aux.abajo != None:
                    aux = aux.abajo
                    while aux.abajo != None and aux.getLetra() != mes:
                        aux = aux.abajo

                    if aux.getLetra() == mes:
                        if aux.getNombre() != dia:
                            while aux.atras != None and aux.getNombre() != dia:
                                aux = aux.atras

                        if aux.getNombre() == dia:
                            aux.getHash().modificar(nombre, nuevoNombre, direccion, descripcion)


    def eliminarEvento(self, dia, nombre, mes, ano):
        if self.vacioHorizont() == False:
            aux = self.inicioHorizontal
            while aux.derecha != None and aux.getDominio() != ano:
                aux = aux.derecha

            if aux.getDominio() == ano:
                if aux.abajo != None:
                    aux = aux.abajo
                    while aux.abajo != None and aux.getLetra() != mes:
                        aux = aux.abajo

                    if aux.getLetra() == mes:
                        if aux.getNombre() != dia:
                            while aux.atras != None and aux.getNombre() != dia:
                                aux = aux.atras

                        if aux.getNombre() == dia:
                            aux.getHash().delete(nombre)


    def graficaEvento(self, dia, mes, ano):
        if self.vacioHorizont() == False:
            aux = self.inicioHorizontal
            while aux.derecha != None and aux.getDominio() != ano:
                aux = aux.derecha

            if aux.getDominio() == ano:
                if aux.abajo != None:
                    aux = aux.abajo
                    while aux.abajo != None and aux.getLetra() != mes:
                        aux = aux.abajo

                    if aux.getLetra() == mes:
                        if aux.getNombre() != dia:
                            while aux.atras != None and aux.getNombre() != dia:
                                aux = aux.atras

                        if aux.getNombre() == dia:
                            aux.getHash().hacerGrafica()

    def verificaExistencia(self, dia, nam, direccion, descripcion, hora, mes, ano):
        #nam = nombre
        if self.vacioHorizont() == False:
            aux = self.inicioHorizontal
            while aux.derecha != None and aux.getDominio() != ano:
                aux = aux.derecha

            if aux.getDominio() == ano:
                if aux.abajo != None:
                    aux = aux.abajo
                    while aux.abajo != None and aux.getLetra() != mes:
                        aux = aux.abajo

                    if aux.getLetra() == mes:
                        if aux.getNombre() != dia:
                            while aux.atras != None and aux.getNombre() != dia:
                                aux = aux.atras

                        if aux.getNombre() == dia:
                            aux.getHash().insertar(nam,direccion,descripcion,hora)
                            return True

                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def ingresarDisp(self, dia, nam, direccion, descripcioin, hora, mes, ano):
        if self.verificaExistencia(dia, nam, direccion, descripcioin, hora, mes, ano) == False:
            self.ingresar(dia, nam, direccion, descripcioin, hora, mes, ano)



#--------------------------------------------------------------------------------------------------------------------
#-------------------------------------------- PRUEBAS ---------------------------------------------------------------

# hashi = Matriz()
# hashi.ingresarDisp("2", "rafa", "usac", "la mera verga", "son las que te importa", "enero", "2017")
# hashi.ingresarDisp("20", "pedro", "usac", "la mera verga", "son las que te importa", "febrero", "2017")
# hashi.ingresarDisp("8", "felipe", "usac", "la mera verga", "son las que te importa", "enero", "2017")
# hashi.ingresarDisp("6", "kam", "usac", "la mera verga", "son las que te importa", "diciembre", "2015")
# hashi.ingresarDisp("27", "tom", "usac", "la mera verga", "son las que te importa", "junio", "2006")
# hashi.ingresarDisp("4", "kamasutra", "usac", "la mera verga", "son las que te importa", "septiembre", "2011")
# hashi.ingresarDisp("22", "margarita", "usac", "la mera verga", "son las que te importa", "febrero", "2014")
# hashi.ingresarDisp("22", "peter", "usac", "la mera verga", "son las que te importa", "febrero", "2014")
# hashi.ingresarDisp("22", "mamasita", "usac", "la mera verga", "son las que te importa", "febrero", "2014")
# hashi.ingresarDisp("5", "PUTOS", "usac", "la mera verga", "son las que te importa", "abril", "2015")
# hashi.ingresarDisp("10", "que vivan las putas", "usac", "la mera verga", "son las que te importa", "enero", "2007")
# hashi.graficaEvento("22", "febrero", "2014")