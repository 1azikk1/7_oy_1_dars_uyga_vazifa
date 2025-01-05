from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='Kurs nomi', unique=True)
    description = models.TextField(blank=True, null=True, verbose_name="Kurs haqida")
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='Rasmi')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'kurs '
        verbose_name_plural = 'kurslar'


class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name='Talaba ismi')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Email manzili')
    enrolled_at = models.DateTimeField(auto_now_add=True, verbose_name='Yozilgan vaqti')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Kursi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'talaba '
        verbose_name_plural = 'Talabalar'
        permissions = [('test permission', 'test permission'),]
