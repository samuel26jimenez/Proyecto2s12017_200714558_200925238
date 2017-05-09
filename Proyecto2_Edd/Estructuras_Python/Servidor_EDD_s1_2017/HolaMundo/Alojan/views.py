from django.http import response


def HolaMundo(requets, string ):
    print('Salida de Hola Mundo ' + string +'\n')
    return response

def HolaMundoOtro(requets):
    if requets.method == 'POST':
        print('Salida de Hola Mundo Otro\n')
    else:
        print('Salida de Hola Mundo Otro Error\n')
    return response