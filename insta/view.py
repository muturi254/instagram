from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import profileEdit
# from django.http import HttpResponse

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def profile(request, user_id):
    user_name = request.user.username
    print(user_name)
    return render(request, 'profile.html')

@login_required(login_url='/accounts/login/')
def profile_edit(request, user_id):
    form = profileEdit()
    return render(request, 'edit-profile.html', {'form': form})