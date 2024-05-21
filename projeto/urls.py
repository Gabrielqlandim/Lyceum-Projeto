from django.urls import path
from django.contrib import admin
from app import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name = 'home'),
    path('alunos/', views.alunos, name = 'alunos'),
    path('disciplinas/', views.disciplinas, name ='disciplinas'),
    path('calendario_academico/', views.calendario_academico, name = 'calendario_academico'),
    path('perfil/', views.perfil, name = 'perfil'),
    path('cadastro/', views.cadastro_prof, name = 'cadastro'),
    path('cadastrar_alunos/', views.cadastrar_alunos, name = 'cadastrar_alunos'),
    path('atualizar_alunos/', views.atualizar_alunos, name = 'atualizar_alunos'),
    path('editar_alunos/', views.editar_alunos, name= 'editar_alunos'),
    path('admin/', admin.site.urls),

    #disciplinas
    path('portugues/', views.portugues, name = 'portugues'),
    path('matematica/', views.matematica, name = 'matematica'),
    path('historia/', views.historia, name = 'historia'),
    path('geografia/', views.geografia, name = 'geografia'),
    path('ciencias/', views.ciencias, name = 'ciencias'),
    path('ingles/', views.ingles, name = 'ingles'),
    path('notas/', views.notas, name = 'notas'),
    path('faltas/', views.faltas, name = 'faltas'),
]
