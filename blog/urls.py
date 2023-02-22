from django.urls import path 
from .views import PostList , PostDetail
from rest_framework.routers import DefaultRouter
from .api import PostDetailAPI,PostListAPI , PostAPI



app_name = 'blog'



urlpatterns = [
    path('' , PostList.as_view() , name='post_list'),
    path('<int:pk>' , PostDetail.as_view() , name='post_detail'), 
    path('api/' , PostListAPI.as_view()),
    path('api/<int:pk>' , PostDetailAPI.as_view()),
]