from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, Category
from .forms import RecipeForm
import random
from django.contrib.auth import logout
from .forms import SignUpForm
from django.core.files.uploadedfile import InMemoryUploadedFile


def home(request):
    recipes = Recipe.objects.all()
    random_recipes = random.sample(list(recipes), min(len(recipes), 5))
    context = {'recipes': random_recipes}
    return render(request, 'recipes_app/home.html', context)


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {'recipe': recipe}
    return render(request, 'recipes_app/recipe.html', context)


@login_required
def add_edit_recipe(request, recipe_id=None):
    if recipe_id:
        recipe = Recipe.objects.get(id=recipe_id)
    else:
        recipe = None

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user

            # Обработка загруженного изображения
            if 'image' in request.FILES:
                image_file = request.FILES['image']
                if isinstance(image_file, InMemoryUploadedFile):
                    recipe.image.save(image_file.name, image_file, save=True)

            # Получаем или создаем объект Category для каждой категории из формы
            category_names = form.cleaned_data.get('categories').split(',')
            for category_name in category_names:
                category, created = Category.objects.get_or_create(name=category_name.strip())
                recipe.categories.add(category)

            recipe.save()
            return redirect('add_edit_recipe', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipes_app/add_edit_recipe.html', {'form': form, 'recipe': recipe})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перенаправляем пользователя на главную страницу
    else:
        form = SignUpForm()
    return render(request, 'recipes_app/registration.html', {'form': form})


def logout_view(request):
    logout(request)
    # Перенаправляем пользователя на главную страницу или на страницу входа
    return redirect('home')
