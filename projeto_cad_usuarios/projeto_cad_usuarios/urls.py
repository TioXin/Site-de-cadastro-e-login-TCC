from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota, view responsável, nome de referencia
     path('', views.home, name='home'), #definição do path (pode ser usuarios.com, mas se usado path("admin/") ficaria usuarios.com/admin)
    #  usuarios.com/usuarios
   path('usuarios/', views.usuarios, name='listagem_usuarios')
   #AJAX

]
