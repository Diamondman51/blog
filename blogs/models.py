from cgitb import text
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'


STATUS_CHOICES = (
    (1, 'Published'),
    (0, 'Draft')
)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=False)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    is_featured = models.BooleanField(default=False)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(null=True)
    words = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Blogs"
        verbose_name = "Blog"


class Comment(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, null=False, on_delete=models.CASCADE)
    text = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.text
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        