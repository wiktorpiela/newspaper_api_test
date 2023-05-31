from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path("article-list/", views.ArticleList.as_view()),
    path("article-details/<int:pk>/", views.ArticleDetails.as_view()),
]