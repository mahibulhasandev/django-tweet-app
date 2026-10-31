from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Tweet Form
class TweetForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ['text', 'photo']

        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control rounded-3',
                'placeholder': 'What is happening?',
                'rows': 4,
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control rounded-3',
            }),
        }


# User Registration Form
class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control rounded-3 py-2',
            'placeholder': 'Enter your email',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():

            if field_name == 'email':
                continue

            field.widget.attrs.update({
                'class': 'form-control rounded-3 py-2',
                'placeholder': field.label,
            })
