from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class CustomUser(AbstractUser):

    username = None
    phone_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)
    user_profile_image = models.ImageField(upload_to='profile')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()

# //////////////////////////////////////////////////////////////////////////////////////////////
#   singnals in django 
#   There are four types of singnal 
#   1:pre_save ,  2:post_save , 3:pre_delete , 4:post_delete  

from django.db.models.signals import post_save , post_delete, pre_delete , pre_save
from django.dispatch import receiver

class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

    def __str__(self) ->str:
        return self.car_name        
    
@receiver(post_save, sender = Car)
def call_car_api(sender, instance, **kwargs):
    print('Car object created')
    print(sender, instance, kwargs)
