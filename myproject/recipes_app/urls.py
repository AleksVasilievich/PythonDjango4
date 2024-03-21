from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views, logout


urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/add/', views.add_edit_recipe, name='add_edit_recipe'),
    path('recipes/add/<int:recipe_id>/', views.add_edit_recipe, name='add_edit_recipe'),
    path('accounts/registration/', views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='recipes_app/login.html'), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    # path('accounts/profile/', views.add_edit_recipe, name='add_edit_recipe'),
    path('accounts/profile/', views.home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)