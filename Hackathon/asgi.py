import os

from channels.auth import AuthMiddlewareStack #추가
from channels.routing import ProtocolTypeRouter, URLRouter #URLRouter 추가
from django.core.asgi import get_asgi_application
import chat.routing # chat import

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hackathon.settings")

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack( # 추가
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})