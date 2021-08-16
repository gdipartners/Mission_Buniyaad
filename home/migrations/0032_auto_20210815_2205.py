# Generated by Django 3.2.5 on 2021-08-15 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_newcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcontent',
            name='classname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.standard', verbose_name='Class'),
        ),
        migrations.AlterField(
            model_name='newcontent',
            name='subjectname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subject', verbose_name='Subject'),
        ),
    ]