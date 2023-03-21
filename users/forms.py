from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'user-name',
        'id': 'user-name',
        'placeholder': 'Логин'
    }), max_length=65, required=True)

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'name': 'user-pass',
        'id': 'user-pass',
        'placeholder': 'Пароль'
    }), max_length=65, required=True)
