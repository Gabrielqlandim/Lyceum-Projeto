from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as lg
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Aluno, Materia, SerieTurma

#login
def login(request):
    if request.method == 'GET':
        return render(request, 'pages/login.html', {'check': 0 })
    elif request.method == 'POST':
        if 'login' in request.POST:
            name = request.POST.get('name')
            senha = request.POST.get('senha')
            
            user = authenticate(request,username=name,password=senha)

            if user:
                lg(request, user)
                return HttpResponseRedirect('/home/')
            else:
                print('oi')
                return render(request, 'pages/login.html',{'check': 1 } ) 
        elif 'ok' in request.POST:
                return render(request, 'pages/login.html',{'check':0 } )
               
def cadastro_prof(request):
    if request.method == 'GET':
        return render(request, 'pages/cadastro.html', {'check': 0, 'message':''})
    elif request.method == 'POST':
        if 'cadastrar' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            senha = request.POST.get('senha')

            username_check = User.objects.filter(username=name).first()
            user_email = User.objects.filter(email=email).first()

            if username_check or user_email:
                return render(request, 'pages/cadastro.html', {'check': 1, 'message':'Usuário já existente.'})
            else:
                user = User.objects.create_user(username=name,email=email,password=senha)
                user.save()
                return HttpResponseRedirect('/')
        elif 'ok' in request.POST:
            return render(request, 'pages/cadastro.html', {'check': 0, 'message':''})
        
### LOGADO ###
        
#home
@login_required
def home(request):
    user = request.user
    return render(request, 'pages/home.html')

# visualizar alunos // cadastrar alunos // criar turma
@login_required
def alunos(request):
    turmas = SerieTurma.objects.all()
    alunos = Aluno.objects.all()
    if request.method == 'GET':
        return render(request, 'pages/alunos.html', {'alunos': alunos, 'turmas':turmas, 'check': 0, 'turma_check': 0})
    elif request.method == 'POST':
        if 'cadastrar' in request.POST:
            return render(request, 'pages/alunos.html', {'alunos': alunos, 'turmas':turmas, 'check': 1, 'turma_check': 0})
        elif 'cadastrar_confirmar' in request.POST:
            materias = ['portugues', 'matematica', 'historia', 'geografia', 'ciencias', 'ingles']
            aluno_name = request.POST.get('nome-aluno')
            nome_turma = request.POST.get('turma-aluno')
            aluno_turma = SerieTurma.objects.filter(nome_turma=nome_turma).first()
            data_matriculado = request.POST.get('data-aluno')

            aluno = Aluno(nome=aluno_name,serie_turma=aluno_turma,data_matricula=data_matriculado)
            aluno.save()

            for materia in materias:
                mateira_nova = Materia(aluno=aluno, nome_materia=materia, faltas=0, notas=0)
                mateira_nova.save()

            return render(request, 'pages/alunos.html', {'alunos': alunos, 'turmas':turmas, 'check': 0, 'turma_check': 0})
        elif 'criar_turma' in request.POST:
            return render(request, 'pages/alunos.html', {'alunos': alunos, 'turmas':turmas, 'check': 0, 'turma_check': 1})
        elif 'criar_turma_confirmar' in request.POST:
            nome = request.POST.get('nome-turma')
            serie_turma = SerieTurma(nome_turma=nome)
            serie_turma.save()
            return render(request, 'pages/alunos.html', {'alunos': alunos, 'turmas':turmas, 'check': 0, 'turma_check': 0})
        
        elif 'apagar_turma' in request.POST:
            return render(request, 'pages/alunos.html', {'alunos': alunos, 'turmas':turmas, 'check': 0, 'turma_check': 2})
        elif 'apagar_turma_confirmar' in request.POST:
            nome = request.POST.get('turma-aluno')
            turma = SerieTurma.objects.filter(nome_turma=nome).first()
    
            first_turma = SerieTurma.objects.exclude(id=turma.id).first()
            Aluno.objects.filter(serie_turma=turma).update(serie_turma=first_turma)

            turma.delete()
            return render(request, 'pages/alunos.html', {'alunos': alunos, 'turmas':turmas, 'check': 0, 'turma_check': 0})
        elif 'cancelar' in request.POST:
            return render(request, 'pages/alunos.html', {'alunos': alunos, 'turmas':turmas, 'check': 0, 'turma_check': 0})

# editar alunos
@login_required
def editar_alunos(request):
    turmas = SerieTurma.objects.all()
    alunos = Aluno.objects.all()
    if request.method == 'GET':
        if request.user.is_authenticated and request.user.is_active:
            return render(request, 'pages/alunos/editar_alunos.html', {'alunos': alunos, 'turmas':turmas, 'check': 0, 'name': '', 'serie_turma': '', 'data_matricula': '', 'id':''})
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
            id = request.POST.get("atualizar")
            aluno = Aluno.objects.get(id_aluno=id)
            nome = aluno.nome
            serie_turma = aluno.serie_turma
            data_matricula = aluno.data_matricula
            return render(request, 'pages/alunos/editar_alunos.html', {'alunos': alunos, 'turmas':turmas, 'check': 1, 'name': nome, 'serie_turma': serie_turma, 'data_matricula': data_matricula, 'id':id})
        
        if 'atualizar_confirmar' in request.POST:
            id = request.POST.get("atualizar_confirmar")
            aluno = Aluno.objects.get(id_aluno=id)

            nome_turma = request.POST.get("turma-aluno")
            turma_selecionada = SerieTurma.objects.filter(nome_turma=nome_turma).first()

            aluno.nome = request.POST.get("nome-aluno")
            aluno.serie_turma = turma_selecionada
            aluno.data_matricula = request.POST.get("data-aluno")
            aluno.save()
            return render(request, 'pages/alunos/editar_alunos.html', {'alunos': alunos, 'turmas':turmas, 'check': 0, 'name': '', 'serie_turma': '', 'data_matricula': '', 'id':''})
        if 'atualizar_cancelar' in request.POST:
            return render(request, 'pages/alunos/editar_alunos.html', {'alunos': alunos, 'turmas':turmas, 'check': 0, 'name': '', 'serie_turma': '', 'data_matricula': '', 'id':''})

## DISCIPLINAS ##
@login_required
def disciplinas(request):
    return render(request, 'pages/disciplinas.html')
    
@login_required
def portugues(request):
    return render(request, 'pages/disciplinas/portugues.html')

@login_required
def matematica(request):
    return render(request, 'pages/disciplinas/matematica.html')

@login_required
def historia(request):
    return render(request, 'pages/disciplinas/historia.html')

@login_required
def geografia(request):
    return render(request, 'pages/disciplinas/geografia.html')

@login_required
def ciencias(request):
    return render(request, 'pages/disciplinas/ciencias.html')

@login_required
def ingles(request):
    return render(request, 'pages/disciplinas/ingles.html')


# visualizar notas
@login_required
def notas(request):
    if(request.method == 'GET'):
        materia_escolhida = request.GET.get('notas')
        materias = Materia.objects.all()
        dados_escolhidos = []
        for materia in materias:
            if(materia.nome_materia == materia_escolhida):
                dados_escolhidos.append(materia)

        return render(request, 'pages/disciplinas/notas.html', {'materia': dados_escolhidos, 'notas': materia_escolhida})     

# editar notas    
@login_required
def editar_nota(request):
    print("EDITAR NOTA")
    if(request.method == 'GET'):
        print("GET")
        materia_id = request.GET.get('editar_notas')
        materia = Materia.objects.filter(id = materia_id).first()
        teste=1.0
        nota=str(materia.notas)
        print(materia.notas)
        return render(request, 'pages/disciplinas/editar_nota.html', {'materia': materia, 'nota': nota})
    
    if(request.method == 'POST'):
        print("POST")
        if "nota-aluno" in request.POST:
            print("ATT")
            materia_id=request.POST.get("nota-aluno")
            materia = Materia.objects.filter(id = materia_id).first()
            nova_nota=request.POST.get("nova_nota")
            print(nova_nota)
            print("FIM")
            
            materia.notas=nova_nota
            materia.save()

            return HttpResponseRedirect('/notas/?notas='+materia.nome_materia)
    
# visualizar e editar faltas
@login_required
def faltas(request):
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
            if materia.faltas > 0:
                materia.faltas -= 1
                materia.save()
            return HttpResponseRedirect('/faltas/?faltas='+materia_escolhida)

#########################

@login_required
def calendario_academico(request):
    if request.method == 'GET':
        return render(request, 'pages/calendario_academico.html')

@login_required
def perfil(request):
    if request.method == 'GET':
        return render(request, 'pages/perfil.html', {'user': request.user})
    
    elif request.method == 'POST':
        user = request.user
        if 'perfil_confirmar' in request.POST:
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            
            user.username = nome
            user.email = email
            if senha:
                user.set_password(senha)
            user.save()
            
            if senha:
                user = authenticate(request, username=nome, password=senha)
                if user:
                    lg(request, user)
            
            return HttpResponseRedirect('/perfil/')

        
        elif 'perfil_cancelar' in request.POST:
            return render(request, 'pages/perfil.html')

        elif 'logout' in request.POST:
            logout(request)
            return HttpResponseRedirect('/')

