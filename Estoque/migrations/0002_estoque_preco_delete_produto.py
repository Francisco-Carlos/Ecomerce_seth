# Generated by Django 4.1.4 on 2023-02-07 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estoque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoque',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]
