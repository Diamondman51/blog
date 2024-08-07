from blog.forms import RegistrationForm
from blogs.models import Blog, Category
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.shortcuts import redirect, render

from settingsapp.models import About, Social_links


# Create your views here.
# @login_required(login_url='login')
def blogs(request):
    blog = Blog.objects.filter(status=1)
    featured = blog.filter(is_featured=True)
    context = {
        'blogs': blog,
        'featured': featured,
    }

    return render(request, 'blogs.html', context)


# @login_required(login_url='login')
def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    category = blog.category
    paragraph = blog.body.split("\n")
    context = {
        'blog': blog,
        "paragraph": paragraph,
        'categor': category,
    }
    return render(request, "blog.html", context)


# @login_required(login_url='login')
def posts_by_category(request, category_id):
    data = Blog.objects.filter(category=category_id)
    single_cat = Category.objects.get(id=category_id)
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
            print(request.errors)
            return redirect('login')
    else:
        form = AuthenticationForm()
        context = {
            'form': form
        }

        return render(request, "login.html", context)


def logout(request):
    auth.logout(request)
    return redirect("blogs")