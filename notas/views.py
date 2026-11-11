from django.shortcuts import HttpResponse
from notas.models import Nota

def index(request):
    notas = Nota.objects.count()
    return HttpResponse(
        f"<h1>Notas</h1><p>Total de notas: {notas}</p>"
        f"<footer><p>Desarrollado por: Tu Nombre</p></footer>"
    )
    