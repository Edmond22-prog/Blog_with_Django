from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    # Lorsque l'on cree un nouveau Poste, il a une cle primaire lorsqu'il est enregistre dans
    # la base de donnees, c'est cette cle primaire qu'on recupere ici avec "pk"
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add-post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="edit-post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete-post"),
    path('add_category/', AddCategoryView.as_view(), name="add-category"),
]