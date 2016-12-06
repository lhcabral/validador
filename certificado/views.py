from django.shortcuts import render, redirect
from django.http import HttpResponse
from certificado.models import Certificado, Evento, Participante, User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def home(request):
	site = "ForumRD"
	certificado = Certificado.objects.all()
	context = {
		'site': site,
		'certificado': certificado
	}

	return render(request,'certificado/home.html', context)

def resultado(request):
	site = "ForumRD"
	
	numero = request.GET.get('numero')
	certificado_all = Certificado.objects.all()
	certificado = Certificado.objects.filter(numero=numero)

	if certificado == None:
		error = True
		context = {
			'site': site,
			'error': error,
			'certificado': certificado,
		}
		return render(request,'certificado/home.html', context)
	error = False
	context = {
		'site': site,
		'certificado': certificado,
		'numero': numero,
		'error': error,
	}
	return render(request,'certificado/resultado.html', context)


	# context = {
	# 	'site': site,
	# 	'certificado': certificado,
	# }

	# return render(request,'certificado/home.html',context)

def auth(request):
    error = False

    if request.method == 'POST':
        # username = 'luiz'
        username = request.POST.get("username")
        # password = '123456ba'
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
        	login(request, user)
        	return redirect('certificado.home')
        else:
            error = True
            


    context = {
    	'error':error,
    }
    return render(request, 'account/auth.html', context)


