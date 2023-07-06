from django.db import models

from accounts.models import CustomUser
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

PRINTED = (
    ('local', 'Mahalliy jurnalda'),
    ('foreign', 'Xalqaro jurnalda'),
)


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_date(self):
        return self.create_at.strftime("%d/%m/%Y, %H:%M")

    def students_count(self):
        return self.students.count()

    class Meta:
        verbose_name = 'Fakultet'
        verbose_name_plural = '1. Fakultetlar'


class SubFaculty(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Yo\'nalish'
        verbose_name_plural = '2. Yo\'nalishlar'


class Student(models.Model):
    base_student = models.OneToOneField(
        to=CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/students/image', blank=True)
    faculty = models.ForeignKey(
        to=Faculty,
        on_delete=models.SET_NULL,
        verbose_name='Faculty',
        related_name='students',
        blank=True,
        null=True
    )
    sub_faculty = models.ForeignKey(
        to=SubFaculty,
        on_delete=models.SET_NULL,
        verbose_name='SubFaculty',
        related_name='students',
        blank=True,
        null=True
    )
    group = models.CharField(verbose_name='Guruh', max_length=10)
    course = models.IntegerField(verbose_name='Kurs')
    passport_number = models.CharField(max_length=10, blank=True)
    idcart_number = models.CharField(max_length=16, blank=True)
    passport_or_idcart_file = models.FileField(
        upload_to='media/students/', blank=True)
    phone_number = models.CharField(
        max_length=15, verbose_name="Telefon raqam", blank=True)
    status = models.BooleanField(default=False)
    region = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    resume = models.FileField(upload_to='media/students/', blank=True)
    grade_book = models.FileField(upload_to='media/students/', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.base_student.first_name + ' ' + self.base_student.last_name + ' || ' + self.group

    def get_full_name(self):
        return self.base_student.first_name + ' ' + self.base_student.last_name

    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = '3. Talabalar'


class Article(models.Model):
    student = ChainedForeignKey(
        Student,
        chained_field="continent",
        chained_model_field="continent",
        show_all=False,
        auto_choose=True,
        verbose_name='Talaba',
        related_name='articles',
        sort=True)
    

    printed = models.CharField(
        max_length=7, choices=PRINTED, blank=True, null=True)
    name = models.CharField(verbose_name='Nomi', max_length=200)
    file = models.FileField(upload_to='media/students/articles')
    grade = models.IntegerField(verbose_name='Baho', default=0)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = '4. Maqolalar'


class Win(models.Model):
    student = models.ForeignKey(
        to=Student,
        on_delete=models.CASCADE,
        verbose_name='Talaba',
        related_name='wins'
    )
    name = models.CharField(verbose_name='Nomi', max_length=200)
    file = models.FileField(upload_to='media/students/wins')
    grade = models.IntegerField(verbose_name='Baho', default=0)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Yutuq'
        verbose_name_plural = '5. Yutuqlar'


class Message(models.Model):
    student = models.ForeignKey(
        to=Student,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    article = models.ForeignKey(
        to=Article, 
        on_delete=models.CASCADE,
        related_name='message',
        verbose_name='Maqola nomi',
        blank=True, 
        null=True
    )
    win = models.ForeignKey(
        to=Win,
        on_delete=models.CASCADE,
        related_name='message',
        verbose_name='Yutuq nomi',
        blank=True,
        null=True
    )

    letter = models.TextField(verbose_name='Talaba uchun xat', max_length=3000)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Xabar'
        verbose_name_plural = '6. Xabarlar'
