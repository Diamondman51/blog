from blogs.models import Category
from settingsapp.models import About, Social_links


def header(req):
    category = Category.objects.all()
    context = {
        'categories': category
    }

    return context


def get_about(request):
    about = About.objects.all()
    links = Social_links.objects.all()
    context = {
        'about': about,
        'links': links
        }
    return context
