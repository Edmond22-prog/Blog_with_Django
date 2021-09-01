from django.urls import path
from .views import PasswordsChangeView, UserEditView, UserRegisterView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit-profile"),
    # Lien pour la modification de mot de passe, du formulaire de modification de profil
    # Le parametre de <as_view()> est la forme que va prendre la page ou le lien nous amene
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')), 
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    # Lien pour apres modification du mot de passe
    path('password_success', views.password_success, name="password-success")
]