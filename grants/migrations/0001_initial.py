# Generated by Django 4.2 on 2023-05-22 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0003_alter_article_options_alter_faculty_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nomi')),
                ('description', models.TextField(blank=True, null=True, verbose_name="Umumiy ma'lumot")),
                ('statute', models.FileField(blank=True, null=True, upload_to='grant/nizomlar/', verbose_name='Nizom')),
                ('start_date', models.DateTimeField(auto_now=True, verbose_name='Boshlanish vaqti')),
                ('end_date', models.DateTimeField(verbose_name='Tugash vaqti')),
                ('status', models.BooleanField(default=True, verbose_name='Holati')),
                ('first_science', models.CharField(max_length=100, verbose_name='Birinchi fan')),
                ('second_science', models.CharField(max_length=100, verbose_name='Ikkinchi fan')),
                ('third_science', models.CharField(max_length=100, verbose_name='Uchinchi fan')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Tanlov',
                'verbose_name_plural': 'Tanlovlar',
            },
        ),
        migrations.CreateModel(
            name='ScienceDirection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research_advisor', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ilmiy maslahatchi')),
                ('letter_dekan', models.FileField(blank=True, null=True, upload_to='grant/dekan_tavsiyanoma/', verbose_name='Dekanlik hujjati')),
                ('letter_mudir', models.FileField(blank=True, null=True, upload_to='grant/mudir_tavsiyanoma/', verbose_name='Mudirlik hujjati')),
                ('rank_notebook', models.FileField(blank=True, null=True, upload_to='grant/reyting_daftarcha/', verbose_name='Reyting daftarcha')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('grant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='science_directions', to='grants.grant', verbose_name='Tanlov')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='science_directions', to='students.student', verbose_name='Talaba')),
            ],
            options={
                'verbose_name': "Ilmiy yo'nalish",
                'verbose_name_plural': "Ilmiy yo'nalishlar",
            },
        ),
    ]
