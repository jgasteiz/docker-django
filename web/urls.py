from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'about/', views.about, name='about'),
]
