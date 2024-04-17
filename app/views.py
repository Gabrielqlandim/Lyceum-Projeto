from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as lg
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Aluno
from .models import Aviso


#home
def home(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'pages/home.html')
    else:
        return HttpResponseRedirect('/')
#login
def login(request):
    if request.method == 'GET':
        return render(request, 'pages/login.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        senha = request.POST.get('senha')
        
        user = authenticate(request,username=name,password=senha)

        if user:
            lg(request, user)
            return HttpResponseRedirect('/home')
        else:
            print(user)
            return HttpResponse('email ou senha invalidos')
        
        
def cadastro_prof(request):
    if request.method == 'GET':
        return render(request, 'pages/cadastro.html' )
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=name).first()

        if user:
            messages.success(request, 'Usuário já existente.')
            return HttpResponseRedirect('/cadastro/')
        else:
            user = User.objects.create_user(username=name,email=email,password=senha)
            user.save()

            messages.success(request, 'Usuário cadastrado!')
        return HttpResponseRedirect('/')

#cadastro de aluno
def cadastrar_alunos(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_active:
            return render(request, 'pages/alunos/cadastrar_alunos.html')
        else:
            return HttpResponseRedirect('/')
    elif request.method == 'POST':
        aluno_name = request.POST.get('nome-aluno')
        aluno_turma = request.POST.get('turma-aluno')
        data_matriculado = request.POST.get('data-aluno')

        aluno = Aluno(nome=aluno_name,serie_turma=aluno_turma,data_matricula=data_matriculado)
        aluno.save()

        return HttpResponseRedirect('/alunos/')

#atualizar alunos
def atualizar_alunos(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_active:
            id = request.GET['atualizar']
            return render(request, 'pages/alunos/atualizar_alunos.html', {'id_aluno': id})


#editar alunos (em processo de desenvolvimento, não funcional)
    
def editar_alunos(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_active:
            alunos = Aluno.objects.all()
            return render(request, 'pages/alunos/editar_alunos.html', {'alunos': alunos})
        else:
            return HttpResponseRedirect('/')
    elif request.method == 'POST':
        if 'remover' in request.POST:
            pk = request.POST.get('remover')
            aluno = Aluno.objects.get(id_aluno=pk)
            aluno.delete()
            return HttpResponseRedirect('/editar_alunos/')
        if 'atualizar' in request.POST:
            return render(request, 'pages/alunos/atualizar_alunos/')

def alunos(request):
    if request.user.is_authenticated and request.user.is_active:
        alunos = Aluno.objects.all()
        return render(request, 'pages/alunos.html', {'alunos': alunos})
    else:
        return HttpResponseRedirect('/')
    
    

def disciplinas(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'pages/disciplinas.html')
    else:
        return HttpResponseRedirect('/')

def calendario_academico(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'pages/calendario_academico.html')
    else:
        return HttpResponseRedirect('/')


def perfil(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_active:
            return render(request, 'pages/perfil.html')
        else:
            return HttpResponse('Você precisa estar logado!')
    if request.method == 'POST':
        user = User.objects.filter().first()
        logout(request)
        return HttpResponseRedirect('/')

#Alunos
def plataforma(request):
    if request.user.is_authenticated:
        return
    else:
        return HttpResponseRedirect('/')
