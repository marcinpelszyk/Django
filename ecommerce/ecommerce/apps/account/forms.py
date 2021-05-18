from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)

from .models import Address, Customer


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["full_name", "phone", "address_line", "address_line2", "town_city", "postcode"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["full_name"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Imię i Nazwisko"}
        )
        self.fields["phone"].widget.attrs.update({"class": "form-control mb-2 account-form", "placeholder": "Telefon"})
        self.fields["address_line"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "adres"}
        )
        self.fields["address_line2"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "adres"}
        )
        self.fields["town_city"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Miasto"}
        )
        self.fields["postcode"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "kod pocztow"}
        )



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
        error_messages={'required': 'Przepraszamy, będziesz potrzebować e-maila'}
    )
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ('user_name', 'email',)

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        r = Customer.objects.filter(user_name=user_name)
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
        if Customer.objects.filter(email=email).exists():
            raise forms.ValidationError('Użyj innego adresu e-mail')
        return email


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': '', 'placeholder': 'Nazwa użytkownika'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Hasło'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Powtórz hasło'})

class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='Adres e-mail konta (nie można go zmienić)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'E-mail', 'id': 'form-email', 'readonly': 'readonly'}))
    user_name = forms.CharField(
        label='Nazwa użytkownika', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Nazwa użytkownika', 'id': 'form-firstname',
                   'readonly': 'readonly'}))
    first_name = forms.CharField(
        label='Imię', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'imię', 'id': 'form-lastname'}))

    class Meta:
        model = Customer
        fields = ('email', 'user_name', 'first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['email'].required = True


class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=255, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'E-mail', 'id': 'form-email'}
    ))
    def clean_email(self):
        email = self.cleaned_data['email']
        u = Customer.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                'Niestety nie możemy znaleźć tego adresu e-mail'
            )
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='Nowe hasło', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Nowe hasło', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Potwórz hasło', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Nowe hasło', 'id': 'form-new-pass2'}))