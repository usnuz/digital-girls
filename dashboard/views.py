from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from main.models import *
from datetime import date


@login_required(login_url='login-url')
def index(request):
    today_registration = Registration.objects.filter(date_created__date=date.today())
    all_registration = Registration.objects.all()
    checked = Registration.objects.filter(is_checked=True)
    not_checked = Registration.objects.filter(is_checked=False)
    context = {
        'today': {
            'registration': today_registration
        },
        'all': {
            'registration': all_registration,
            'checked': checked,
            'not_checked': not_checked,
        }
    }
    return render(request, 'dashboard.html', context)
