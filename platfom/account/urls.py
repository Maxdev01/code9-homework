from django.urls import path

from . import views


urlpatterns = [
    path('incription', views.inscription, name="inscription"),
    path('connexion', views.connexion, name="connexion"),
    path('deconnection', views.deconnecter, name="logout")
]


