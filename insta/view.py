from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import ProfileForm, profileEdit, ImageUpload, CommentForm
from django.contrib import messages
from .models import Image, Comments
from django.core.exceptions import ObjectDoesNotExist
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
            photo.image_owner = current_user
            photo.save()
            return redirect('index')
    else:
        form = ImageUpload()
    return render(request, 'post.html', {"form": form})


@login_required(login_url='/accounts/register')
def like(request):
    '''
    The view starts by looking for a GET variable called id. If it finds one, it retrieves the
    Image object that is associated with this id.
    Next, the view checks to see whether the user has voted for this bookmark before.
    This is done by calling the filter method.
    If this is the first time that the user has liked for this bookmark, we increment the
    post.likes
    '''
    if request.GET['id']:
        try:
            id = request.GET['id']
            post = Image.objects.get(id=id)
            user_liked = post.users_liked.filter(
                username=request.user.username)
            if not user_liked:
                post.image_likes += 1
                post.users_liked.add(request.user)
                post.save()

            elif user_liked and post.image_likes != 0:
                post.image_likes -= 1
                post.users_liked.remove(request.user)
                post.save()
        except ObjectDoesNotExist:
            raise Http404('Post not found.')

    if request.META['HTTP_REFERER']:
        return HttpResponseRedirect(request.META['HTTP_REFERER'], {"user_liked": user_liked})

    return HttpResponseRedirect('/')

@login_required(login_url='/accounts/login/')
def comment(request, id):
    current_user = request.user
    image = Image.objects.get(pk=id)
    commenty = Comments.objects.all()
    print(current_user.profile.avatar)

    print(image)  
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.writer = current_user
            comment.post = image
            comment.save()
            return redirect('index')
    else:
        form = CommentForm()

    return render(request, 'comment.html', {'form':form, 'image':image, 'commenty':commenty })
