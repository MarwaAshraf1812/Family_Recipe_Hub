from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from django.contrib.auth.models import User


# def home(request):
#     return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print("form = ", form)
        if form.is_valid():
            form.save()
            user_obj = User.objects.all().get(username=form.cleaned_data['username'])
            CustomUser.objects.create(user=user_obj, email=form.cleaned_data['email'])
            return redirect('accounts:login')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        print("form = ", request.POST.get('password'))
        username = request.POST.get('username')
        password = request.POST.get('password')
        # objects = User.objects.all().filter(username=username)
        # print("objects = ", objects)
        if "@" in username:
            try:
                user_object = User.objects.get(email=username)
                username = user_object.username
            except User.DoesNotExist:
                user = None
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('accounts:login')