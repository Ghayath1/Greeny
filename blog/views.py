from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView
from .models import Post, Category , Comment
from taggit.models import Tag
from django.views.generic.edit import FormMixin
from django.urls import reverse
from .forms import CommentForm
# Create your views here.

class PostList( ListView):
    model = Post
    extra_context = {
        'category_list' : Category.objects.all() , 
        'tags_list' : Tag.objects.all()
    }


class PostDetail(FormMixin,DetailView):
    model = Post
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        post = self.get_object()
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(post=post) 
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user 
            myform.post = post 
            myform.save() 
            return redirect(reverse('blog:post_detail' , kwargs={'pk': post.id}))