from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404

#all articles list and creating new one       
class ArticleList(APIView):

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#get single article details, delete or update them
class ArticleDetails(APIView):

    def get_object(self, pk, format=None):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Http404
        
    def get(self, request, pk ,format=None):
        my_article = self.get_object(pk)
        serializer = ArticleSerializer(my_article)
        return JsonResponse(serializer.data, safe=True)
    
    def put(self, request, pk ,format=None):
        my_article = self.get_object(pk)
        serializer = ArticleSerializer(instance=my_article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk ,format=None):
        my_article = self.get_object(pk)
        my_article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



