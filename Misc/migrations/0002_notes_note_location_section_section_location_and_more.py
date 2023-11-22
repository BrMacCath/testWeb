# Generated by Django 4.2.4 on 2023-11-21 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Misc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='note_location',
            field=models.CharField(default='Default', max_length=30),
        ),
        migrations.AddField(
            model_name='section',
            name='section_location',
            field=models.CharField(default='Default', max_length=30),
        ),
        migrations.AddField(
            model_name='topic',
            name='topic_location',
            field=models.CharField(default='Default', max_length=30),
        ),
    ]