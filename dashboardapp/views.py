from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog
from dashboardapp.forms import *
from django.utils.text import slugify
from .forms import EditUserForm, AddUserForm


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
            context = {
            'form': form
            }
            print(form.errors)
            return render(request, "add_category.html", context)
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
        else:
            context = {
                'form': form,
            }
            return render(request, 'edit_category.html')


@login_required(login_url='login')
def dashboard_blogs(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs,
    }
    return render(request, "dashboard_blogs.html", context)


@login_required(login_url='login')
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
            return redirect('dashboard_blogs')
        else:
            print(form.errors)
            context = {
            'form': form
                }
            return render(request, "add_blog.html", context)
    elif request.method == "GET":
        form = BlogForm()
        context = {
            'form': form
        }
        return render(request, 'add_blog.html', context)


@login_required(login_url='login')
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect("dashboard_blogs")
 

@login_required(login_url='login')
def edit_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('dashboard_blogs')
        else:
            print(form.errors)
            context = {
            'form': form
                }
            return render(request, "edit_blog.html", context)

    elif request.method == "GET":
        form = BlogForm(instance=blog)
        context = {
            'form': form,
            'blog': blog
        }
        return render(request, "edit_blog.html", context)
    

@login_required(login_url='login')
def users(request):
    users = User.objects.exclude(username='admin')
    # group = user.groups.exclude(username="admin")
    context = {
        'users': users,
    }
    return render(request, 'users.html', context)


@login_required(login_url='login')
def add_user(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print('llllllllllllllllllllllllllllllllllllllllllllllllllllllllll')
            print(form.errors)
            context = {
                'form': form,
                }
            return render(request, 'add_user.html', context)
        
    elif request.method == 'GET':
        form = AddUserForm()
        context = {
            'form': form,
        }
        return render(request, "add_user.html", context)


@login_required(login_url='login')
@permission_required("auth.delete_user", raise_exception=True)
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect("users")


@login_required(login_url='login')
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print("------------------------------------------------------")
            print(form.errors)
            context = {
                'form': form,
                "user": user,
            }
            return render(request, "edit_user.html", context)
    elif request.method == "GET":
        form = EditUserForm(instance=user)
        context = {
            'form': form,
            'user': user,
        }
        return render(request, 'edit_user.html', context)
