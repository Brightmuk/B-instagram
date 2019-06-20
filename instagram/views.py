from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Image,Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()
    users = User.objects.all()
    return render(request, 'index.html',{"images":images,'users':users})

def profile(request,id):
    user = User.objects.filter(id=id)

    return render(request,'profile/profile.html',{'user':user})
