# Generated by Django 3.2.5 on 2021-08-11 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_chapter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignsubject',
            name='classname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.standard', verbose_name='Class'),
        ),
        migrations.AlterField(
            model_name='assignsubject',
            name='subjectname',
            field=models.ManyToManyField(to='home.Subject', verbose_name=' List of Subjects'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='subjectname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.assignsubject', verbose_name='Subject'),
        ),
    ]