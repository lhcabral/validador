from django.conf.urls import url

from certificado import views

urlpatterns = [
    url(r'^$', views.home, name='certificado.home'),
    url(r'admin$', views.home_admin, name='certificado.home_admin'),
    url(r'resultado$', views.resultado, name='certificado.resultado'),
    url(r'participante/create$', views.participante_create, name='certificado.participante_create'),
    url(r'participante/list$', views.participante_list, name='certificado.participante_list'),
    url(r'participante/delete/(?P<participante_id>\d+)', views.participante_delete, name='certificado.participante_delete'),
    
]