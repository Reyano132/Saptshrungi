from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from task.consumers import NotificationConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("notifications/", NotificationConsumer),
    ])
})
