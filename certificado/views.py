from django.shortcuts import render, redirect
from django.http import HttpResponse
from certificado.models import Certificado, Evento, Participante, User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

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

# def auth(request):
# 	error = False
	
# 	if request.method == 'POST':
# 		username = request.POST.get("username")
# 		password = request.POST.get('password')
# 		user = authenticate(username=username, password=password)
		
# 		if user == None:
# 			error = True
# 		else:
# 			error = False
# 			login(request, user)

# 		context = {
# 			'error' : error
# 		}
# 	return render(request,'account/auth.html', context)

def auth(request):
    error = False

    if request.method == 'POST':
        # username = 
        username = 'luiz'
        password = '123456ba'
        # password = request.POST.get('password')

        user = authenticate(username='username', password=password)
        if user is not None:
        	login(request, user)
        	return redirect('certificado.home')
        else:
            error = True
            


    context = {
    	'error':error,
    }
    return render(request, 'account/auth.html', context)


