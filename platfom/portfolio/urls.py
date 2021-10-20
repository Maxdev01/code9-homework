from django.urls import path

from . import views


urlpatterns = [
    path('', views.indexpage, name="first"),
    path('dashboard', views.dashboard, name="dash"),
    path('profile-user/<int:id>/', views.detail_profil, name="detail-profil"),
    path('project-user/<int:id>/', views.detail_project, name="detail-project"),
    path('ajoutertonprofil', views.newProfile, name="newprofils"),
    path("newprojectuser", views.newProjects, name="newprojects"),
    path("viewbyuser", views.viewByUser, name="byuser"),
    #path("infoindex", views.InfosPage, name="info"),
    path("deleteproject/<int:id>/", views.deleteProj, name="del"),
  
]


