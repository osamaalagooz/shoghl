from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail 
from django.conf import settings
import json
#from django.contrib.auth.models.
# Create your views here.
def contact_us(request):
    info = Info.objects.first()
    return render(request,'contact.html',{'info':info})
    
def send_message(request):
        print(request.body)
        if request.body:
            data = json.loads(request.body.decode("utf-8"))
            subject = data.get('subject')
            email = data.get('email')
            message = data.get('message')
            print(message)
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
            )
            return JsonResponse({
            "response": "sending message success"
            })
        else:
            return JsonResponse({
            "response": "sending message fail"
            })