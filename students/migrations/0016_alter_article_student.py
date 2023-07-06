# Generated by Django 4.2 on 2023-07-06 10:02

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0015_message_article_message_win'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='student',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='continent', chained_model_field='continent', on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='students.student', verbose_name='Talaba'),
        ),
    ]
