# Generated by Django 3.0.7 on 2024-03-29 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0015_auto_20240329_1417'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accessory',
            options={'verbose_name_plural': 'Accesorios'},
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name_plural': 'Camiñones'},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name_plural': 'Imágenes'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name_plural': 'Vídeos'},
        ),
    ]