from django.contrib import admin
from .models import Profile, Image,Followers,Like

admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Followers)
admin.site.register(Like)
