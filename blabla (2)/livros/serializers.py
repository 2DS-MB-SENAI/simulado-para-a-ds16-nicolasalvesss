from .models import Livros
from rest_framework import serializers 

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields = "__all__"