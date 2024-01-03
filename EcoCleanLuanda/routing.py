from django.urls import path
from .consumers import ContainerDetailsConsumer

websocket_urlpatterns = [
    path('ws/contentor/<uuid:contentor_uuid>/', ContainerDetailsConsumer.as_asgi()),
]