from .models import Article
from django.contrib.auth.models import User
from .serializers import ArticleSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status, mixins, generics, filters
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.permissions import AllowAny, IsAdminUser
from .permission import IsOwnerReadOnly
from rest_framework.reverse import reverse
from .paginators import ArticlePaginator

#all articles list and creating new one       
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticlePaginator
    filter_backends = [filters.OrderingFilter]
    ordering = ["-date"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


#get single article details, delete or update them
class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerReadOnly]


#display all users and create new one
class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        return [IsAdminUser() if self.request.method == "GET" else AllowAny()]
    
class APIRoot(APIView):
    def get(self, request, format=None):
        links = {
            "articles": reverse("articles", request=request, format=format),
            "users": reverse("users", request=request, format=format)
        }
        return Response(links)
