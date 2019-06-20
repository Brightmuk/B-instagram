from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.shortcuts import render,redirect
from .models import Image,Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm
from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()
    users = User.objects.all()
    return render(request, 'index.html',{"images":images,'users':users})

@login_required(login_url='/accounts/login/')
def profile(request,id):
    user = User.objects.get(id=id)
    # try:
    #     profile = Profile.objects.get(user_id=id)
    # except ObjectDoesNotExist:
    #     return redirect(update_profile)            
    
    return render(request,'profile/profile.html',{'user':user,'profile':profile})

def update_profile(request,id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect(home)
    else:
            form = UpdateProfileForm()
    return render(request,'profile/update_profile.html',{'user':user,'form':form})