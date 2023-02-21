from email.policy import default
from django.db import models
from django.contrib.auth.models import User 
from utils.generate_code import generate_code
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# Users 
'''
    User : 
        username 
        email 
        first_name
        last_name
        password 

    extend user :
        - BaseUser
        - ABstractBaseUser
        - One-To-One

    signals :
        post :  init  delete  save 
        pre  :  init  delete  save 
        m2m_changes
    @decorator
'''
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/' , null=True , blank=True)
    code = models.CharField(max_length=10,default=generate_code)
    code_used = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created :
        Profile.objects.create(
            user=instance
        )

DATA_TYPE = (
    ('Home' , 'Home'),
    ('Office','Office'),
    ('Bussines','Bussines'),
    ('Academy','Academy'),
    ('Others','Others'),
)    

class UserAddress(models.Model):
    user = models.ForeignKey(User,related_name='user_address',on_delete=models.CASCADE)
    address_type = models.CharField(max_length=10 , choices=DATA_TYPE)
    country = CountryField()
    city = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    street = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=10)
    notes = models.CharField(max_length=300)


class UserPhoneNumbers(models.Model):
    user = models.ForeignKey(User,related_name='user_phone_number',on_delete=models.CASCADE)
    type = models.CharField(max_length=10 , choices=DATA_TYPE)
    phone_number = models.CharField(max_length=15)