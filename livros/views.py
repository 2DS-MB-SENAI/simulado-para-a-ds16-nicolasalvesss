from django.shortcuts import render , redirect , get_object_or_404
from .models import Livros
from .forms import ItemForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import LivroSerializer

def read(request):
    livros = Livros.objects.all()
    return render(request, 'livros.html', {'livros':livros})

@api_view(['GET','POST'])
def read_api(request):
    if request.method == "GET":
        try:
            livros = Livros.objects.get 
        except Livros.DoesNotExist:
            return Response({'erro': 'Evento inexistente'}, status= status.HTTP_404_NOT_FOUND)
    
    if request.method == "POST":
        serializer = LivroSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
