# Generated by Django 3.2.5 on 2021-08-12 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_topic'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topic',
            new_name='Content',
        ),
    ]
