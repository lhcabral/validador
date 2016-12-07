from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from certificado.models import Certificado, Evento, Participante, User
from certificado.forms import ParticipanteForm


def home(request):
	site = "ForumRD"
	context = {
		'site': site,
	}

	return render(request,'certificado/home.html', context)

def resultado(request):
	site = "ForumRD"

	numero = request.GET.get('numero')
	certificado = Certificado.objects.filter(numero=numero)
	valido = True

	if not certificado:
		valido = False

	context = {
		'site': site,
		'valido': valido,
		'certificado': certificado,
	}

	return render(request,'certificado/home.html', context)


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

def logout_view(request):
	logout(request)
	return redirect('certificado.home')

def participante_create(request):
	form = ParticipanteForm()

	return render(request, 'certificado/participante_create.html', {'form': form})


