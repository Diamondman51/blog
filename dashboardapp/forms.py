from blogs.models import Blog, Category
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User, Permission, Group


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


class AddUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'groups', 'user_permissions')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email
    def __init__(self, *args, **kwargs):
        super(AddUserForm, self).__init__(*args, **kwargs)
        self.fields['user_permissions'].queryset = Permission.objects.filter(
            codename__in=['add_blog', 'view_blog', 'change_blog', 'delete_blog', 'add_category', 'view_category', 'change_category', 'delete_category']
        )


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
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False 
    )
    user_permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.filter(codename__in=['add_blog', 'view_blog', 'change_blog', 'delete_blog', 'add_category', 'view_category', 'change_category', 'delete_category']),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name", 'is_active', 'is_staff', 'groups', 'user_permissions')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # super(EditUserForm, self).__init__(*args, **kwargs)

        # Comment
        # self.fields['user_permissions'].queryset = Permission.objects.filter(
        #     codename__in=['add_blog', 'view_blog', 'change_blog', 'delete_blog', 'add_category', 'view_category', 'change_category', 'delete_category']
        # )

        # Optionally set labels for better form display
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        # If you don't want to require a password on update:
        self.fields['password'].required = False 
        self.fields['password2'].required = False

    def clean(self):
        """Verify both passwords match."""
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        print('4444444444444444444444444444444444444444444444444444444444444444444444444')
        print(cleaned_data)

        if self.cleaned_data['password2']:
            if password != password2:
                raise forms.ValidationError("Passwords do not match.")
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_id = self.instance.id
        if User.objects.filter(email=email).exclude(id=user_id).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False) 
        if self.cleaned_data['password'] and self.cleaned_data['password2']:
            user.set_password(self.cleaned_data['password2'])  # Hash the password
        if commit:
            user.save()
            user.groups.set(self.cleaned_data['groups'])
            user.user_permissions.set(self.cleaned_data['user_permissions'])
        return user
    