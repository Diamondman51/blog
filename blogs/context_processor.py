from blogs.models import Category


def header(req):
    category = Category.objects.all()
    context = {
        'categories': category
    }

    return context