from django import forms
from .models import Category, Post

""" Definition statique de la liste de categories """
#categories = [('Coding', 'Coding'), ('Sport', 'Sport'), ('Entertainment', 'Entertainment'),]

""" Definition dynamique de la liste de categories """
categories = Category.objects.all().values_list('name', 'name')
categories_list = []
for item in categories:
    categories_list.append(item)

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=categories_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
