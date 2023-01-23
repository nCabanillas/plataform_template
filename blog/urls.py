from django.urls import path
from . import views

urlpatterns = [
    #For admin views
    path('', views.home, name='home'),
    #including app Blog
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store')
]