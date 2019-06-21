from django.shortcuts import render
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.shortcuts import render,redirect
from .models import Image,Profile,Like,Followers,Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm,PostImage,CommentForm
from django.core.exceptions import ObjectDoesNotExist

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all().order_by('-post_date')
    users = User.objects.all()  
    current_user = request.user
    return render(request, 'index.html',{"images":images,'users':users})

@login_required(login_url='/accounts/login/')
def profile(request,id):
    images = Image.objects.filter(owner_id=id)
    current_user = request.user
    user = User.objects.get(id=id)
    try:
        profile = Profile.objects.get(user_id=id)
    except ObjectDoesNotExist:
        return redirect(update_profile,current_user.id)            
    
    return render(request,'profile/profile.html',{'user':user,'profile':profile,'images':images,'current_user':current_user})
@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    current_user = request.user
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id=id
            profile.save()
            return redirect(home)
    else:
        form = UpdateProfileForm()
    return render(request,'profile/update_profile.html',{'user':user,'form':form})

def search_results(request):

    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = User.objects.filter(username__icontains=search_term)
        
        message = f"{search_term}"
        
        return render(request, 'searched.html',{"message":message,"users": searched_users})

    else:
        message = "Please input a name in the search form"
        return render(request, 'searched.html',{"message":message})

@login_required(login_url='/accounts/login/')
def new_image(request,id):
    current_user = request.user
    current_profile = Profile.objects.get(user_id=id)
    if request.method == 'POST':
        form = PostImage(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.owner = current_user
            image.profile = current_profile
            image.save()
        return redirect(home)
    else:
        form = PostImage()
    return render(request, 'new_image.html', {'user':current_user,"form": form})

@login_required(login_url='/accounts/login/')   
def comment(request,c_id):
    comments = Comment.objects.filter(image_id=c_id)
    current_user = request.user
    current_image = Image.get_image_by_id(c_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image = current_image
            comment.save()
            return redirect(home)
    else:
        form = CommentForm()
    
    return render(request,'comments.html',{"form":form,'comments':comments})   

