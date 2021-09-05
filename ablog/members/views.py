from theblog.models import Profile
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.detail import DetailView
from .forms import EditProfileForm, PasswordChangingForm, SignUpForm
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse_lazy


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = [
        'bio', 
        'profile_pic', 
        'website_url', 
        'facebook_url', 
        'twitter_url', 
        'instagram_url', 
        'pinterest_url'
    ]
    success_url = reverse_lazy('home')


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # Recuperation de tous les users
        # users = Profile.objects.all()
        # ??????
        context = super(ShowProfilePageView , self).get_context_data(*args, **kwargs)
        # Recuperation d'un user particulier
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        # Attribution au context
        context["page_user"] = page_user
        return context   


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


class PasswordsChangeView(PasswordChangeView):
    #form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    #success_url = reverse_lazy('home')
    success_url = reverse_lazy('password-success')


def password_success(request):
    return render(request, 'registration/password_success.html', {})