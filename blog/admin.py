from re import search
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post , Category , Comment , Author
# Register your models here.

class PostAdmin(admin.ModelAdmin):
     summernote_fields = '__all__'
     list_display = ['title','author','category']
     list_filter = ['category','author']
     search_fields = ['title','content']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','post','comment','created_at']


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Category)
admin.site.register(Author)