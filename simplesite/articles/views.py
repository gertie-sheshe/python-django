from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Article

# Create your views here.
class ArticlesView(ListView):
    model = Article
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'data_object'
