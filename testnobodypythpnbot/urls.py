from django.urls import path
from .views import handle_bot_request
from .credentials import BOT_URL_SECRET

urlpatterns = [
    path(f"{BOT_URL_SECRET}/", handle_bot_request),
    # path('poll/', poll_updates)
]
