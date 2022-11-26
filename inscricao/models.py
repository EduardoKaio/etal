from django.db import models


LISTA_SEXO= [
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
]

class MiniCurso(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nome

# Create your models here.
class Participante(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=20)
    email = models.EmailField()
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=50)
    sexo = models.CharField(max_length=15,choices=LISTA_SEXO, default="Feminino")
    minicursos = models.ManyToManyField(MiniCurso)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome
