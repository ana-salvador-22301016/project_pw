# Generated by Django 4.0.6 on 2024-05-24 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0007_alter_docente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='apresentacao',
            field=models.CharField(max_length=500),
        ),
    ]
