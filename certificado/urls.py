from django.conf.urls import url

from certificado import views

urlpatterns = [
    url(r'^$', views.home, name='certificado.home'),
    url(r'resultado$', views.resultado, name='certificado.resultado'),
    url(r'participante/create$', views.participante_create, name='certificado.participante_create'),
    
]