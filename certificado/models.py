from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Evento(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name

class Participante(models.Model):
	user = models.OneToOneField(User, unique=True)
	num_inscricao = models.CharField(max_length=30)
	cpf = models.CharField(max_length=50)

class Curso(models.Model):
	participante = models.ForeignKey(User)
	evento = models.ForeignKey(Evento)
	name = models.CharField(max_length=255)
	carga_horaria = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name
