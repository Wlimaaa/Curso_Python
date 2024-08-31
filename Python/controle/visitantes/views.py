"""
Para registrar a nova pagina de cadastro registrar_visitante , context é criado para integra o python com o html
"""
from django.shortcuts import render, redirect, get_object_or_404
from visitantes.forms import VisitanteForm
from porteiros.models import Porteiro
from django.contrib import messages
from visitantes.models import Visitante

def registrar_visitante(request):
    form = VisitanteForm()
    if request.method=="POST":
        form=VisitanteForm(request.POST)
        
        if form.is_valid():
            visitante = form.save(commit=False)
            visitante.registrado_por = Porteiro.objects.get(id=1)
            visitante.save()
            
            messages.success(
                request,
                "O Visitante foi registrado com sucesso!"
            )
            return redirect ("index")
            
    context = {
        "nome_pagina":"Registrar visitante",
        "form": form
    }
    return render(request, "Telacadastrovisitantes.html", context)

def informacoes_visitante(request, id):
    visitante = get_object_or_404(
        Visitante,
        id=id
    )
    
    context={
        "nome_pagina":"informaçoes do visitante",
        "visitante":visitante
        
    }
    
    return render (request, "informacoes_visitante.html", context)