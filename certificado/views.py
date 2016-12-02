from django.shortcuts import render
from django.http import HttpResponse
from certificado.models import Certificado, Evento, Participante, User
from django.contrib.auth import authenticate, login

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

def auth(request):
	error = False
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username,password=password)
		if user == None:
			error = True
		else:
			error = False
			login(request, user)

	context = {
		'error' : error
	}

	return render(request,'certificado/auth.html', context)
