from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path("article-list/", views.article_list),
    path("article-details/<int:pk>/", views.article_details),
]