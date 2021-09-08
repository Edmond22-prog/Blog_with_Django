from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(blank=True, null=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.CharField(max_length=255, blank=True, null=True)
    twitter_url = models.CharField(max_length=255, blank=True, null=True)
    instagram_url = models.CharField(max_length=255, blank=True, null=True)
    pinterest_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.user)
    

    def get_absolute_url(self):
        return reverse("home")


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
    # Determine l'auteur du Poste du côté de l'administration
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
    

class Comment(models.Model):
    # Determine le poste dont il est question
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    # Determine le nom de la personne qui a fait le commentaire
    name = models.CharField(max_length=255)
    # Texte du commentaire
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True) 


    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

""" Après chaque action ici, il faut migrer, c-a-d 'python manage.py migrate' avant de lancer le serveur,
pour sauvegarder dans la base de données. """   