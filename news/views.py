from .models import Article
from .serializers import ArticleSerializer
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