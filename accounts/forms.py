from django import forms
from .models import User, Profile
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'full_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError('passwords must match')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'full_name')

    def clean_password(self):
        return self.initial['password']


class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=30,
                                widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.EmailField(max_length=50,
                             widget=forms.EmailInput(attrs={'placeholder': 'your email'}))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={'placeholder': 'enter your password'}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={'placeholder': 'enter your confirm password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError(
                'this email already exists ! plz enter enother one')
        return email

    def clean(self):
        clean_data = super().clean()
        p1 = clean_data.get('password1')
        p2 = clean_data.get('password2')
        if p1 and p2:
            if p1 != p2:
                raise forms.ValidationError('password must match')


class EditProfileForm(forms.ModelForm):
    full_name = forms.CharField(max_length=30,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'full name'}))
    email = forms.EmailField(max_length=50,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your email'}))

    class Meta:
        model = Profile
        fields = ('bio', 'age', 'phone', 'street', 'city', 'state', 'zip_code')
        widgets = {
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
        }
