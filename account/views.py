from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib import messages


@login_required(login_url='login_name')
def profile(request):
    return render(request, 'account/profile.html')


@login_required(login_url='login_name')
def edit_profile(request):
    return render(request, 'account/edit-profile.html')


@login_required(login_url='login_name')
def edit_username(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    avatar = request.FILES.get('avatar')
    user = request.user
    try:
        user.username = username
        user.save()
    except Exception as err:
        messages.error(request, 'This username is busy')
        return redirect('edit-profile-url')
    user.email = email
    user.save()
    print(avatar)
    if avatar is not None:
        user.avatar = avatar
        user.save()
    messages.success(request, f'Your information has been successfully changed!')
    return redirect('edit-profile-url')


@login_required(login_url='login_name')
def edit_profile_info(request):
    firs_name = request.POST.get('first-name')
    last_name = request.POST.get('last-name')
    middle_name = request.POST.get('middle-name')
    user = request.user
    user.first_name = firs_name
    user.last_name = last_name
    user.middle_name = middle_name
    user.save()
    messages.success(request, f'Your information has been successfully changed!')
    return redirect('edit-profile-url')


@login_required(login_url='login_name')
def edit_password(request):
    old_pwd = request.POST.get('old-pwd')
    pwd = request.POST.get('pwd')
    pwd1 = request.POST.get('pwd1')
    user = request.user
    if user.check_password(old_pwd):
        if pwd == pwd1:
            user.set_password(pwd)
            user.save()
            messages.success(request, f'Your password has been successfully changed!')
        else:
            messages.error(request, f'The new passwords must be the same!')
    else:
        messages.warning(request, 'Wrong password!')
    return redirect('edit-profile-url')


@login_required(login_url='login_name')
def delete_account(request):
    pwd = request.POST.get('pwd')
    user = request.user
    if user.check_password(pwd):
        user.delete()
        return redirect('login-url')
    else:
        messages.warning(request, 'Wrong password!')
        return redirect('edit-profile-url')


def log_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    usr = authenticate(username=username, password=password)
    if usr is not None:
        login(request, usr)
        return redirect('dashboard-url')
    return render(request, 'account/login.html')


@login_required(login_url='login_name')
def log_out(request):
    logout(request)
    return redirect('login-url')


def reset_password(request):
    return render(request, 'account/reset-password.html')

