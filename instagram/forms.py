from django import forms
from .models import Profile,Image,Comment
from django.contrib.auth.models import User

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['followers','following','user']

class PostImage(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['owner','likes','post_date','profile']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','image','posted_on']