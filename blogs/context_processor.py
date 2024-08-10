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
    telegram = links.get(name='Telegram')
    context = {
        'about': about,
        'links': links,
        'telegram': telegram
        }
    return context
