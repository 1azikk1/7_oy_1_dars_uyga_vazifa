from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Course


# for username
def user_availability_check(value):
    if User.objects.filter(username=value).exists():
        raise ValidationError("Ushbu foydalanuvchi nomi bilan ro'yhatdan o'tilgan!")


def login_validator(value):
    if not User.objects.filter(username=value).exists():
        raise ValidationError("Bunday foydalanuvchi mavjud emas!")


# password check for login page
def password_check_by_username(username, password):
    user = User.objects.get(username=username)
    if not check_password(password, user.password):
        raise ValidationError("Noto'g'ri parol kiritildi!")


def check_nbsp(value):
    if ' ' in value:
        raise ValidationError("Foydalanuvchi nomi bo'sh joylarsiz yozilishi kerak!")


# course name unique check
def course_validator(value):
    if Course.objects.filter(title=value).exists():
        raise ValidationError("Bunday kurs mavjud!")
