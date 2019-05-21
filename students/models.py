from django.db import models

class Student(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
