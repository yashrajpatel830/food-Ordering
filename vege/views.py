from django.shortcuts import render, redirect
# Create your views here.
from vege.models import Receipe
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
User = get_user_model()

@login_required(login_url="/login_page/")
def receipe(request):

    if request.method == 'POST':
        receipe_name = request.POST.get('receipe_name')
        receipe_dec = request.POST.get('receipe_dec')
        receipe_img = request.FILES.get('receipe_img')

        data = Receipe(receipe_name=receipe_name,receipe_dec=receipe_dec,receipe_img=receipe_img)
        data.save()

        return redirect('/')

    queryset = Receipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))

    allData = {'queryset':queryset}

    return render(request,'index.html',allData)

# @login_required(login_url="/login_page/")
def delete_receipe(request,id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/')

# @login_required(login_url="/login_page/")
def update_receipe(request,id):
    queryset = Receipe.objects.get(id = id)

    if request.method == 'POST':

      receipe_name = request.POST.get('receipe_name')
      receipe_dec = request.POST.get('receipe_dec')
      receipe_img = request.FILES.get('receipe_img')       
    
      queryset.receipe_name = receipe_name
      queryset.receipe_dec = receipe_dec

      if receipe_img:
         queryset.receipe_img = receipe_img
      queryset.save()
      return redirect('/')    

    allData = {'queryset':queryset}
    return render(request,'update_receipe.html',allData)

# ////////////////////////////////////////////////////////////////////////////////////////////////////
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout

def login_page(request):
    
    if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      if not User.objects.filter(username = username).exists():
          messages.error(request,'Invalid Username')
          return redirect('/login_page/')
    
      user = authenticate(username = username , password = password)
      if user is None:
          messages.error(request,'Invalid password')
          return redirect('/login_page/')
      else:
          login(request,user)
          return redirect('/')

    return render(request,'login.html') 

def logout_page(request):
    logout(request)
    return redirect('/login_page/')

def register_page(request):
    if request.method == 'POST':
       first_name = request.POST.get('first_name')
       last_name = request.POST.get('last_name')
       username = request.POST.get('username')
       password = request.POST.get('password')

       user = User.objects.filter(username = username)
       if user.exists():
           messages.info(request,'Username already taken')
           return redirect('/register_page/')

       user = User.objects.create(
           first_name = first_name,
           last_name = last_name,
           username = username
           )
       user.set_password(password)
       user.save() 
       messages.info(request,'Account created succesfuly')
       return redirect('/register_page/')

    return render(request,'register.html') 

# //////////////////////////////////////////////////////////////////////////////////////////////
from vege.models import *
from django.core.paginator import Paginator 
from django.db.models import Q , Sum

def get_astudent(request):
    quereyset = Student.objects.all()

    

    if request.GET.get('search'):
        search = request.GET.get('search')
        quereyset = quereyset.filter(
            Q(student_name__icontains = search)|
            Q(department__department__icontains = search)|
            Q(student_id__student_id__icontains = search)|
            Q(student_email__icontains = search)
        )
   
    paginator = Paginator(quereyset ,10)
    page_number = request.GET.get('page' , 1)
    page_obj = paginator.get_page(page_number)
     
    return render(request,'student.html',{'quereyset' : page_obj})

# from .seed import generate_report_card
def see_maks(request,student_id):
      
    queryset = SubjectMaks.objects.filter(student__student_id__student_id = student_id)
    total_maks = queryset.aggregate(total_maks = Sum('marks'))
    current_rank = -1
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks','-student_age')

    i=1
    for rank in ranks:
        if student_id == rank.student_id.student_id:
            current_rank = i
            break
        i = i + 1

    return render(request,'see_maks.html',{'queryset':queryset , 'total_maks':total_maks,'current_rank':current_rank}) 

    