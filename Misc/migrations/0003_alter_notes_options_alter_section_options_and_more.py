# Generated by Django 4.2.4 on 2023-11-22 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Misc', '0002_notes_note_location_section_section_location_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'ordering': ['note_weight']},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['section_weight']},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['topic_weight']},
        ),
    ]
