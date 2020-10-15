from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato


# Create your views here.
def login(request):
    if request.method != 'POST': 
        return render(request, 'accounts/login.html')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)
    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Voce fez login com sucesso.')
        return redirect('dashboard')
    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('dashboard')
    

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    usuario = request.POST.get('usuario')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')


    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return render(request, 'accounts/cadastro.html')
    
    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuario já existe!')
        return render(request, 'accounts/cadastro.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'Email já cadastrado!')
        return render(request, 'accounts/cadastro.html')

    
    
    if not nome or not sobrenome or not usuario or not email or not senha or not senha2:
        messages.error(request, 'Nenhum Campo pode estar vázio')
        return render(request, 'accounts/cadastro.html')
    
    if len(senha) < 6:
        messages.error(request, 'Senha deve ter no minimo 6 caracteres')
        return render(request, 'accounts/cadastro.html')

    if len(usuario) < 6:
        messages.error(request, 'Usuario deve ter no minimo 6 caracteres')
        return render(request, 'accounts/cadastro.html')
    
    if senha != senha2:        
        messages.error(request, 'Senhas diferentes')
        return render(request, 'accounts/cadastro.html')
    
    
    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome,last_name=sobrenome)
    messages.success(request, 'Registrado com Sucesso')
    return redirect('login')
      

@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContato()
        return render(request, 'accounts/dashboard.html', {'form': form})
    form = FormContato(request.POST, request.FILES)
    if not form.is_valid():
        messages.error(request, 'Erro ao enviar formulário.')
        form = FormContato(request.POST)        
        return render(request, 'accounts/dashboard.html', {'form': form})
    descricao = request.POST.get('descricao')
    if len(descricao) < 5:
        messages.error(request, 'Descriçao precisa ter mais que 5 caracteres')
        form = FormContato(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()
    messages.success(request, 'Cadastrado no Banco com Sucesso!')
    return redirect('dashboard')