from blogs.models import Category


def categories(req):
    categories = Category.objects.all()
    return {'categories': categories}
