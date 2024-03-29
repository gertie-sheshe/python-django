from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticlesView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_page'),
    path('articles/new', views.ArticleCreateView.as_view(), name='new_article'),
    path('article/<int:pk>/edit', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('article/<int:pk>/delete', views.ArticleDeleteView.as_view(), name='article_delete'),
]
