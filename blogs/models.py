from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        index_together = ''

STATUS_CHOICES = (
    (0, 'Draft')
)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, on_delete=models.SET_NULL)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.CharField(max_length=200)
    body = models.TextField(max_length=2000)
    status = models.IntegerField(choices=STATUS_CHOICES, null=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
