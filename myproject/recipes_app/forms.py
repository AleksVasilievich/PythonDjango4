from django import forms
from .models import Recipe

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RecipeForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'large-text-input'}))
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'large-textarea'}))
    preparation_steps = forms.CharField(label='Шаги приготовления',
                                        widget=forms.Textarea(attrs={'class': 'large-textarea'}))
    preparation_time = forms.IntegerField(label='Время приготовления')
    image = forms.ImageField(label='Изображение')
    categories = forms.CharField(label='Категории')

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'preparation_steps', 'preparation_time', 'image', 'categories']
        widgets = {
            'image': forms.FileInput(attrs={'accept': 'image/*'})
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Обязательное поле')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']