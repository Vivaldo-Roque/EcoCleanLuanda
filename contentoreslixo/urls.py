from django.urls import include, path
from rest_framework import routers
from contentoreslixo import views

router = routers.DefaultRouter()
router.register(r'api/v1/contentores', views.ContentorLixoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls))
]