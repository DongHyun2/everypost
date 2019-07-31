from django import forms
from .models import Blog

class NewBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']
        #모든 항목을 상속받고 싶다면, fields = '__all__'