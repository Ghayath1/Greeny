
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated


'''
    GET  :  get data
    POST :  create new data
    PUT  :  update : all fields
    PATCH:  partial update
    DELETE: delete 
'''


'''
    - views : 
         - function 
         - class :
            - generic classes [List , Detail]
            - normal classes
            - viewset [5 opertions : class]
'''


# @api_view(['GET'])
# def post_list_api(request):
#     all_posts = Post.objects.all()
#     data = PostSerializer(all_posts,many=True).data
#     return Response({'post list': data})
    
    
    
# @api_view(['GET'])    
# def post_detail_api(request,id):
#     post = Post.objects.get(id=id)
#     data = PostSerializer(post).data
#     return Response({'post detail': data})



from rest_framework import generics

class PostListAPI(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]



class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]



from rest_framework import viewsets

class PostAPI(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()