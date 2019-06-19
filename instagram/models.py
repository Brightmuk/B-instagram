from django.db import models


class Profile(models.Model):
    bio = models.CharField(max_length =200)
    profile_pic_path = models.ImageField(upload_to = 'photos/', default='DEFAULT VALUE')

    

class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/', default='DEFAULT VALUE')
    profile = models.ForeignKey(Profile)
    image_name = models.CharField(max_length =30)
    comments = models.CharField(max_length =200,blank =True)
    caption = models.CharField(max_length =50)
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
     
    def __str__(self):
        return self.image_name