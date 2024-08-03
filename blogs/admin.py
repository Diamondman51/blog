from django.contrib import admin
<<<<<<< HEAD

from blogs.models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', "title", 'is_featured', "status", "author", "category", "created_at", "updated_at")
    ordering = ("id",)
    search_fields = ("id", 'title', 'status', 'author', 'category', 'is_featured', 'created_at')
    sortable_by = ('id', 'status', 'is_featured', "category", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ("title", "is_featured", "status", "author")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    ordering =  ["name"]
    search_fields = ("id", "name", "created_at", "updated_at")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
=======
from .models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['id', 'title', 'is_featured']

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
>>>>>>> f0cc347699b1c2398f36bf1b520b8bda7fbe31ae
