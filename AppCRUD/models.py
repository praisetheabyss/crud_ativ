import email
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Autor (models.Model):
    nome = models.CharField(max_length=200)
    biografia = models.TextField()
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.nome

class Linguagem (models.Model):
    nome = models.CharField(max_length=30, default= 'Linguagem')

    def __str__(self):
        return self.nome

class Edicao (models.Model):
    numero = models.IntegerField(primary_key= True,
     default=1,
        validators=[
            MaxValueValidator(11),
            MinValueValidator(1)
        ])
    editorial = models.TextField()
    data = models.DateField()

    def __str__(self):
        return str(self.numero)

class Artigo (models.Model):
    autor_id = models.ForeignKey(Autor, on_delete= models.CASCADE)
    linguagem = models.ForeignKey(Linguagem, on_delete= models.CASCADE)
    eicao = models.ForeignKey(Edicao, on_delete= models.CASCADE)
    titulo = models.CharField(max_length= 200)
    introducao = models.TextField()

    def __str__(self):
        return self.titulo
