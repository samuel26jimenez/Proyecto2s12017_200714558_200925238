__autor__ = 'Samuel'

import os

class Lista_Nodo:
    def __init__(self, cad_tecla):
        self.cad_tecla = cad_tecla
        self.Lsig = None
        self.Lant = None

    def set_cadTecla(self, cad_tecla):
        self.cad_tecla = cad_tecla

    def get_cadTecla(self):
        return self.cad_tecla



class Metodo_Lista:
    def __init__(self):
        self.ini = None
        self.ult = None



    def esVacio(self):
        if self.ini == None:
            return True
        else:
            return False




    def _Inserta_Nodo(self, cadenas):
        _nvo_Nodo = Lista_Nodo(cadenas)
        if self.esVacio() == True:
            self.ini = self.ult = _nvo_Nodo
        else:
            #self.ult.Lsig = _nvo_Nodo
            #self.ult = self.ult.Lsig
            #------------------
            if(cadenas < self.ini.cad_tecla):
                self._Inserta_inicio(_nvo_Nodo)
            elif(cadenas > self.ult.cad_tecla):
                self._Inserta_final(_nvo_Nodo)
            else:
                self._Inserta_medio(_nvo_Nodo)



    def _Inserta_inicio(self, cadenas):
        self.ini.Lant = cadenas
        cadenas.Lsig = self.ini
        self.ini = self.ini.Lant

    def _Inserta_final(self, cadenas):
        self.ult.Lsig = cadenas
        cadenas.Lant = self.ult
        cadenas.Lsig = None
        self.ult = self.ult.Lsig


    def _Inserta_medio(self, cadenas):
        tempo1 = tempo2 =  None
        tempo1 = self.ini

        while  tempo1.Lsig != None:
            if(tempo1.cad_tecla > cadenas.cad_tecla):
                break
            tempo2 = tempo1
            tempo1 = tempo1.Lsig
        #while(tempo1.self.cad_tecla < cadenas.cad_tecla):
        #    tempo1 = tempo1.self.Lsig
        #tempo2 = tempo1.self.Lant


        tempo2.Lsig  = cadenas
        cadenas.Lant = tempo2

        tempo1.Lant = cadenas
        cadenas.Lsig = tempo1



    def _Eliminar_N(self, cad_ena):
        if self.esVacio() == True:
            print "Lista Vacia"
        else:
            self.borr = Lista_Nodo
            self.borr = self.ini
            self.aux = None
            while(self.borr != None and self.borr.cad_tecla != cad_ena):
                self.aux = self.borr
                self.borr = self.borr.Lsig
            if self.borr == None:
                print "No Existe Dato"
            else:
                if self.borr.cad_tecla == cad_ena:
                    if self.borr == self.ini:
                        self.ini = self.ini.Lsig
                    else:
                        self.aux.Lsig = self.borr.Lsig
                else:
                    if self.aux == None:
                        self.aux = self.borr.Lsig
                        self.ini = self.borr.Lsig
                        self.borr = None




    def _Mostrar(self):
        self.temporal = self.ini
        while(self.temporal != None):
            print self.temporal.get_cadTecla()
            self.temporal = self.temporal.Lsig





    def search(self, cadena):
        if self.esVacio() == False:
            aux = self.ini
            while aux != None and aux.get_cadTecla() != cadena:
                aux = aux.Lsig

            if  aux != None and aux.get_cadTecla() == cadena:
                print "cadena: "+ aux.get_cadTecla()
            else:
                print "Cadena No Existe"


    def grafica_Lista(self):
        if self.esVacio() == True:
            return
        else:
            archivo = open("grafica_listaUs.dot","w")
            archivo.write("digraph G{\n rankdir = LR;")
            tempo = self.ini
            tempo2 = self.ult
            i = 0
            while tempo != None:
                archivo.write("\"Node"+str(i)+"\"[label = \""+tempo.get_cadTecla()+"\" style=filled]\n")
                if tempo.Lsig != None:
                    archivo.write("\"Node"+str(i)+"\" -> \"Node"+str(i+1)+"\"")
                if tempo2.Lant != None:
                    archivo.write("\"Node"+str(i+1)+"\" -> \"Node"+str(i)+"\"")
                i = i + 1
                tempo = tempo.Lsig
                tempo2 = tempo2.Lant
            archivo.write("}")
            archivo.close()
            os.system("dot -Tpng grafica_listaUs.dot > grafica_listaUs.png")


class opcion:
        a = Metodo_Lista()
        a._Inserta_Nodo("Usuario2")
        a._Inserta_Nodo("Usuario1")
        a._Inserta_Nodo("Usuario5")
        a._Inserta_Nodo("Usuario4")
        a._Inserta_Nodo("Usuario3")
        a._Inserta_Nodo("Usuario51")
        a._Inserta_Nodo("Usuario73")
        a._Inserta_Nodo("Usuario6")
        a._Mostrar()
        a.grafica_Lista()

