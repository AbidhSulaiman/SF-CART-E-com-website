from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control'  # Optional: to add CSS classes for styling
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control'  # Optional: to add CSS classes for styling
    }))