# Generated by Django 4.2.4 on 2023-12-17 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Math_161', '0009_alter_day_day_worksheet_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
