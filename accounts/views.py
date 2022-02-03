from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .models import User

from .forms import UserLoginForm, UserRegistrationForm


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                return redirect('company:home')
            else:
                messages.error(request, 'username or password is wrong !', 'danger')
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            check = User.objects.filter(email__iexact=cd['email']).exists()
            if check:
                messages.error(request, 'please take another email !', 'danger')
            else:
                user = User.objects.create_user(full_name=cd['full_name'], email=cd['email'], password=cd['password1'])
                user.save()
                login(request, user)
                messages.success(request, 'you registered and login successfully', 'success')
                return redirect('company:home')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('company:home')


def profile(request):
    return render(request, 'accounts/profile.html')
