# Generated by Django 3.0.7 on 2024-03-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_auto_20240329_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='passengers',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], null=True, verbose_name='Passageros'),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Precio'),
        ),
    ]
