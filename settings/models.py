from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=25)
    call_us = models.CharField(max_length=20)
    email_us = models.EmailField()
    logo = models.ImageField(upload_to='company/')
    subtitle = models.TextField(max_length=500)
    email = models.TextField(max_length=50)
    mobile_numbers = models.TextField(max_length=50)
    address = models.TextField(max_length=50)
    app_description = models.TextField(max_length=200, null=True , blank=True)
    app_play_store = models.URLField(null=True , blank=True)
    app_app_store = models.URLField(null=True , blank=True)

    fb_link = models.URLField(null=True , blank=True)
    tw_link = models.URLField(null=True , blank=True)
    insta_link = models.URLField(null=True , blank=True)


      
    def __str__(self):
        return self.name