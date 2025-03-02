import requests
from rest_framework import viewsets
from .models import Usuario, Filme
from django.shortcuts import render
from .serializers import UsuarioSerializer, FilmeSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'cadastro/index.html', {'usuarios': usuarios})    

def buscar_filme_no_omdb(titulo):
    api_key = 'bf3eee38'  
    url = f'http://www.omdbapi.com/?apikey={api_key}&t={titulo}'
    response = requests.get(url)
    return response.json()

# Create your views here.