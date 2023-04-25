from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('redirect/', views.redirect_uni, name='redirect_uni'),
    path('success/', views.success, name='success'),
]