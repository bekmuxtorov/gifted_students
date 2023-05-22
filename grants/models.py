from django.db import models

# Create your models here.


class Grant(models.Model):
    name = models.CharField('Nomi', max_length=200)
    description = models.TextField('Umumiy ma\'lumot', blank=True, null=True)
    statute = models.FileField(
        'Nizom', upload_to='grant/nizomlar/', blank=True, null=True)
    start_date = models.DateTimeField('Boshlanish vaqti', auto_now=True)
    end_date = models.DateTimeField('Tugash vaqti')
    status = models.BooleanField('Holati', default=True)
    first_science = models.CharField('Birinchi fan', max_length=100)
    second_science = models.CharField('Ikkinchi fan', max_length=100)
    third_science = models.CharField('Uchinchi fan', max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Tanlov'
        verbose_name_plural = '2. Tanlovlar'

    def __str__(self):
        return self.name


class ScienceDirection(models.Model):
    student = models.ForeignKey(
        to='students.Student',
        verbose_name='Talaba',
        on_delete=models.CASCADE,
        related_name='science_directions'
    )
    grant = models.ForeignKey(
        to=Grant,
        verbose_name='Tanlov',
        on_delete=models.CASCADE,
        related_name='science_directions'
    )
    research_advisor = models.CharField(
        'Ilmiy maslahatchi', max_length=100, blank=True, null=True)
    letter_dekan = models.FileField(
        'Dekanlik hujjati', upload_to='grant/dekan_tavsiyanoma/', blank=True, null=True)
    letter_mudir = models.FileField(
        'Mudirlik hujjati', upload_to='grant/mudir_tavsiyanoma/', blank=True, null=True)
    rank_notebook = models.FileField(
        'Reyting daftarcha', upload_to='grant/reyting_daftarcha/', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ilmiy yo\'nalish'
        verbose_name_plural = '1. Ilmiy yo\'nalishlar'

    def __str__(self):
        return f'{self.student.name} - {self.grant.name}'
