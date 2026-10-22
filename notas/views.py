from django.shortcuts import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Bienvenido a la página de inicio de Notas.</h1><p>Esta es la página principal de la aplicación de Notas.</p>")
    
