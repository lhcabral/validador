from django.shortcuts import render
from django.http import HttpResponse
from certificado.models import Certificado, Evento, Participante, User

def home(request):
	site = "ForumRD"
	certificados = Certificado.objects.all()


# adiciona dados na tabela com varios campos
	# participante = Participante()
	# participante.num_inscricao = "123456"
	# participante.cpf = "030.263.234-46"
	# participante.save()



	context = {
		'site': site,
		'certificados': certificados
	}


	#Este comando adiciona dados direto na tabela do banco. Basta rodar a página
	# Evento.objects.create(name="ForumRD")

	return render(request,'certificado/home.html', context)
