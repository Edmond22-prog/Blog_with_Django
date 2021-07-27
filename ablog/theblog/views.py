from .models import Post
from django.shortcuts import render
# Importation des vues générique de Django : ListView et DetailView
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import EditForm, PostForm

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


class AddPostView(CreateView):
    model = Post   # Lorsque l'on choisit PostForm, on a plus besoin de fields car il le gere deja
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'  # Ici, on importe toutes les proprietes du model qu'on utilise
    # On pouvait aussi choisir celle que l'on veut utiliser en faisant ce qui suit :
    # fields = ('propriete1', 'propriete2', ...)


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'body']