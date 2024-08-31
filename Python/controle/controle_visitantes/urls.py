
"""
Para registrar a nova pagina de cadastro registrar_visitante com nome no path nome da pagina, 
chamar função que foi registrada na views, name é sempre o mesmo criado na função.
"""
from django.contrib import admin
from django.urls import path
from dashboard.views import index
from visitantes.views import registrar_visitante, informacoes_visitante


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('registrar-visitante/', registrar_visitante, name="registrar_visitantes"),
    path('informacoes-visitante/<int:id>/', informacoes_visitante, name="informacoes_visitante")
]