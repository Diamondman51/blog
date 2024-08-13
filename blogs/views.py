from audioop import reverse
import random

from django.http import HttpResponseRedirect
from blog.forms import RegistrationForm
from blogs.models import Blog, Category, Comment
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render



# Create your views here.
# @login_required(login_url='login')
def blogs(request):
    blog = Blog.objects.filter(status=1)
    featured = blog.filter(is_featured=True)
    random_blog = random.choice(featured)
    context = {
        'blogs': blog,
        'featured': featured,
        'random_blog': random_blog,
    }

    return render(request, 'blogs.html', context)


# @login_required(login_url='login')
def blog(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    if request.method == "GET":
        comment = Comment.objects.filter(blog=blog)
        count = comment.count()
        category = blog.category
        paragraph = blog.body.split("\n")
        context = {
            'blog': blog,
            "paragraph": paragraph,
            'category': category,
            'comments': comment,
            'count': count,
        }
        return render(request, "blog.html", context)
    elif request.method == "POST":
        if request.POST.get("comment").strip():
            comment = Comment()
            comment.user = request.user
            comment.blog = blog
            comment.text = request.POST.get("comment")
            comment.save()
            return HttpResponseRedirect('#comment-text')
        else:
            return HttpResponseRedirect(request.path_info)
        

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "") + "#comment-text")


# @login_required(login_url='login')
def posts_by_category(request, category_id):
    data = Blog.objects.filter(category=category_id)
    single_cat = get_object_or_404(Category, id=category_id)
    context = {
        'categor': data,
        "single": single_cat,
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


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            context = {
                'form': form
            }
            return render(request, "register.html", context)
    else:
        form = RegistrationForm()
        context = {
            'form': form
        }
        return render(request, "register.html", context)
    

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('blogs')
        else:
            print('*****************************************************************************************************')
            print(form.errors)
            context = {
                'form': form
            }
            return render(request, 'login.html', context)
    else:
        # pathth = request.path_info
        form = AuthenticationForm()
        context = {
            'form': form
        }

        return render(request, "login.html", context)


def logout(request):
    auth.logout(request)
    return redirect("blogs")