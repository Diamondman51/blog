from django.urls import path

from .views import *


urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("categories/", categories, name="categories"),
    path('categories/add/', add_category, name="add_category"),
    path("categories/delete/<int:pk>", delete_category, name="delete_category"),
    path("categories/edit/<int:pk>", edit_category, name="edit_category"),
    path('blogs/', dashboard_blogs, name="dashboard_blogs"),
    path('blogs/add/', add_blog, name="add_blog"),
    path("blogs/delete/<int:pk>", delete_blog, name="delete_blog"),
    path("blogs/edit/<int:pk>", edit_blog, name="edit_blog"),
    path('users/', users, name="users"),
    path("users/add/", add_user, name='add_user'),
    path("users/delete/<int:pk>", delete_user, name="delete_user"),
    path("users/edit/<int:pk>", edit_user, name="edit_user"),    
]
