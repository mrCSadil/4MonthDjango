from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from posts.models import Post
from user.forms import RegisterForm, LoginForm
from user.models import Profile
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/register.html', {"form": form})
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if not form.is_valid():
            print("Form is not valid", form.errors)
            return render(request, 'user/register.html', {"form": form})
        elif form.is_valid():
            form.cleaned_data.__dalitem__("password_confirm")
            image = form.cleaned_data["image"]
            age = form.cleaned_data["age"]
            user = User.objects.create_user(
                **form.cleaned_data
            )
            Profile.objects.create(
                user=user,
                image = image,
                age = age,
            )
            return redirect('main_view')

def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', {"form": form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/login.html', {"form": form})
        elif form.is_valid():
            user = authenticate(**form.cleaned_data)
            if not user:
                form.add_error(None, "Invalid username or password")
                return render(request, 'user/login.html', {"form": form})
            elif user:
                login(request, user)
                return redirect('main_view')

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('main_view')

@login_required(login_url='/login/')
def profile_view(request):
    if request.method == 'GET':
        user = request.user
        posts = Post.objects.filter(author=user).order_by('-created_at')
        profile = Profile.objects.get(user=user)
        print(request.user)
        print(profile)
        return render(request, 'user/profile.html',  context ={ "user": user, "posts": posts})