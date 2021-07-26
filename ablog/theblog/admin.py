from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)   # Action pour que le Poste soit accéssible sur la page d'administration
