from django.db import models


class Diretor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Genero(models.Model):
    descricao = models.CharField(max_length=60)

    def __str__(self):
        return self.descricao


class Filme(models.Model):
    nome = models.CharField(max_length=100)
    sinopse = models.CharField(max_length=100)
    anoLancamento = models.CharField(max_length=4)
    diretor = models.ForeignKey(Diretor, on_delete=models.SET_NULL, null=True)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome
