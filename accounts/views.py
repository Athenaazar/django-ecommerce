from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

from .forms import UserLoginForm


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
    return render(request, 'accounts/register.html')


def user_logout(request):
    logout(request)
    return redirect('company:home')
