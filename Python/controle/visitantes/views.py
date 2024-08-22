
from django.shortcuts import render

def registrar_visitante(request):
    context = {}
    
    return render(request, "Telacadastrovisitantes.html", context)
