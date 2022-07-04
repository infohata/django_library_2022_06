from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

@csrf_protect
def register(request):

    return render(request, 'user_profile/register.html')
