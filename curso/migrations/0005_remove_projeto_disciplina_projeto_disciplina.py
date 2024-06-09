# Generated by Django 4.0.6 on 2024-05-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0004_alter_docente_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='disciplina',
        ),
        migrations.AddField(
            model_name='projeto',
            name='disciplina',
            field=models.ManyToManyField(related_name='projeto', to='curso.disciplina'),
        ),
    ]
