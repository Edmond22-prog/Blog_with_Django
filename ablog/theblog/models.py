from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    
    def get_absolute_url(self):
        return reverse("home")

class Post (models.Model):
    # Définition du titre d'un Poste (dans le blog) du côté de l'administration
    title = models.CharField(max_length=255)
    header_image = models.ImageField(blank=True, null=True, upload_to="images/")
    # Choix de l'auteur du Poste du côté de l'administration
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Espace de texte pour la description du Poste du coté de l'administration
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    # Date de publication du Poste
    post_date = models.DateField(auto_now_add=True)
    # Categorie de la publication du coté de l'administration
    category = models.CharField(max_length=255, default='coding')
    snippet = models.CharField(max_length=255)
    # Determination des likeurs du poste du coté de l'administration
    likes = models.ManyToManyField(User, related_name='blog_posts')


    def total_likes(self):
        return self.likes.count()


    # Fonction qui affiche on peux dire l'entête du Poste du coté administrateur
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    
    # Fonction qui definit ou est redirigé un Poste, n'étant pas du coté administrateur
    def get_absolute_url(self):
        #return reverse("article-detail", args=(str(self.id)))
        return reverse("home")
    

""" Après chaque action ici, il faut migrer, c-a-d 'python manage.py migrate' avant de lancer le serveur,
pour sauvegarder dans la base de données. """   