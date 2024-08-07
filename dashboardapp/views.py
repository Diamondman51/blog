from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from blog.forms import RegistrationForm
from blogs.models import Blog
from dashboardapp.forms import *
from django.utils.text import slugify


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    blog_count = Blog.objects.all().count()
    context = {
        "blog_count": blog_count,
    }
    return render(request, "dashboard.html", context)


@login_required(login_url='login')
def categories(request):

    return render(request, "categories.html")


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect('categories')
    elif request.method == "GET":
        form = CategoryForm()
        context = {
            'form': form
        }
        return render(request, 'add_category.html', context)


def delete_category(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    cat.delete()
    return redirect("categories")


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'GET':
        form = CategoryForm(instance=category)
        context = {
            'form': form,
            'cat': category
        }
        return render(request, "edit_category.html", context)
    elif request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("categories")


@login_required(login_url='login')
def dashboard_blogs(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs,
    }
    return render(request, "dashboard_blogs.html", context)


def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            # form.save()
            blog.author = request.user
            blog.save()
            blog.slug = slugify(blog.title + ' ' + str(blog.id))
            blog.save()
            blog.slug += slugify(blog.slug + ' ' + '22')
            blog.save() 
            return redirect('dashboard_blogs')
        else:
            print(form.errors)
            return HttpResponse('Not found')
    elif request.method == "GET":
        form = BlogForm()
        context = {
            'form': form
        }
        return render(request, 'add_blog.html', context)


def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect("dashboard_blogs")
 
def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('dashboard_blogs')
        else:
            print(form.errors)
            return redirect("dashboard_blogs")

    elif request.method == "GET":
        form = BlogForm(instance=blog)
        context = {
            'form': form,
            'blog': blog
        }
        return render(request, "edit_blog.html", context)
    

def users(request):
    users = User.objects.exclude(username='admin')
    context = {
        'users': users,
    }
    return render(request, 'users.html', context)


def add_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    elif request.method == 'GET':
        form = RegistrationForm()
        context = {
            'form': form,
        }
        return render(request, "add_user.html", context)


def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect("users")


def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == "POST":
        form = RegistrationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        else:
            print("------------------------------------------------------")
            return redirect("edit_user")
    elif request.method == "GET":
        form = RegistrationForm(instance=user)
        context = {
            'form': form,
            'user': user,
        }
        return render(request, 'edit_user.html', context)
