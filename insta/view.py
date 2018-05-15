from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import ProfileForm, profileEdit, ImageUpload
from django.contrib import messages
from .models import Image

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    posts = Image.objects.all()
    return render(request,'index.html',{'posts':posts})

@login_required(login_url='/accounts/login/')
def profile(request, user_id):
    posts = Image.objects.all()
    return render(request, 'profile.html', {'posts': posts})


@login_required(login_url='/accounts/login/')
# @transaction.atomic
# def profile_edit(request, user_id):

# #     # return HttpResponse('ll %s' %user_id)
# #     # user = User.objects.get(pk=user_id)
# #     # user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...wesley nom'
# #     # user.save()
# #     if request.method == 'POST':
# #         profile_form = ProfileForm(instance=request.user.profile)
# #         if profile_form.is_valid():
# #             profile_form.save()
# #             return redirect('/')
# #     else:
# #         profile_form = ProfileForm(instance=request.user.profile)
# #     return render(request, 'edit-profile.html', {'profile_form':  profile_form})
#     if request.method == 'POST':
#         profile_form = ProfileForm(
#             request.POST, request.FILES, instance=request.user.profile)
#         if profile_form.is_valid():
#             profile_form.save()
#             return redirect('home')
#     else:
       
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'edit-profile.html', {"profile_form": profile_form})
@transaction.atomic
def profile_edit(request, user_id):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            # messages.success(request, _(
            #     'Your profile was successfully updated!'))
            return redirect('profile', user_id)
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit-profile.html', {"profile_form": profile_form})

@login_required(login_url='/accounts/login/')
def post(request): 
    current_user = request.user
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = current_user
            photo.save()
            return redirect('index')
    else:
        form = ImageUpload()
    return render(request, 'post.html', {"form": form})
