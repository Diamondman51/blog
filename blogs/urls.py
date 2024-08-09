from django.urls import path

from blogs.views import *


urlpatterns = [
    path('', blogs, name="blogs"),
    path("blog/<slug:blog_slug>", blog, name='blog'),
    path('category/<int:category_id>', posts_by_category, name="posts_by_category"),
    path('search/', search, name="search"),
]
