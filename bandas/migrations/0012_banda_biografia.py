# Generated by Django 4.0.6 on 2024-05-27 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0011_banda_detalhe'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='biografia',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
