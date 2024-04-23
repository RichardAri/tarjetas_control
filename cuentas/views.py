from django.shortcuts import render, redirect
from cuentas.models import UserProfile
from .forms import UserRegistrationForm  # Asegúrate de haber creado este formulario
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse

# !es registro por eso no usa @login_required
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Guarda el nuevo objeto User creado por el formulario
            user = form.save()

            # Crea un UserProfile con la información adicional
            UserProfile.objects.create(
                user=user,
                rol=form.cleaned_data['rol'],
                empresa=form.cleaned_data['empresa']
            )

            # Inicia sesión automáticamente al usuario después de registrarse
            login(request, user)

            # Redirige a la página principal después del registro exitoso
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# !no puede tener @login_required porque es el envio de login 
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)      
            if user is not None:
                login(request, user)
                return redirect('ver_tarjetas_diarias')  # Redirige a la página principal después del login exitoso
            else:
                return HttpResponse("Credenciales inválidas.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})