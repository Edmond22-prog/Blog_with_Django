from django.http.response import HttpResponseRedirect
from .models import Category, Post
from django.shortcuts import get_object_or_404, render
# Importation des vues générique de Django
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import EditForm, PostForm
from django.urls import reverse_lazy, reverse

# Create your views here.
""" def home (request):
    return render(request, 'home.html', {}) """


def LikeView(request, pk):
    # Recuperation du poste dont on a fait un clique sur le bouton <Like>
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    # Sauvegarde du like de l'utilisateur sur ce poste
    post.likes.add(request.user)
    # Retour sur la page sans chargement
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


# Définition d'une classe HomeView qui permettra d'organiser les différents composants d'une page
# en ListView, c'est à dire en liste descendante
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']  # Permet d'ordonner les Postes, ici c'est du plus recent au plus ancien
    #ordering = ['-post_date']

    """ Cette fonction permet de recuperer toutes les categories et de les afficher (dropdown) dans la
    vue choisit (ici HomeView) """
    def get_context_data(self, *args, **kwargs):
        # Recuperation de toutes les categories
        cat_menu = Category.objects.all()
        # Aucune idee du reste
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context        


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})


# Fonction qui recupere une requete et le nom d'une categorie, pour renvoyer une page contenant tous
# les postes de cette categorie
def CategoryView(request, cats):
    # Ici c'est une requete de recuperation des postes dont la categorie est <cats>
    # Le resultat de la requete est stocke dans la variable <category_posts>
    # La methode <.replace()> remplace le deuxieme argument par le premier
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    # Le nom de la categorie <cats> et la liste des postes de cette categorie <category_posts> est envoye
    # a la page <categories.html>
    # La methode <.title()> rend la premiere lettre d'un mot en majuscule
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    """ Cette fonction permet de recuperer toutes les categories et de les afficher (dropdown) dans la
    vue choisit (ici ArticleDetailView) """
    def get_context_data(self, *args, **kwargs):
        # Recuperation de toutes les categories
        cat_menu = Category.objects.all()
        # Aucune idee du reste
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        # Ouverture du poste dont l'id est le suivant <pk> et stockage de ce poste dans la variable
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        # Recuperation de tous les likes de ce poste
        total_likes = stuff.total_likes()
        # Attribution du nombre de likes total au context, afin qu'il soit accessible dans les templates
        context["total_likes"] = total_likes
        return context 


class AddPostView(CreateView):
    model = Post   
    # Lorsque l'on choisit PostForm, on a plus besoin de fields car il le gere deja
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'  # Ici, on importe toutes les proprietes du model qu'on utilise
    # On pouvait aussi choisir celle que l'on veut utiliser en faisant ce qui suit :
    # fields = ('propriete1', 'propriete2', ...)


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'  # Ici, on importe toutes les proprietes du model qu'on utilise


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')  #Lorsque le Poste est supprimé, ca renvoi automatiquement au home