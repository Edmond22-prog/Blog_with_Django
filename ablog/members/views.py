from .forms import EditProfileForm, SignUpForm
from typing import Generic
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    # Cette fonction remplit toutes les entrees du formulaire avec les informations de 
    # l'utilisateur actuel a modifier
    def get_object(self):
        return self.request.user