# Generated by Django 4.1.4 on 2023-05-31 21:11

import Estoque.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estoque', '0010_clientes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='Produto',
            field=models.CharField(blank=True, max_length=100, verbose_name=Estoque.models.Estoque),
        ),
    ]
