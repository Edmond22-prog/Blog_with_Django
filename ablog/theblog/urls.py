from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    # Lorsque l'on cree un nouveau Poste, il a une cle primaire lorsqu'il est enregistre dans
    # dans la base de donnees, c'est cette cle primaire qu'on recupere ici avec "pk"
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
]