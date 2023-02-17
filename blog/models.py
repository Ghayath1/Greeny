from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='authors/')
    bio = models.TextField(max_length=2000)
    email = models.EmailField()
    tw_link = models.URLField(null=True,blank=True)
    fb_link = models.URLField(null=True,blank=True)
    yt_link = models.URLField(null=True,blank=True)
    in_link = models.URLField(null=True,blank=True)
 
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE , related_name='post_author')
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='posts/')
    content = models.TextField(max_length=10000)
    tags =  TaggableManager()
    created_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE , related_name='post_category')

    def __str__(self):
        return self.title  

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_author')
    post = models.ForeignKey(Post , on_delete=models.CASCADE,related_name='post_comment')
    comment = models.TextField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)