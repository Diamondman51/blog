from django.shortcuts import render

from blogs.models import Blog, Category


def home(req):
    post = Blog.objects.filter(is_featured=True, status=1)
    blogs = Blog.objects.filter(is_featured=False, status=1)
    category = Category.objects.all()
    print(post)
    context = {
        'categories': category,
        'posts': post,
        'blogs': blogs
    }
    return render(req, 'blogs.html', context)

