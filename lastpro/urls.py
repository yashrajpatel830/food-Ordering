"""
URL configuration for lastpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lastpro import views
from vege.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',views.main),
    path('',receipe),
    path('register_page/',register_page),
    path('delete_receipe/<id>',delete_receipe),
    path('update_receipe/<id>',update_receipe),
    path('login_page/',login_page),
    path('logout_page/',logout_page),
   
    path('get_astudent/',get_astudent),
    path('see_marks/<student_id>',see_maks , name='see_marks'),

    path('email/',email),
    path('home/',home),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()    