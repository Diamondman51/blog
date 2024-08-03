from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from blogs.models import Blog, Category

# Create your views here.

def blogs(request):
    blogs = Blog.objects.filter(status=1)
    featured = blogs.filter(is_featured=True)
    context = {
        'blogs': blogs,
        'featured': featured
    }

    return render(request, 'blogs.html', context)

def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    category = blog.category
    paragraph = blog.body.split("\n")
    context = {
        'blog': blog,
        "paragraph": paragraph,
        'categor': category
    }
    return render(request, "blog.html", context)

def posts_by_category(request, category_id):
    data = Blog.objects.filter(category=category_id)
    single_cat = Category.objects.get(id=category_id)
    context = {
        'categor': data,
        "single": single_cat
    }
    return render(request, "by_category.html", context=context)

def search(request):


# Construct the regex pattern with word boundaries
    keyword = (request.GET.get("keyword", ""))
    # pattern = rf'\b{keyword}\b'
    # data = Blog.objects.filter(Q(title__iregex=pattern) & Q(short_description__iregex=pattern))
    data = Blog.objects.filter(Q(title__icontains=keyword) & Q(short_description__icontains=keyword))
    num = data.count()

    print("sssssssssssssssssssssssssssssssssssssssssssssssssssss")
    print(data)
    context = {
        'result': data,
        'num': num,
        'keyword': keyword
    }
    return render(request, "search.html", context)