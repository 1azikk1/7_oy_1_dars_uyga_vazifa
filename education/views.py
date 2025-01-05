from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Student
from .forms import CourseForm, LoginForm, RegisterForm
from django.contrib import messages


def home(request):
    students = Student.objects.all()
    context = {
        'title': "Asosiy Sahifa",
        'students': students
    }
    return render(request, 'index.html', context)


def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {
        'student': student,
        'title': f"{student.course.title}: {student.name}"
    }
    return render(request, 'student_detail.html', context)


def students_by_course(request, course_id):
    students = Student.objects.filter(course_id=course_id)
    course = Course.objects.get(pk=course_id)
    context = {
        'course': course,
        'students': students,
        "title": f"{course.title}: talabalar!"
    }
    return render(request, 'index.html', context)


def course_detail(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        context = {
            'course': course,
            'title': course.description,
        }
        return render(request, 'detail.html', context)
    except:
        return render(request, '404.html', status=404)


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            course = form.create()
            messages.success(request, "Kurs muvaffaqiyatli tarzda qo'shildi!")
            return redirect('home')
    else:
        form = CourseForm()

    context = {
        'form': form,
        'title': "Kurs qo'shish"
    }
    return render(request, 'add_course.html', context)


def update_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.update(course)
            messages.success(request, "Dars muvaffaqiyatli tarzda o'zgartirildi!")
            return redirect('course_detail', course_id=course.pk)

    form = CourseForm(initial={
        'title': course.title,
        'description': course.description,
        'photo': course.photo
    })

    context = {
        'form': form,
        'course': course,
        'photo': course.photo
    }
    return render(request, 'add_course.html', context)


def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, "Kurs muvaffaqiyatli tarzda o'chirildi!")
        return redirect('home')

    context = {
        'course': course,
        'title': f"{course.title} kursini o'chirish!"
    }
    messages.warning(request, "Ushbu kursni o'chirmoqchimisiz?")
    return render(request, 'delete_confirm.html', context)


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            password_confirm = form.cleaned_data.get('password_confirm')
            if password == password_confirm:
                user = User.objects.create_user(
                    form.cleaned_data.get('username'),
                    form.cleaned_data.get('email'),
                    password
                )
                messages.success(request, "Tabriklaymiz, muvaffaqiyatli tarzda ro'yhatdan o'tdingiz!")
                return redirect('user_login')
    else:
        form = RegisterForm()

    context = {
        'form': form,
        'title': "Ro'yhatdan o'tish"
    }
    return render(request, 'auth/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                messages.success(request, f"{username} web sahifamizga xush kelibsiz!")
                login(request, user)
                return redirect('home')
            messages.error(request, "Bunday foydalanuvchi mavjud emas!")
    else:
        form = LoginForm()
    context = {
        'form': form,
        'title': "Saytga kirish"
    }
    return render(request, 'auth/login.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, "Siz web sahifamizdan chiqib ketdingiz!")
    return redirect('user_login')