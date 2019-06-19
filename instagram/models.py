from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    bio = models.CharField(max_length =200)
    profile_pic_path = models.ImageField(upload_to = 'photos/', default='DEFAULT VALUE')
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True,default=1)
    followers = models.ManyToManyField('Profile',related_name="profile_followers",blank=True)
    following = models.ManyToManyField('Profile',related_name="profile_following",blank=True)

class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/', default='DEFAULT VALUE')
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE,related_name="user_name")
    profile = models.ForeignKey(Profile)
    image_name = models.CharField(max_length =30)
    caption = models.CharField(max_length =50)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
     
    def __str__(self):
        return self.image_name

class Comment(models.Model):
    image = models.ForeignKey('Image', null=True)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now=True)