from django.shortcuts import render, redirect
from .forms import UserRegistrationForm  # Asegúrate de haber creado este formulario
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente al usuario después de registrarse
            return redirect('home')  # Redirige a la página principal después del registro exitoso
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirige a la página principal después del login exitoso
            else:
                return HttpResponse("Credenciales inválidas.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})