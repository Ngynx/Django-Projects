from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola, estas en el index de encuestas")

def detalle(request, pregunta_id):
    return HttpResponse("Estas viendo la pregunta %s." % pregunta_id)

def resultados(request, pregunta_id):
    response = "Estas viendo los resultados de la pregunta %s."
    return HttpResponse(response % pregunta_id)

def votar(request, pregunta_id):
    return HttpResponse("Estas votando por la pregunta %s." % pregunta_id)

def sumar(request, pregunta_id, numero):
    numero1 = int(pregunta_id)
    numero2 = int(numero)
    return HttpResponse("La suma de los numeros es: %s" % (numero1 + numero2))

def restar(request, pregunta_id, numero):
    numero1 = int(pregunta_id)
    numero2 = int(numero)
    return HttpResponse("La resta de los numeros es: %s" % (numero1 - numero2))

def multiplicar(request, pregunta_id, numero):
    numero1= int(pregunta_id)
    numero2= int(numero)
    return HttpResponse("la multiplicacion de los numeros es: %s" % (numero1 * numero2))

