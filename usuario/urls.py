from django.urls import path
from .import views

urlpatterns =[
    path('auth/registro/', view=views.create_user, name='create_usuario'),
    path('auth/login', view=views.logar_usuario, name='logar_usuario'),
    path('output/', view=views.output_user, name='output_user')
    
]