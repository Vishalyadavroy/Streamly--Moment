from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
      class Meta: #ye meta class hai 
            model = Tweet
            fields = ['text' , 'photo'] 