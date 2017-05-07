import os
import CalendarDriver
from CalendarDriver import *
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

    def getHash(self):
        return self.hashEventos

    def getMes(self):
        return self.mes

    def getAno(self):
        return self.ano

    def getDia(self):
        return self.dia


#MATRIZ
class Matriz:

    def __init__(self):
        self.inicioHorizontal = None
        self.inicioVertical = None

    def ingresar(self, day, nombre, direccion, descripcion, hora, month, year):
        hash = CalendarDriver.tablaHasssh()
        hash.insertar(nombre,direccion,descripcion,hora)

        nuevoNodoMatriz = NodoMatriz(hash, day, month, year)

        if self.vacioHorizont() == True:
            nuevoNodoHorizontal = NodoMatriz("","","","","","",year)
            self.inicioHorizontal = nuevoNodoHorizontal

        if self.vacioVerti() == True:
            nuevoNodoVertical = NodoMatriz("","","","","",month,"")
            self.inicioVertical = nuevoNodoVertical

        ################# CREACION CABECERA HORIZONTAL #################

        tempHorizont = self.inicioHorizontal

        if self.existeHorizont(year) == True:
            while tempHorizont.getAno() != year:
                tempHorizont = tempHorizont.derecha

        else:
            nuevoNodoHorizontal = NodoMatriz("","","","","","",year)
            temp2 = None
            while tempHorizont != None and tempHorizont.getAno() < year:
                temp2 = tempHorizont
                tempHorizont = tempHorizont.derecha

            if tempHorizont != None and tempHorizont.getAno() > year:

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
                if  tempHorizont.getMes() == month or tempHorizont.getMes() > month:
                    break

        if tempHorizont.getMes() == month:
            if tempHorizont.atras != None:
                while tempHorizont.atras != None:
                    tempHorizont = tempHorizont.atras
            tempHorizont.atras = nuevoNodoMatriz
            nuevoNodoMatriz.adelante = tempHorizont

        elif tempHorizont.abajo != None and tempHorizont.abajo.getMes() > month:
            temp6 = tempHorizont.abajo
            tempHorizont = nuevoNodoMatriz
            temp5.abajo = tempHorizont
            tempHorizont.abajo = temp6
            temp6.arriba = tempHorizont
            tempHorizont.arriba = temp5

        elif tempHorizont != None and tempHorizont.getMes() > month:
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

        if self.existeVerti(month) == True:
            while tempVerti.getMes() != month:
                tempVerti = tempVerti.abajo

        else:
            nuevoNodoVertical = NodoMatriz("","","","","",month,"")
            temp3 = None
            while tempVerti != None and tempVerti.getMes() < month:
                temp3 = tempVerti
                tempVerti = tempVerti.abajo

            if tempVerti != None and tempVerti.getMes() > month:
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
                if  tempVerti.getAno() == year or tempVerti.getAno() > year:
                    break

        if tempVerti.getAno() == year and tempVerti.getDia() != day:
            return

        elif tempVerti.derecha != None and tempVerti.derecha.getAno() > year:
            temp6 = tempVerti
            tempVerti = nuevoNodoMatriz
            temp5.derecha = tempVerti
            tempVerti.derecha = temp6
            temp6.izquierda = tempVerti
            tempVerti.izquierda = temp5

        elif tempVerti != None and  tempVerti.getAno() != "" and tempVerti.getAno() > year:
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
            if temporal.getMes() == letra:
                return True
            else:
                temporal = temporal.abajo

        return False

    def existeHorizont(self, dominio):
        temp = self.inicioHorizontal

        while temp != None:
            if temp.getAno() == dominio:
                return True
            else:
                temp = temp.derecha

        return False

    def buscarPorLetra(self, letra):
        if self.vacioVerti() == False:
            aux = self.inicioVertical
            while aux != None and aux.getMes() != letra:
                aux = aux.abajo

            if aux.getMes() == letra:
                if aux.derecha != None:
                    cadena = ""
                    aux = aux.derecha
                    while aux != None:
                        cadena = cadena + aux.getAno() +"\n"
                        if aux.atras != None:
                            aux2 = aux.atras
                            while aux2 != None:
                                cadena = cadena + aux2.getAno() + "\n"
                                aux2 = aux2.atras
                        aux = aux.derecha

                    return cadena


    def modificarEvento(self, dia, nombre, nuevoNombre, direccion, descripcion, mes, ano):
        if self.vacioHorizont() == False:
            aux = self.inicioHorizontal
            while aux.derecha != None and aux.getAno() != ano:
                aux = aux.derecha

            if aux.getAno() == ano:
                if aux.abajo != None:
                    aux = aux.abajo
                    while aux.abajo != None and aux.getMes != mes:
                        aux = aux.abajo

                    if aux.getMes() == mes:
                        if aux.getDia() != dia:
                            while aux.atras != None and aux.getDia() != dia:
                                aux = aux.atras

                        if aux.getDia() == dia:
                            aux.getHash().modificar(nombre, nuevoNombre, direccion, descripcion)


    def eliminarEvento(self, dia, nombre, mes, ano):
        if self.vacioHorizont() == False:
            aux = self.inicioHorizontal
            while aux.derecha != None and aux.getAno() != ano:
                aux = aux.derecha

            if aux.getAno() == ano:
                if aux.abajo != None:
                    aux = aux.abajo
                    while aux.abajo != None and aux.getMes != mes:
                        aux = aux.abajo

                    if aux.getMes() == mes:
                        if aux.getDia() != dia:
                            while aux.atras != None and aux.getDia() != dia:
                                aux = aux.atras

                        if aux.getDia() == dia:
                            aux.getHash().delete(nombre)


    def buscarPorDominio(self, dominio):
        if self.vacioHorizont() == False:
            aux = self.inicioHorizontal
            while aux != None and aux.getAno() != dominio:
                aux = aux.derecha

            if aux.getAno() == dominio:
                if aux.abajo != None:
                    cadena = ""
                    aux = aux.abajo
                    while aux != None:
                        cadena = cadena + aux.getAno() +" || Mes = "+ aux.getMes()+"\n"
                        if aux.atras != None:
                            aux2 = aux.atras
                            while aux2 != None:
                                cadena = cadena + aux2.getAno() +" || Mes = "+ aux.getMes()+"\n"
                                aux2 = aux2.atras
                        aux = aux.abajo

                    return cadena

    def eliminar(self, nombre, letra, dominio):
        tempHorizont = self.inicioHorizontal
        tempVerti = self.inicioVertical
        temp1 = temp2 = None

        while tempHorizont != None and tempHorizont.getAno() != dominio:
            temp1 = tempHorizont
            tempHorizont = tempHorizont.derecha

        while tempVerti != None and tempVerti.getMes() != letra:
            temp2 = tempVerti
            tempVerti = tempVerti.abajo

        if tempHorizont != None and tempVerti != None and tempHorizont.getAno() == dominio and tempVerti.getMes() == letra:

            while tempHorizont != None and tempHorizont.getMes() != letra:
                temp3 = tempHorizont
                tempHorizont = tempHorizont.abajo

            while tempVerti != None and tempVerti.getAno() != dominio:
                temp4 = tempVerti
                tempVerti = tempVerti.derecha

            if tempHorizont != None and tempHorizont.atras != None:
                while tempHorizont.atras != None and tempHorizont.getDia() != nombre:
                    temp3 = tempHorizont
                    tempHorizont = tempHorizont.atras

            if tempVerti != None and tempVerti.atras != None:
                while tempVerti.atras != None and tempVerti.getDia() != nombre:
                    temp4 = tempVerti
                    tempVerti = tempVerti.atras

            ################ EMPIEZA ELIMINACION DE NODOS EN CABECERA HORIZONTAL
            if tempHorizont != None and tempHorizont.getDia() == nombre:
                if temp3 != None and temp3.getDia() == "":
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
            if tempVerti != None and tempVerti.getDia() == nombre:
                if temp4 != None and temp4.getDia() == "":
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
            file.write("\"INICIO\" -> \"n" + str(tempVerti.getMes()) + "\"\n")
            while tempVerti != None:
                file.write("\"n" + str(tempVerti.getMes()) + "\"[label = \"" + str(tempVerti.getMes()) + "\", style = filled, fillcolor=\"#E1E16E\", fontcolor=\"#040404\", shape=box]\n")
                if (tempVerti.abajo != None):
                    file.write("\"n" + str(tempVerti.getMes()) + "\" -> \"n" + str(tempVerti.abajo.getMes()) + "\"[rankdir=UD];\n")
                    file.write("\"n" + str(tempVerti.abajo.getMes()) + "\" -> \"n" + str(tempVerti.getMes()) + "\"\n")

                if (tempVerti.derecha != None):
                    file.write("\"n" + str(tempVerti.derecha.getMes()) + "," + str(
                        tempVerti.derecha.getDia()) + "," + str(
                        tempVerti.derecha.getAno()) + "\"[label = \"" + str(
                        tempVerti.derecha.getDia()) + "\", style = filled, fillcolor=\"#5C5C5A\", fontcolor=\"#FCFC29\", shape=circle]\n")
                    file.write("\"n" + str(tempVerti.getMes()) + "\" -> \"n" + str(tempVerti.derecha.getMes()) + ","+ str(tempVerti.derecha.getDia()) +","+ str(tempVerti.derecha.getAno()) + "\"[constraint=false];\n")
                    file.write("\"n" + str(tempVerti.derecha.getMes()) + ","+ str(tempVerti.derecha.getDia()) +","+ str(tempVerti.derecha.getAno()) + "\" -> \"n" + str(tempVerti.getMes()) + "\"[constraint=false];\n")
                    file.write("{rank=same; \"n" + str(tempVerti.getMes()) + "\"  \"n" + str(tempVerti.derecha.getMes()) + ","+ str(tempVerti.derecha.getDia()) +","+ str(tempVerti.derecha.getAno()) + "\"}\n")
                    file.write("{rank=same; \"n" + str(tempVerti.derecha.getMes()) + ","+ str(tempVerti.derecha.getDia()) +","+ str(tempVerti.derecha.getAno()) + "\"  \"n" + str(tempVerti.getMes()) + "\"}\n")
                    AUXtempVerti = tempVerti.derecha

                while (AUXtempVerti.derecha != None):
                    file.write("\"n" + str(AUXtempVerti.derecha.getMes()) + ","+ str(AUXtempVerti.derecha.getDia()) +","+ str(AUXtempVerti.derecha.getAno()) +"\"[label = \""
                               + str(AUXtempVerti.derecha.getDia()) + "\", style = filled, fillcolor=\"#5C5C5A\", fontcolor=\"#FCFC29\", shape=circle]\n")
                    file.write("\"n" + str(AUXtempVerti.getMes()) + ","+ str(AUXtempVerti.getDia()) +","+ str(AUXtempVerti.getAno()) + "\" -> \"n"
                               + str(AUXtempVerti.derecha.getMes()) + ","+ str(AUXtempVerti.derecha.getDia()) +","+ str(AUXtempVerti.derecha.getAno()) + "\"[constraint=false];\n")
                    file.write("\"n" + str(AUXtempVerti.derecha.getMes()) + ","+ str(AUXtempVerti.derecha.getDia()) +","+ str(AUXtempVerti.derecha.getAno())
                               + "\" -> \"n" + str(AUXtempVerti.getMes()) + ","+ str(AUXtempVerti.getDia()) +","+ str(AUXtempVerti.getAno()) + "\"[constraint=false];\n")
                    file.write("{rank=same; \"n" + str(AUXtempVerti.getMes()) + ","+ str(AUXtempVerti.getDia()) +","+ str(AUXtempVerti.getAno()) + "\" \"n" + str(AUXtempVerti.derecha.getMes())
                               + ","+ str(AUXtempVerti.derecha.getDia()) +","+ str(AUXtempVerti.derecha.getAno()) + "\"}\n");
                    file.write("{rank=same; \"n" + str(AUXtempVerti.derecha.getMes()) + ","+ str(AUXtempVerti.derecha.getDia()) +","+ str(AUXtempVerti.derecha.getAno()) + "\" \"n"
                               + str(AUXtempVerti.getMes()) + ","+ str(AUXtempVerti.getDia()) +","+ str(AUXtempVerti.getAno()) + "\"}\n");

                    AUXtempVerti = AUXtempVerti.derecha

                tempVerti = tempVerti.abajo


            file.write("\"INICIO\" -> \"n" + str(tempHorizont.getAno()) + "\"\n")
            file.write("{rank=same; \"INICIO\"  \"n" + str(tempHorizont.getAno()) + "\"}\n")
            while tempHorizont != None:
                file.write("\"n" + str(tempHorizont.getAno()) + "\"[label = \"" + str(tempHorizont.getAno()) + "\", style = filled, fillcolor=\"#E1E16E\", fontcolor=\"#040404\", shape=box]\n")
                if (tempHorizont.derecha != None):
                    file.write("\"n" + str(tempHorizont.getAno()) + "\" -> \"n" + str(tempHorizont.derecha.getAno()) + "\"\n")
                    file.write("\"n" + str(tempHorizont.derecha.getAno()) + "\" -> \"n" + str(tempHorizont.getAno()) + "\"\n")
                    file.write("{rank=same; \"n" + str(tempHorizont.getAno()) + "\"  \"n" + str(tempHorizont.derecha.getAno()) + "\"}\n")
                    file.write("{rank=same; \"n" + str(tempHorizont.derecha.getAno()) + "\"  \"n" + str(tempHorizont.getAno()) + "\"}\n")

                if (tempHorizont.abajo != None):
                    file.write("\"n" + str(tempHorizont.getAno()) + "\" -> \"n" + str(tempHorizont.abajo.getMes()) + ","+ str(tempHorizont.abajo.getDia()) +","+ str(tempHorizont.abajo.getAno()) + "\"[rankdir=UD];\n")
                    file.write("\"n" + str(tempHorizont.abajo.getMes()) + ","+ str(tempHorizont.abajo.getDia()) +","+ str(tempHorizont.abajo.getAno()) + "\" -> \"n" + str(tempHorizont.getAno()) + "\"\n")
                    AUXtempHorizont = tempHorizont.abajo

                while (AUXtempHorizont.abajo != None):
                    file.write("\"n" + str(AUXtempHorizont.getMes()) + ","+ str(AUXtempHorizont.getDia()) +","+ str(AUXtempHorizont.getAno()) + "\" -> \"n"
                               + str(AUXtempHorizont.abajo.getMes()) + ","+ str(AUXtempHorizont.abajo.getDia()) +","+ str(AUXtempHorizont.abajo.getAno()) + "\"[rankdir=UD];\n")
                    file.write("\"n" + str(AUXtempHorizont.abajo.getMes()) + ","+ str(AUXtempHorizont.abajo.getDia()) +","+ str(AUXtempHorizont.abajo.getAno())
                               + "\" -> \"n" + str(AUXtempHorizont.getMes()) + ","+ str(AUXtempHorizont.getDia()) +","+ str(AUXtempHorizont.getAno()) + "\"\n")

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
                        file.write("\"extra" + str(AUXtempVerti.getAno()) + "\"[label = \"" + str(AUXtempVerti.derecha.getAno()) + "\", style = filled, shape=box]\n")

                    if AUXtempVerti.atras != None:
                        file.write("\"extra" + str(AUXtempVerti.getAno()) + "\"[label = \"" + str(
                            AUXtempVerti.getAno()) + "\", style = filled, shape=box]\n")
                        file.write("\"n" + str(AUXtempVerti.atras.getMes()) + "," + str(
                            AUXtempVerti.atras.getDia()) + "," + str(
                            AUXtempVerti.atras.getAno()) + "\"[label = \"" + str(
                            AUXtempVerti.atras.getDia())  + "\", style = filled, shape=circle]\n")
                        file.write("\"extra" + str(AUXtempVerti.getAno()) + "\" -> \"n" + str(AUXtempVerti.atras.getMes()) + "," + str(
                            AUXtempVerti.atras.getDia()) + "," + str(
                            AUXtempVerti.atras.getAno()) +"\"\n")
                        file.write("\"n" + str(AUXtempVerti.atras.getMes()) + "," + str(
                            AUXtempVerti.atras.getDia()) + "," + str(
                            AUXtempVerti.atras.getAno()) + "\" -> \"extra" + str(AUXtempVerti.getAno()) +"\"\n")
                        AUX2Verti = AUXtempVerti.atras

                        while (AUX2Verti.atras != None):
                            file.write("\"n" + str(AUX2Verti.atras.getMes()) + ","+ str(AUX2Verti.atras.getDia()) +","+ str(AUX2Verti.atras.getAno()) +"\"[label = \"" + str(AUX2Verti.atras.getDia()) + "\", style = filled, shape=circle]\n")
                            file.write("\"n" + str(AUX2Verti.getMes()) + ","+ str(AUX2Verti.getDia()) +","+ str(AUX2Verti.getAno()) + "\" -> \"n"
                                       + str(AUX2Verti.atras.getMes()) + ","+ str(AUX2Verti.atras.getDia()) +","+ str(AUX2Verti.atras.getAno()) + "\"\n")
                            file.write("\"n" + str(AUX2Verti.atras.getMes()) + ","+ str(AUX2Verti.atras.getDia()) +","+ str(AUX2Verti.atras.getAno())
                                       + "\" -> \"n" + str(AUX2Verti.getMes()) + ","+ str(AUX2Verti.getDia()) +","+ str(AUX2Verti.getAno()) + "\"\n")

                            AUX2Verti = AUX2Verti.atras

                    AUXtempVerti = AUXtempVerti.derecha


                if AUXtempVerti.atras != None:
                    file.write("\"extra" + str(AUXtempVerti.getAno()) + "\"[label = \"" + str(
                        AUXtempVerti.getAno()) + "\", style = filled, shape=box]\n")
                    file.write("\"n" + str(AUXtempVerti.atras.getMes()) + "," + str(
                            AUXtempVerti.atras.getDia()) + "," + str(
                            AUXtempVerti.atras.getAno()) + "\"[label = \"" + str(
                            AUXtempVerti.atras.getDia())  + "\", style = filled, shape=circle]\n")
                    file.write("\"extra" + str(AUXtempVerti.getAno()) + "\" -> \"n" + str(AUXtempVerti.atras.getMes()) + "," + str(
                            AUXtempVerti.atras.getDia()) + "," + str(
                            AUXtempVerti.atras.getAno()) + "\"\n")
                    file.write("\"n" + str(AUXtempVerti.atras.getMes()) + "," + str(
                            AUXtempVerti.atras.getDia()) + "," + str(
                            AUXtempVerti.atras.getAno()) + "\" -> \"extra" + str(AUXtempVerti.getAno()) +"\"\n")
                    AUX2Verti = AUXtempVerti.atras

                    while (AUX2Verti.atras != None):
                        file.write("\"n" + str(AUX2Verti.atras.getMes()) + ","+ str(AUX2Verti.atras.getDia()) +","+ str(AUX2Verti.atras.getAno()) +"\"[label = \"" + str(AUX2Verti.atras.getDia()) + "\", style = filled, shape=circle]\n")
                        file.write("\"n" + str(AUX2Verti.getMes()) + ","+ str(AUX2Verti.getDia()) +","+ str(AUX2Verti.getAno()) + "\" -> \"n"
                            + str(AUX2Verti.atras.getMes()) + ","+ str(AUX2Verti.atras.getDia()) +","+ str(AUX2Verti.atras.getAno()) + "\"\n")
                        file.write("\"n" + str(AUX2Verti.atras.getMes()) + ","+ str(AUX2Verti.atras.getDia()) +","+ str(AUX2Verti.atras.getAno())
                            + "\" -> \"n" + str(AUX2Verti.getMes()) + ","+ str(AUX2Verti.getDia()) +","+ str(AUX2Verti.getAno()) + "\"\n")

                        AUX2Verti = AUX2Verti.atras

                tempVerti = tempVerti.abajo

            file.write("label = \"PROFUNDIDAD\";\n")
            file.write("}\n")
            file.write("}")
            file.close()
            os.system("dot -Tjpg matriz.dot > matriz.jpg")
