from .models import Article
from django.contrib.auth.models import User
from .serializers import ArticleSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404

#all articles list and creating new one       
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

#get single article details, delete or update them
class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

#display all users and create new one
class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
