from django.http import HttpResponse
from datetime import datetime
from django.template import Template , Context, loader


def saludo(request):
    return HttpResponse("Holis")


def dia_hoy(request, nombre):
    hoy = datetime.now()

    respuesta = f"Hoy es {hoy}, Holis {nombre}"
    return HttpResponse(respuesta)


def edad(request, edad):
    edad = int(edad)
    anio = datetime.now().year - edad
    return HttpResponse(f"El año en que naciste es: {anio}")


#def vista_plantilla(request):
#    archivo = open(r"C:\Users\Gerardo\Desktop\CoderHoyse\Clase_17\Primer_proyecto_django\Primer_proyecto_django\Templates\Plantilla.html")
#
#    plantilla = Template(archivo.read())
#
#    archivo.close()
#
#    contexto = Context()
#
#    documento = plantilla.render(contexto)
#
#    return HttpResponse(documento)


def vista_plantilla(request):


    datos = {
        "Nombre": "Gerardo",
        "Apellido": "Campero",
        "Fecha" : datetime.now(),
    }

    plantilla = loader.get_template("Plantilla.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)


def listado_alumnos(request):


    lista_de_alumnos = ["Pepe", "Pepa", "Pipo", "Pupo", "Pipe"]

    datos = {
        "tecnologia": "Python",
        "lista_de_alumnos": lista_de_alumnos
    }

    
    plantilla = loader.get_template("Plantilla.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)

    
def listado_alumnos2 (request):
    
    lista_de_alumnos = ["Pepe", "Pepa", "Pipo", "Pupo", "Pipe"]

    datos = {
        "tecnologia": "Python",
        "lista_de_alumnos": lista_de_alumnos
    }

    plantilla = loader.get_template("listado_alumnos.html")
    documento = plantilla.render(datos)

    return HttpResponse(documento)

