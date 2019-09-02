from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola, estas en la parte principal de nuestra Aplicacion")

def sumar(request, numero1, numero2):
    a = int(numero1)
    b = int(numero2)
    return HttpResponse("La suma de los numeros ingresados es: %s" % (a+b))

def restar(request, numero1, numero2):
    a = int(numero1)
    b = int(numero2)
    return HttpResponse("La resta de los numeros ingresados es: %s" % (a-b))

def multiplicar(request, numero1, numero2):
    a = int(numero1)
    b = int(numero2)
    return HttpResponse("La multiplicacion de los numeros ingresados es: %s" % (a*b))




