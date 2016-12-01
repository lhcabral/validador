from django.contrib import admin

from certificado.models import Evento, Participante, Curso, Certificado


admin.site.register(Evento)
admin.site.register(Participante)
admin.site.register(Curso)
admin.site.register(Certificado)