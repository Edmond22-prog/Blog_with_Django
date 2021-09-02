from django.contrib import admin
from .models import Post, Category, Profile

# Register your models here.
admin.site.register(Post)   # Action pour que le Poste soit accéssible sur la page d'administration
admin.site.register(Category)   # Same
admin.site.register(Profile)    # Same