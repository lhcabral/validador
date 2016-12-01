from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Evento(models.Model):
	name = models.CharField(max_length=255)
	descricao = models.CharField(max_length=500, null=True)

	def __str__(self):
		return self.name

class Participante(models.Model):
	# user = models.OneToOneField(User, unique=True)
	nome = models.CharField(max_length=255)
	num_inscricao = models.CharField(max_length=30)
	cpf = models.CharField(max_length=50)

	def __str__(self):
		return self.nome

class Curso(models.Model):
	evento = models.ForeignKey(Evento)
	name = models.CharField(max_length=255)
	carga_horaria = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Certificado(models.Model):
	participante = models.ForeignKey(Participante)
	curso = models.ForeignKey(Curso)
	evento = models.ForeignKey(Evento)
	descricao = models.CharField(max_length=50)
	link_certificado = models.CharField(max_length=500)

	def __str__(self):
		return self.descricao


