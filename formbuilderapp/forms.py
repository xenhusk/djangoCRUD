from django import forms

class PersonForm(forms.Form):
    first_name = forms.CharField(
        label = 'First Name',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter First Name'
        })
        )
    last_name = forms.CharField(
        label = 'Last Name',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Last Name'
        })
        )
    email = forms.EmailField(
        label = 'Email Address',
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Email Address'
        })
        )
    age = forms.IntegerField(
        label = 'Age',
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Age'
        })
        )
