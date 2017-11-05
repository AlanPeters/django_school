from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.professors, name='index'),
    url(r'professors$', views.professors, name='professors'),
]
