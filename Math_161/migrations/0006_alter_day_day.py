# Generated by Django 4.2.4 on 2023-12-16 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Math_161', '0005_alter_day_day_alter_day_id_alter_day_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Friday', 'Friday')], default=('Monday', 'Monday'), max_length=10),
        ),
    ]
