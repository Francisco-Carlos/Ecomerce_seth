# Generated by Django 4.1.4 on 2023-02-12 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estoque', '0007_alter_empresa_lucro_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='estoque',
            name='img',
            field=models.ImageField(default=1, upload_to='Img_prod/%d/%m%Y'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empresa_lucro',
            name='Data',
            field=models.DateField(),
        ),
    ]