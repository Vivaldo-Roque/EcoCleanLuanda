from django.urls import path
from usuarios import views

urlpatterns = [
    path('', views.home, name='inicio'),
    path('inicio/', views.home, name='inicio'),
    path('sobre/', views.about, name='sobre'),
    path('entrar/', views.signIn, name='entrar'),
    path('registar/', views.signUp, name='registar'),
    path('vender/', views.sell, name='vender'),
    path('comprar/', views.buy, name='comprar'),
    path('sair/', views.my_logout, name='sair'),
    path('eliminar_conta/', views.delete_account, name='eliminar_conta'),
    path('perfil/', views.profile, name='perfil'),
]