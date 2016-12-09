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

@login_required
def home_admin(request):
	site = "ForumRD"
	context = {
		'site': site,
	}

	return render(request,'certificado/home_admin.html', context)


def resultado(request):

	numero = request.GET.get('numero')
	certificado = Certificado.objects.filter(numero=numero)
	valido = True

	if not certificado:
		valido = False

	context = {
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
        	return redirect('certificado.home_admin')
        else:
            error = True
            


    context = {
    	'error':error,
    }
    return render(request, 'accounts/auth.html', context)

@login_required
def logout_view(request):
	logout(request)
	return redirect('certificado.home')

# Início do CRUD / Participante
@login_required
def participante_list(request):
	list = Participante.objects.all()
	context = {
		'list': list,
	}
	return render(request, 'certificado/participante_list.html', context)

@login_required
def participante_create(request):
	if request.method == 'POST':
		form = ParticipanteForm(request.POST)
		if form.is_valid():
			participante = Participante()
			participante.nome = form.cleaned_data['nome']
			participante.num_inscricao = form.cleaned_data['num_inscricao']
			participante.cpf = form.cleaned_data['cpf']
			participante.save()
			return redirect("participante/list")
	else:
		form = ParticipanteForm()

	form = ParticipanteForm()

	return render(request, 'certificado/participante_create.html', {'form': form})

@login_required
def perticipante_delete(request,participante_id):
	participante = Participante.objects.get(pk=participante_id)
	participante.delete()

	return redirect("participante/list")
