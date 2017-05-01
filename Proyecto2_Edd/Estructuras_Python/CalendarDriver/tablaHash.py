import os

class nodo_hash:
    def __init__(self, nombre, direccion, descripcion, hora):
        self.nombre = nombre
        self.direccion = direccion
        self.descripcion = descripcion
        self.hora = hora

    def get_name(self):
        return self.nombre

    def get_dir(self):
        return self.direccion

    def get_descrip(self):
        return self.descripcion

    def get_hora(self):
        return self.hora

class tablaHash:

    def __init__(self):
        self.tamano = 7
        self.cantidad = 0
        self.nodoHash = [None]*self.tamano

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
            #print(self.nodoHash[posicion].get_name())
            if (posicion < len(self.nodoHash)):
                if(self.nodoHash[posicion] == None):
                    self.nodoHash[posicion] = nuevoNodo
                    self.cantidad.__add__(1)
                    ingresa = True

                elif(self.nodoHash[posicion] != None):
                    posicion = self.seChoco(posicion)
                    colision += 1

            else:
                self.REhash()


    def numeroPrimo(self, dato):
        numero = 2
        siEs = True

        while (siEs == True) and (numero != dato):
            if(dato % numero == 0):
                siEs = False
            numero+=1

        return siEs


    def seChoco(self, num):
        return ( num + 1 )
        #pos = 0
        #asciiCode = []
        #chars = name
        #chars.strip()
        #for i in chars:
        #    asciiCode = ord(i)

        #for a in range(0, 3):
        #   pos = pos + asciiCode[a]

        #pos.__add__(int((num + 1).__pow__(2)))

        #return (pos % self.tamano)


    def REhash(self):
        print("ENTRA REHASH")
        tamano2 = self.tamano + 1
        SiEsPrimo = self.numeroPrimo(tamano2)

        while (SiEsPrimo == False):
            tamano2 += 1
            SiEsPrimo = self.numeroPrimo(tamano2)

        otroHash=[None]*tamano2

        for a in range(0, self.tamano):
            if(self.nodoHash[a] != None):
                otroHash[a] = self.nodoHash[a]

        self.tamano = tamano2
        self.nodoHash = [None]*self.tamano
        self.nodoHash = otroHash


    def delete(self, nombre):
        for i in range(0, self.tamano):
            if((self.nodoHash[i] != None) and (self.nodoHash[i].get_name() == nombre)):
                self.nodoHash[i] = None
                self.cantidad = self.cantidad - 1

    def imprimir(self):
        for i in range(0, self.tamano):
            if(self.nodoHash[i] != None):
                print(self.nodoHash[i].get_name()+"")
                print(str(len(self.nodoHash)))

#--------------------------------------------------------------------------------------------------------------------
#-------------------------------------------- PRUEBAS ---------------------------------------------------------------
# colita = Cola()
# colita.ingresar(3)
# colita.ingresar(5)
# colita.ingresar(7)
# colita.ingresar(9)

hashi = tablaHash()
hashi.insertar("rafa", "usac", "la mera verga", "son las que te importa")
hashi.insertar("pedro", "usac", "la mera verga", "son las que te importa")
hashi.insertar("felipe", "usac", "la mera verga", "son las que te importa")
hashi.insertar("kam", "usac", "la mera verga", "son las que te importa")
hashi.insertar("tom", "usac", "la mera verga", "son las que te importa")
hashi.insertar("kamasutra", "usac", "la mera verga", "son las que te importa")
hashi.insertar("margarita", "usac", "la mera verga", "son las que te importa")
hashi.insertar("PUTOS", "usac", "la mera verga", "son las que te importa")
hashi.insertar("putas ricas", "usac", "la mera verga", "son las que te importa")
hashi.imprimir()