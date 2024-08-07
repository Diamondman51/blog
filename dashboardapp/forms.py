from blogs.models import Blog, Category
from django import forms


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title',  "category", "is_featured", 
                  "featured_image", "short_description", 
                  'words', 'body', 'status')
        
