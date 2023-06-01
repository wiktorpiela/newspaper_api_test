from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "news"

urlpatterns = [
    path("article-list/", views.ArticleList.as_view()),
    path("article-details/<int:pk>/", views.ArticleDetails.as_view()),
    path("users-list/", views.UserView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)