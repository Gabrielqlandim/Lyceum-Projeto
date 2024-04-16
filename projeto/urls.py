from django.urls import path

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
    path('avisosCalendario/', views.avisosCalendario, name = 'avisosCalendario'),
    path('avisos', views.avisos, name = 'avisos'),
]
