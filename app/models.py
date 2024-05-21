from django.db import models

class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120, null=False)
    serie_turma = models.CharField(max_length=8, null=False)
    data_matricula = models.DateField()

class Aviso(models.Model):
    mensagem = models.TextField()
    data_aviso = models.DateField()

class Materia(models.Model):
    nome_materia = models.CharField(max_length=120, null=False)
    faltas = models.IntegerField(default=0)
    notas = models.DecimalField(max_digits=5, decimal_places=2)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    