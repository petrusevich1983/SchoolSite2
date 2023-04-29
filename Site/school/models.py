from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator


class Lesson(models.Model):
    """
    Предметы в школьной программе
    """
    name = models.CharField('Предмет', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class SchoolClass(models.Model):
    """
    Список классов
    """
    class_num = models.SmallIntegerField('Номер', validators=[MaxValueValidator(11), MinValueValidator(1)])
    class_index = models.CharField('Буква', max_length=1)
    lessons = models.ManyToManyField(Lesson, verbose_name='Предметы класса')

    def __str__(self):
        return f'{self.class_num}{self.class_index}'

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
