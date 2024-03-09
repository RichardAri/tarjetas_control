from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # Actualiza el campo 'rol' para usar ChoiceField
    rol = forms.ChoiceField(choices=UserProfile.ROLES, required=True, label="Rol")
    empresa = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'rol', 'empresa']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div('username', 'email', css_class='form-group'),
            Div('password1', 'password2', css_class='form-group'),
            Div('rol', 'empresa', css_class='form-group'),
            Submit('submit', 'Registrar', css_class='btn btn-primary mt-3')
        )
