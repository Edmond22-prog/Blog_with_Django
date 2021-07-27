from .models import Post
from django.shortcuts import render
# Importation des vues générique de Django : ListView et DetailView
from django.views.generic import ListView, DetailView

# Create your views here.
""" def home (request):
    return render(request, 'home.html', {}) """

# Définition d'une classe HomeView qui permettra d'organiser les différents composants d'une page
# en ListView, c'est à dire en liste descendante
class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
