from django.urls import include, path
from PlatformReciclagem.views import views

urlpatterns = [
    path('vendas-dashboard/', views.dashboard, name='vendas-dashboard')
]