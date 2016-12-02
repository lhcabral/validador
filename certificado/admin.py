from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


from certificado.models import Evento, Participante, Curso, Certificado, UserProfile

class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False

class UserAdmin(UserAdmin):
	inlines = (UserProfileInline,)


class CertificadoAdmin(admin.ModelAdmin):
	list_display = ('participante','curso','evento','descricao','link_certificado')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Evento)
admin.site.register(Participante)
admin.site.register(Curso)
admin.site.register(Certificado,CertificadoAdmin)