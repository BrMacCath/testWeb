# Generated by Django 4.2.4 on 2023-12-17 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Math_161', '0007_remove_day_day_webpage_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='day_worksheet_source',
            field=models.CharField(default='test', max_length=50),
        ),
    ]
