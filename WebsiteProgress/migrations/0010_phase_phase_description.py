# Generated by Django 4.2.4 on 2023-09-15 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebsiteProgress', '0009_alter_phase_web_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='phase',
            name='phase_description',
            field=models.CharField(default='Not yet.', max_length=100),
        ),
    ]