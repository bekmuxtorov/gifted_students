# Generated by Django 4.2 on 2023-06-23 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_base_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='printed',
            field=models.CharField(blank=True, choices=[('local', 'Mahalliy jurnalda'), ('foreign', 'Xalqaro jurnalda')], max_length=7, null=True),
        ),
    ]
