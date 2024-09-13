from django.urls import path
from . import consumers

websocket_urlpatterns = [
  path('ws/jwc/', consumers.MyJsonWebsocketConsumer.as_asgi()),
  path('ws/ajwc/', consumers.MyAsyncJsonWebsocketConsumer.as_asgi()),
]


# ws://127.0.0.1:8000/ws/jwc/
# ws://127.0.0.1:8000/ws/ajwc/