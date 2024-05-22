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

#cadastro de aluno
def cadastrar_alunos(request):
    materias = ['portugues', 'matematica', 'historia', 'geografia', 'ciencias', 'ingles']
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

        for materia in materias:
            mateira_nova = Materia(aluno=aluno, nome_materia=materia, faltas=0, notas=0)
            mateira_nova.save()

        return HttpResponseRedirect('/alunos/')

#atualizar alunos
def atualizar_alunos(request):
    print("FUNÇÃO OK")
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_active:
            id = request.GET['atualizar']
            aluno = Aluno.objects.get(id_aluno=id)
            print("GET OK")
            return render(request, 'pages/alunos/atualizar_alunos.html', {'id_aluno': id, 'aluno': aluno})
    if request.method =='POST':
        print("POST OK")
        if 'att' in request.POST:
            id = request.POST.get("att")
            aluno = Aluno.objects.get(id_aluno=id)
            aluno.nome = request.POST.get('nome-aluno')
            aluno.serie_turma = request.POST.get('turma-aluno')
            aluno.data_matricula = request.POST.get('data-aluno')

            aluno = Aluno(id_aluno=id, nome=aluno.nome, serie_turma=aluno.serie_turma, data_matricula=aluno.data_matricula)
            aluno.save()
            print("ATT OK")
            return HttpResponseRedirect('/alunos/')


#editar alunos
    
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

            materias = Materia.objects.all()
            for materia in materias:
                if(materia.aluno == aluno):
                    materia.delete()
                    
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
            materias = Materia.objects.all()
            dados_escolhidos = []
            for materia in materias:
                if(materia.nome_materia == materia_escolhida):
                    dados_escolhidos.append(materia)
    
            return render(request, 'pages/disciplinas/notas.html', {'materia': dados_escolhidos, 'notas': materia_escolhida})     
        
        if(request.method == 'POST'):
            if 'editar_notas' in request.POST:
                return render(request, 'pages/disciplinas/editar_nota.html')
    else:
        return HttpResponseRedirect('/')
    
def editar_nota(request):
    if request.user.is_authenticated and request.user.is_active:
        if(request.method == 'GET'):
            materia_id = request.POST.get('editar_nota')
            materia = Materia.objects.filter(id = materia_id).first()
            return render(request, 'pages/disciplinas/editar_nota.html', {'materia': materia})     
        
        if(request.method == 'POST'):
            if "att" in request.POST:
                nota=request.post.get("att")
                materia.notas=nota
                materia.save()
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
