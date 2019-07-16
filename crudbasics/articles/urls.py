from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticlesView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_page'),
    path('articles/new', views.ArticleCreateView.as_view(), name='new_article')
]
