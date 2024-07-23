from django.contrib import admin
from .models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['id', 'title']

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
