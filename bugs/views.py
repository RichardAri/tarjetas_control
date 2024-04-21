from django.shortcuts import redirect, render
from .forms import BugReportForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required
def report_bug(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST, request.FILES)
        if form.is_valid():
            bug_report = form.save(commit=False)
            
            # Asignar el usuario actual al bug_report, si está autenticado
            if request.user.is_authenticated:
                bug_report.user = request.user
            
            bug_report.save()

            # Configurar el correo electrónico
            subject = f"{bug_report.tipo} - Nuevo Reporte por {request.user.username}"
            message = f"Reportado por: {request.user.username}\nDescripción: {bug_report.description}"
            
            email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, ['jpingenieriagpt@gmail.com'])

            # Adjuntar la imagen si existe
            if bug_report.image:
                email.attach(bug_report.image.name, bug_report.image.read())

            # Enviar el correo
            email.send()

            return redirect('home')
    else:
        form = BugReportForm()

    return render(request, 'report_bug.html', {'form': form})


