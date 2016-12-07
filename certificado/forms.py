from django.forms import ModelForm

from certificado.models import Participante

class ParticipanteForm(ModelForm):
	class Meta:
		
		model = Participante
		fields = ['nome','num_inscricao','cpf']  
