from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class FeedbackForm(forms.Form):
    category_list = (
        ('Комнатное растение', 'Комнатное растение'),
        ('Уличное растение', 'Уличное растение'),
        ('Букет', 'Букет'),
    )

    user = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'user-name',
        'id': 'user-name',
        'placeholder': 'Имя'
    }), required=False)

    mail = forms.EmailField(widget=forms.EmailInput(attrs={
        'name': 'user-email',
        'id': 'user-email',
        'placeholder': 'Email'
    }), required=True)

    category = forms.ChoiceField(widget=forms.Select(attrs={
        'name': 'user-category',
        'id': 'user-category',
    }), choices=category_list, required=False)

    feedback_text = forms.CharField(widget=forms.Textarea(attrs={
        'name': 'user-text',
        'id': 'user-text',
        'placeholder': 'Введите ваш текст',
        'rows': 6,
        'style': 'resize: none'
    }), required=True)


class RecognitionForm(forms.Form):
    image = forms.ImageField(label='')
