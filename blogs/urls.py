from django.urls import path

from blogs.views import posts_by_category


urlpatterns = [
    path('<int:category_id>/', posts_by_category, name='posts_by_category')
]