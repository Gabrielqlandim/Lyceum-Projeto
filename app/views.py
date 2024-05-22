from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as lg
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Aluno
from .models import Materia

from datetime import date
#home
def home(request):
    if request.user.is_authenticated and request.user.is_active:
        user = request.user
        return render(request, 'pages/home.html', {'username': user})
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

#editar alunos
def editar_alunos(request):
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_active:
            alunos = Aluno.objects.all()
            return render(request, 'pages/alunos/editar_alunos.html', {'alunos': alunos, 'check': 0, 'name': '', 'serie_turma': '', 'data_matricula': '', 'id':''})
        else:
            return HttpResponseRedirect('/')
    elif request.method == 'POST':
        if 'remover' in request.POST:
            pk = request.POST.get('remover')
            aluno = Aluno.objects.get(id_aluno=pk)

            materias = Materia.objects.all()
            for materia in materias:
                if(materia.aluno == aluno):
                    materia.delete()
                    
            aluno.delete()
            return HttpResponseRedirect('/editar_alunos/')
        if 'atualizar' in request.POST:
            alunos = Aluno.objects.all()
            id = request.POST.get("atualizar")
            aluno = Aluno.objects.get(id_aluno=id)
            nome = aluno.nome
            serie_turma = aluno.serie_turma
            data_matricula = aluno.data_matricula
            return render(request, 'pages/alunos/editar_alunos.html', {'alunos': alunos, 'check': 1, 'name': nome, 'serie_turma': serie_turma, 'data_matricula': data_matricula, 'id':id})
        
        if 'atualizar_confirmar' in request.POST:
            alunos = Aluno.objects.all()
            id = request.POST.get("atualizar_confirmar")
            aluno = Aluno.objects.get(id_aluno=id)
            aluno.nome = request.POST.get("nome-aluno")
            aluno.serie_turma = request.POST.get("turma-aluno")
            aluno.data_matricula = request.POST.get("data-aluno")
            aluno.save()
            return render(request, 'pages/alunos/editar_alunos.html', {'alunos': alunos, 'check': 0, 'name': '', 'serie_turma': '', 'data_matricula': '', 'id':''})
        if 'atualizar_cancelar' in request.POST:
                alunos = Aluno.objects.all()
                return render(request, 'pages/alunos/editar_alunos.html', {'alunos': alunos, 'check': 0, 'name': '', 'serie_turma': '', 'data_matricula': '', 'id':''})

def alunos(request):
    if request.user.is_authenticated and request.user.is_active:
        if request.method == 'GET':
            alunos = Aluno.objects.all()
            return render(request, 'pages/alunos.html', {'alunos': alunos, 'check': 0})
        elif request.method == 'POST':
            if 'cadastrar' in request.POST:
                alunos = Aluno.objects.all()
                return render(request, 'pages/alunos.html', {'alunos': alunos, 'check': 1})
            elif 'cadastrar_confirmar' in request.POST:
                alunos = Aluno.objects.all()
                materias = ['portugues', 'matematica', 'historia', 'geografia', 'ciencias', 'ingles']
                aluno_name = request.POST.get('nome-aluno')
                aluno_turma = request.POST.get('turma-aluno')
                data_matriculado = request.POST.get('data-aluno')

                aluno = Aluno(nome=aluno_name,serie_turma=aluno_turma,data_matricula=data_matriculado)
                aluno.save()

                for materia in materias:
                    mateira_nova = Materia(aluno=aluno, nome_materia=materia, faltas=0, notas=0)
                    mateira_nova.save()

                return render(request, 'pages/alunos.html', {'alunos': alunos, 'check': 0})
            elif 'cadastrar_cancelar' in request.POST:
                alunos = Aluno.objects.all()
                return render(request, 'pages/alunos.html', {'alunos': alunos, 'check': 0})

        else:
            return HttpResponseRedirect('/')


# disciplinas
def disciplinas(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'pages/disciplinas.html')
    else:
        return HttpResponseRedirect('/')
    
def portugues(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'pages/disciplinas/portugues.html')
    else:
        return HttpResponseRedirect('/')

def matematica(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'pages/disciplinas/matematica.html')
    else:
        return HttpResponseRedirect('/')
    
def historia(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'pages/disciplinas/historia.html')
    else:
        return HttpResponseRedirect('/')
    
def geografia(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'pages/disciplinas/geografia.html')
    else:
        return HttpResponseRedirect('/')
    
def ciencias(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'pages/disciplinas/ciencias.html')
    else:
        return HttpResponseRedirect('/')
    
def ingles(request):
    if request.user.is_authenticated and request.user.is_active:
        return render(request, 'pages/disciplinas/ingles.html')
    else:
        return HttpResponseRedirect('/')
    
def notas(request):
    if request.user.is_authenticated and request.user.is_active:
        if(request.method == 'GET'):
            materia_escolhida = request.GET.get('notas')

            return render(request, 'pages/disciplinas/notas.html')
        if(request.method == 'POST'):
            return HttpResponseRedirect('/notas/')
    else:
        return HttpResponseRedirect('/')

def faltas(request):
    if request.user.is_authenticated and request.user.is_active:
        if(request.method == 'GET'):
            materias = Materia.objects.all()
            materia_escolhida = request.GET.get('faltas')
            
            # faz um array com todos os dados da materia escolhida
            dados_escolhidos = []
            for materia in materias:
                if(materia.nome_materia == materia_escolhida):
                    dados_escolhidos.append(materia)
    
            return render(request, 'pages/disciplinas/faltas.html', {'materia': dados_escolhidos, 'faltas': materia_escolhida})     
            
        elif(request.method == 'POST'):
            if request.POST.get('faltas_plus') != None:
                id_materia = request.POST.get('faltas_plus')
                materia_dados = Materia.objects.filter(id=id_materia).first()

                materia_escolhida = materia_dados.nome_materia
                id_aluno = materia_dados.aluno.id_aluno

                aluno = Aluno.objects.get(id_aluno=id_aluno)
                materia = Materia.objects.filter(aluno=aluno, nome_materia=materia_escolhida).first()

                materia.faltas += 1
                materia.save()
                return HttpResponseRedirect('/faltas/?faltas='+materia_escolhida)
            elif request.POST.get('faltas_minus') != None:
                id_materia = request.POST.get('faltas_minus')
                materia_dados = Materia.objects.filter(id=id_materia).first()

                materia_escolhida = materia_dados.nome_materia
                id_aluno = materia_dados.aluno.id_aluno

                aluno = Aluno.objects.get(id_aluno=id_aluno)
                materias = Materia.objects.all()

                # remove uma falta na materia escolhida
                materia = Materia.objects.filter(aluno=aluno, nome_materia=materia_escolhida).first()
                materia.faltas -= 1
                materia.save()
                return HttpResponseRedirect('/faltas/?faltas='+materia_escolhida)
    else:
        return HttpResponseRedirect('/')

#########################

def calendario_academico(request):
    if request.user.is_authenticated and request.user.is_active:
        if request.method == 'GET':
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
