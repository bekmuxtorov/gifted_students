from django.db import models

# Create your models here.


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SubFaculty(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    # base_student = models.ForeignKey('BaseStudent', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='students/image', blank=True)
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
        upload_to='students/', blank=True)
    status = models.BooleanField(default=False)
    region = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    resume = models.FileField(upload_to='students/', blank=True)

    # def __str__(self):
    #     return self.base_student.first_name + ' ' + self.base_student.last_name + ' || ' + self.group

    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'


class Article(models.Model):
    student = models.ForeignKey(
        to=Student,
        on_delete=models.CASCADE,
        verbose_name='Talaba',
        related_name='articles'
    )
    name = models.CharField(verbose_name='Nomi', max_length=200)
    file = models.FileField(upload_to='students/articles')

    def __str__(self):
        return self.student + ' || ' + self.name[:100]

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'


class Win(models.Model):
    student = models.ForeignKey(
        to=Student,
        on_delete=models.CASCADE,
        verbose_name='Talaba',
        related_name='wins'
    )
    name = models.CharField(verbose_name='Nomi', max_length=200)
    file = models.FileField(upload_to='students/wins')

    def __str__(self):
        return self.student + ' || ' + self.name[:50]

    class Meta:
        verbose_name = 'Yutuq'
        verbose_name_plural = 'Yutuqlar'
