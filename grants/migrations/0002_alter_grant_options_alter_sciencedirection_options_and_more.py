# Generated by Django 4.2 on 2023-05-22 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_article_options_alter_faculty_options_and_more'),
        ('grants', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grant',
            options={'verbose_name': 'Tanlov', 'verbose_name_plural': '2. Tanlovlar'},
        ),
        migrations.AlterModelOptions(
            name='sciencedirection',
            options={'verbose_name': "Ilmiy yo'nalish", 'verbose_name_plural': "1. Ilmiy yo'nalishlar"},
        ),
        migrations.AlterField(
            model_name='grant',
            name='start_date',
            field=models.DateTimeField(verbose_name='Boshlanish vaqti'),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('success', 'Muaffaqiyatli'), ('failed', 'Rad etildi'), ('waiting', 'Kutilmoqda')], default='waiting', max_length=10, verbose_name='Holati')),
                ('first_science_grade', models.IntegerField(blank=True, null=True, verbose_name='Birinchi fan')),
                ('second_science_grade', models.IntegerField(blank=True, null=True, verbose_name='Ikkinchi fan')),
                ('third_science_grade', models.IntegerField(blank=True, null=True, verbose_name='Uchinchi fan')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('grant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='grants.grant', verbose_name='Tanlov')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='students.student', verbose_name='Talaba')),
            ],
            options={
                'verbose_name': 'Natija',
                'verbose_name_plural': 'Natijalar',
            },
        ),
    ]
