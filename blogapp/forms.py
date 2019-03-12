from django import forms
from .models import Blog

class BlogPost(forms.Form): #모델에서 형식을 가져오려면 ModelForm으로 바꿔주기
    #class Meta:
     #   model = Blog
      #  fields = ['title', 'body']
    email = forms.EmailField()
    files = forms.FileField()
    url = forms.URLField()
    words = forms.CharField(max_length=200)
    max_number = forms.ChoiceField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three')])