from django.urls import include, path
from rest_framework import routers
from contentoreslixo import views

router = routers.DefaultRouter()
router.register(r'api/v1/contentores', views.ContentorLixoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contentores/', views.containers, name='contentores'),
    path('adicionarcontentor/', views.add_container, name='adicionarcontentor'),
    path('editarcontentor/', views.edit_container, name='editarcontentor'),
    path('contentordetalhes/', views.containerdetails, name='contentordetalhes'),
    path('deletarcontentor/', views.delete_container, name='deletarcontentor'),
    path('devicestatus/', views.check_if_device_is_online, name='devicestatus'),
    path('chartdata/<uuid:id>', views.chart_data, name='chartdata')
]