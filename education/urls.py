from django.urls import path
from .views import (home, add_course, course_detail, student_detail, students_by_course, delete_course, update_course,
                    user_logout, user_login, user_register, error_404, add_student, delete_student, update_student)

urlpatterns = [
    path('', home, name='home'),

    # course actions
    path('course/add/', add_course, name='add_course'),
    path('course/<int:course_id>/delete/', delete_course, name='delete_course'),
    path('course/<int:course_id>/update/', update_course, name='update_course'),

    # student actions
    path('student/add/', add_student, name='add_student'),
    path('student/<int:student_id>/delete/', delete_student, name='delete_student'),
    path('student/<int:student_id>/update/', update_student, name='update_student'),

    path('course/<int:course_id>/', course_detail, name='course_detail'),
    path('student/<int:student_id>/', student_detail, name='student_detail'),
    path('students/<int:course_id>/', students_by_course, name='students_by_course'),

    #auth
    path('auth/register/', user_register, name='user_register'),
    path('auth/login/', user_login, name='user_login'),
    path('auth/logout/', user_logout, name='user_logout'),

    #404
    path('404/notfound/', error_404, name='404'),

]
