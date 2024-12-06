from django.shortcuts import render, redirect
from .utils import send_email_to_client ,send_email_with_attachment
from django.conf import settings
from accounts.models import Car
from django.http import HttpResponse
# Create your views here.

def email(request):
    # send_email_to_client()
    subject = "This email is from django server with atteacment"
    message = "hy please find this attach file with is email"
    recipient_list = ["sendhavyashraj587@gmail.com"]
    file_path = f"{settings.BASE_DIR}/MAIN.XXXX"
    send_email_with_attachment(subject, message, recipient_list, file_path)
    return redirect('/email/')


import random
def home(request):
    Car.objects.create(car_name=f"nexon = {random.randint(0 , 100)}")    
    return render(request,'home.html')