from django.db import models

from django.contrib.auth.models import AbstractUser

from Site import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class User(AbstractUser):
    """
    Пользователь
    """
    GENDER_CHOICES = [('М', 'М'), ('Ж', 'Ж')]
    USER_STATUS_CHOICES = [('teacher', 'Учитель'), ('student', 'Ученик'), ('parents', 'Родители')]
    middle_name = models.CharField("Отчество", max_length=150, blank=True, null=True)
    sex = models.CharField('Пол', choices=GENDER_CHOICES, max_length=1)
    status = models.CharField('Статус пользователя', choices=USER_STATUS_CHOICES, max_length=10)
    birthday = models.DateField('Дата рождения', blank=True, null=True)
    photo = models.ImageField('Фото', upload_to='media/photos/', default='media/default-user.png', blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = ("Пользователь")
        verbose_name_plural = ("Пользователи")


class Teacher(models.Model):
    """
    Учитель
    """
    lessons = models.ManyToManyField('school.Lesson', related_name='teachers', verbose_name='Ведет предметы')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='teacher', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Учитель")
        verbose_name_plural = ("Учителя")


class Student(models.Model):
    """
    Школьник
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='student', on_delete=models.CASCADE)
    class_init = models.ForeignKey('school.SchoolClass', related_name='students', on_delete=models.CASCADE,
                                   verbose_name='Состоит в классе', null=True)

    class Meta:
        verbose_name = ("Ученик")
        verbose_name_plural = ("Ученики")


class Parents(models.Model):
    """
    Родители школьника
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='parents', on_delete=models.CASCADE)
    student_init = models.ManyToManyField('Student', related_name='student', verbose_name='Ребенок/Дети')

    class Meta:
        verbose_name = ("Родитель")
        verbose_name_plural = ("Родители")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    При сохранении в БД User, сигнал post_save запускается, и функция create_user_profile выполняется
    :param sender: Модель отправившая сигнал - User
    :param instance: Экземпляр, который был сохранен (status)
    :param created: Указывает, был ли создан экземпляр (True)
    :param kwargs:
    :return:
    """
    if created and instance.status == 'teacher':
        Teacher.objects.create(user=instance)
    elif created and instance.status == 'student':
        Student.objects.create(user=instance)
    elif created and instance.status == 'parents':
        Parents.objects.create(user=instance)
