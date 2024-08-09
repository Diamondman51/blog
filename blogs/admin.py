from django.contrib import admin

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


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "blog", "text", "created_at",)
    ordering = ["id"]
    search_fields = ("id", "user", "text", "created_at")
    sortable_by= ("id", "user", "blog" , "created_at")
    list_editable= ("user", "blog", "text")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)