from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# app_name = "news"

urlpatterns = [
    path("article-list/", views.articles, name="articles"),
    path("article-details/<int:pk>/", views.ArticleDetails.as_view(), name="articleDetails"),
    path("users-list/", views.UserView.as_view(), name="users"),
    path("", views.APIRoot.as_view(), name="links"),
]

urlpatterns = format_suffix_patterns(urlpatterns)