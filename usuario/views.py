from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import UsuarioDS16
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def create_user(request):
    telefone = request.data.get('telefone')

  
    
    if UsuarioDS16.objects.filter(telefone=telefone).exists():
        return Response ({'Erro':f'telefone {telefone} já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    usuario = UsuarioDS16.objects.create_user(
            telefone=telefone,
        
    )
    return Response({'Mensagem': f'Usuário {telefone} criado com sucesso'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def logar_usuario(request):
    telefone = request.data.get('telefone')

    usuario  =  authenticate(telefone = telefone)

    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'acesso': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_200_OK)
    else:
        return Response ({'Erro':'Usuario ou/e senha incorreto(s)'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def output_user(request):
    return Response({'Mensagem':'Olá! DS16'}, status=status.HTTP_200_OK)