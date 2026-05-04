from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('photographers/', views.photographers, name='photographers'),
    path('decorators/', views.decorators, name='decorators'),
    path('caterers/', views.caterers, name='caterers'),
    path('packages/', views.packages, name='packages'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
]