from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.sections, name='index'),
    url(r'sections$', views.sections, name='courses'),
]
