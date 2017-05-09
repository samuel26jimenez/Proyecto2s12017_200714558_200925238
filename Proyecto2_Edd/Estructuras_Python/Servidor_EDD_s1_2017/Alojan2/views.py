from django.http import response


def HolaMundo(requets, string ):
    if requets.method == "GET":
        print('Salida de Hola Mundo ' + string +'\n')
    return  requets

def HolaMundoOtro(requets):
    if requets.method == 'POST':
        if requets.method['p'] != None and requets.method['p'] != "":
            print 'La salida Recivida ' + requets.method['p']
        else:
            print('Salida de Hola Mundo Otro\n')
    else:
        print('Salida de Hola Mundo Otro Error\n')
    return requets

def HolaMundoOtro2(requets):
    if requets.method == 'POST':
        if requets.method['p'] != None and requets.method['p'] != "":
            print 'La salida Recivida ' + requets.method['p']
        else:
            print('Salida de Hola Mundo Otro\n')
    else:
        print('Salida de Hola Mundo Otro Error\n')
    return