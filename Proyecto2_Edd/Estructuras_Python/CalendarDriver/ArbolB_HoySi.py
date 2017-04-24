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

    cuentas = 0
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
        self.Xder = self.Xizq = None
        X = None
        Xr = None


    def Vacio(self, raiz):
        return raiz == None or raiz.a.







