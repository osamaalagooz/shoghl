
from django.urls import path
from .views import contact_us, send_message

urlpatterns = [
    path('', contact_us, name = "conector"),
    path('send', send_message, name = "sender"),
]    

app_name = 'contact'