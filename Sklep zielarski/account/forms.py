from django import forms
from .models import UserBase
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Nazwa uzytkownika', 'id': 'login-user'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Hasło',
            'id': 'login-pwd',

        }
    ))


class RegistrationForm(forms.ModelForm):

    user_name = forms.CharField(
        label='Wpisz nazwe użytkownika', min_length=4, max_length=50, help_text='Wymagany'
    )
    email = forms.EmailField(
        max_length=100, help_text='Wymagane',
        error_messages={'required': 'Przepraszamy, będziesz potrzebować e-maila '}
    )
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = UserBase.objects.filter(user_name=user_name)
        if r.count():
            raise forms.ValidationError('Nazwa użytkowanika już istnieje')
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasła nie pasują do siebie')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError('użyj innego adresu e-mail, który jest już zajęty')
        return email


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Nazwa użytkownika'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Hasło'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Powtórz hasło'})




