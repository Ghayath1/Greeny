from django.contrib import admin
from .models import Profile , UserAddress , UserPhoneNumbers
# Register your models here.




admin.site.register(Profile)
admin.site.register(UserPhoneNumbers)
admin.site.register(UserAddress)