from django import forms
from django.core.exceptions import ValidationError
from .validators import *
from .models import Course


class CourseForm(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': "Kurs nomini kiriting",
        'class': 'form-control'
    }), label='Kurs nomi', validators=[course_validator])

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': "Kurs haqida ma'lumot kiriting",
        'class': 'form-control'
    }), label='Kurs haqida', required=False)

    photo = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control'
    }), label='Rasmi', required=False)

    def create(self):
        course = Course.objects.create(**self.cleaned_data)
        return course

    def update(self, course):
        course.title = self.cleaned_data.get('title')
        course.description = self.cleaned_data.get('description')
        course.photo = self.cleaned_data.get('photo') if self.cleaned_data.get('photo') else course.photo
        course.save()


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'id': 'form3Example1cg',
        'class': 'form-control form-control-lg'
    }), validators=[check_nbsp, user_availability_check])
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'id': 'form3Example3cg',
        'class': 'form-control form-control-lg'
    }))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'id': 'form3Example4cg',
        'class': 'form-control form-control-lg'
    }))
    password_confirm = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={
        'id': 'form3Example4cdg',
        'class': 'form-control form-control-lg'
    }))

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password_confirm != password:
            raise ValidationError("Parollar bir xil bo'lishi kerak!")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'id': 'typeEmailX-2',
        'class': 'form-control form-control-lg'
    }), validators=[check_nbsp, login_validator])

    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'id': 'typePasswordX-2',
        'class': 'form-control form-control-lg'
    }))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                password_check_by_username(username, password)
            except ValidationError as e:
                self.add_error('password', e.message)
