from django.shortcuts import render
from .models import Usuario
from django.shortcuts import render, redirect  # redireciona a outra pagina
from django.core.exceptions import ValidationError
from asgiref.sync import sync_to_async
from django.http import JsonResponse

def home(request):
    return render (request,'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':  # se for um POST (envio de formulário)
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.save()
        return redirect('listagem_usuarios')  # redirecionamento para evitar duplicação
    
    # se for GET (apenas carregamento da página)
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)
