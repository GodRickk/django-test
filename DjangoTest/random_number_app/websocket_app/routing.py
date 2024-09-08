from django.urls import re_path
from .consumers import RandomNumberConsumer

websocket_urlpatterns = [
    re_path(r'ws/random_number/$', RandomNumberConsumer.as_asgi()),
]