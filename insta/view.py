from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def profile(request, question_id):
    user_name = request.user.username
    print(user_name)
    return render(request, 'profile.html')