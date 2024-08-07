from blogs.models import Blog, Category
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


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
        

# class EditUserForm(UserChangeForm):
    # class Meta:
    #     model = User
    #     fields = ('username', 'first_name', 'last_name', 'email')

class EditUserForm(UserChangeForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}), 
        label="New Password", 
        required=False
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm New Password'}), 
        label="Confirm New Password", 
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optionally set labels for better form display
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        # If you don't want to require a password on update:
        self.fields['password'].required = False 
        self.fields['password2'].required = False

    # def clean_username(self):
        # ... (username uniqueness validation - same as before) ... 

    def clean(self):
        """Verify both passwords match."""
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords do not match.")

    def save(self, commit=True):
        user = super().save(commit=False) 
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
        return user