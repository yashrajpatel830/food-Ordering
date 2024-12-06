from django.shortcuts import render
from django.http import HttpResponse



def main(request):
    return HttpResponse('yashraj singh patel ismailkhadi i have pursuing my gratuation from ranaissance univarsity indore')

def home(request):
    return render(request,'index.html')

