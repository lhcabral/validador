from django.conf.urls import url

from certificado import views

urlpatterns = [
    url(r'^$', views.home),
]