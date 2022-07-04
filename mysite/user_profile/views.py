from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        is_error = False
        if not username or get_user_model().objects.filter(username=username).exists():
            messages.error(request, 'Vartotojo vardas neįvestas, arba toks vartotojas jau egzistuoja.')
            is_error = True
        if not email or get_user_model().objects.filter(email=email).exists():
            messages.error(request, 'El.pašto adresas neįvestas, arba vartotojas su įvestu el.pašto adresu jau egzistuoja.')
            is_error = True
        if not password or not password2 or password != password2:
            messages.error(request, 'Slaptažodžiai nesutampa arba neįvesti.')
            is_error = True
        if is_error:
            return redirect('register')
        else:
            get_user_model().objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Vartotojas {} sukurtas sėkmingai'.format(username))
            return redirect('login')
    else:
        return render(request, 'user_profile/register.html')
