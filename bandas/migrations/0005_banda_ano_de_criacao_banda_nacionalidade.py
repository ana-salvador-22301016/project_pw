# Generated by Django 4.0.6 on 2024-04-01 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0004_delete_artista_remove_musica_ano_lancamento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='ano_de_criacao',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='banda',
            name='nacionalidade',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]