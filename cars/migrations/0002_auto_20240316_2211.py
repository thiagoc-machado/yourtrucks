# Generated by Django 3.0.7 on 2024-03-16 21:11

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='truck_videos',
        ),
        migrations.AddField(
            model_name='video',
            name='youtube_link',
            field=models.CharField(blank=True, max_length=200, null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='cars',
            name='availability',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Disponibilidad'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='condition',
            field=models.CharField(blank=True, choices=[('1', 'Nuevo'), ('2', 'Usado'), ('3', 'Usado, como nuevo')], max_length=100, null=True, verbose_name='Condición'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Fecha de cadastro'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='delivery',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Entrega'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='documents',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Documentos'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='drive_train',
            field=models.CharField(blank=True, choices=[('1', 'hidráulico'), ('2', 'eléctrico'), ('3', 'hidrodinámico'), ('4', 'electromagnético'), ('5', 'neumático')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='fuel_type',
            field=models.CharField(blank=True, choices=[('1', 'Diesel'), ('2', 'Gasolina'), ('3', 'Gas'), ('4', 'Hibrido'), ('5', 'Electrico'), ('6', 'Bio')], max_length=50, null=True, verbose_name='Combustible'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='guarantee',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tiempo de garantia'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='is_featured',
            field=models.BooleanField(blank=True, choices=[('1', 'Si'), ('2', 'No')], default=False, null=True, verbose_name='Favorito'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Umbicación'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='no_of_owners',
            field=models.IntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5 +')], null=True, verbose_name='Proprietarios'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='obs',
            field=models.TextField(blank=True, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='passengers',
            field=models.IntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], null=True, verbose_name='Passageros'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='warranty',
            field=models.BooleanField(blank=True, choices=[('1', 'Si'), ('2', 'No')], null=True, verbose_name='Tiene garantia'),
        ),
        migrations.AlterField(
            model_name='cars',
            name='year',
            field=models.IntegerField(blank=True, choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], null=True, verbose_name='Año'),
        ),
    ]
