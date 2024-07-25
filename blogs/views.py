from django.shortcuts import render

from blogs.models import Blog, Category

# Create your views here.

def posts_by_category(req, category_id):
    posts = Blog.objects.filter(category=category_id)
    categories = Category.objects.get(pk=category_id)

    context = {
        'posts': posts,
        'category':  categories
    }

    return render(req, 'posts_by_category2.html', context)