from django.shortcuts import render
from .models import Usuario # type: ignore

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'index.html', {'usuarios': usuarios})