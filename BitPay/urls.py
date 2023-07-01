from django.urls import path
from .views import bit_pay_main_hook
from .BitPaySettings import API_URL_SECRET

urlpatterns = [
    path(f"{API_URL_SECRET}", bit_pay_main_hook),
]
