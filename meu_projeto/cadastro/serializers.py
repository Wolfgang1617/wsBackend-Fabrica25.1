from rest_framework import serializers
from .models import Usuario, Filme

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    filmes = FilmeSerializer(many=True, read_only=True)

    class Meta:
        model = Usuario
        fields = '__all__'