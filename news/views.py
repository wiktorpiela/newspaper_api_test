from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

#all articles list and creating new one
@api_view(["GET", "POST"])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#get single article details, delete or update them
@api_view(["GET", "PUT", "DELETE"])
def article_details(request, pk):
    article = Article.objects.get(pk=pk)
    
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "PUT":
        serializer = ArticleSerializer(instance = article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    else:
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

