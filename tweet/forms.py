from django import forms
from .models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'image']
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class SearchForm(forms.Form):
    query = forms.CharField(label='search', max_length=10)