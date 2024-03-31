# Generated by Django 3.0.7 on 2024-03-29 08:59

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='car',
            name='car_photo',
        ),
        migrations.RemoveField(
            model_name='car',
            name='car_photo_1',
        ),
        migrations.RemoveField(
            model_name='car',
            name='car_photo_2',
        ),
        migrations.RemoveField(
            model_name='car',
            name='car_photo_3',
        ),
        migrations.RemoveField(
            model_name='car',
            name='car_photo_4',
        ),
        migrations.RemoveField(
            model_name='car',
            name='doors',
        ),
        migrations.RemoveField(
            model_name='car',
            name='features',
        ),
        migrations.RemoveField(
            model_name='car',
            name='interior',
        ),
        migrations.RemoveField(
            model_name='car',
            name='milage',
        ),
        migrations.RemoveField(
            model_name='car',
            name='miles',
        ),
        migrations.RemoveField(
            model_name='car',
            name='state',
        ),
        migrations.RemoveField(
            model_name='car',
            name='vin_no',
        ),
        migrations.AddField(
            model_name='car',
            name='availability',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Disponibilidad'),
        ),
        migrations.AddField(
            model_name='car',
            name='axis_distance',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='axis_one_breaks',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='axis_one_distance',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='axis_one_percentage',
            field=models.CharField(blank=True, choices=[('1', '10 %'), ('2', '20 %'), ('3', '30 %'), ('4', '40 %'), ('5', '50 %'), ('6', '60 %'), ('7', '70 %'), ('8', '80 %'), ('9', '90 %')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='axis_one_suspension',
            field=models.CharField(blank=True, choices=[('1', 'Parabolica'), ('2', 'Neumática'), ('3', 'Muelles'), ('4', 'Pneumática'), ('5', 'Ballestas'), ('6', 'Eje rígido')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='axis_one_weight',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='axis_two_breaks',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='axis_two_distance',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='axis_two_percentage',
            field=models.CharField(blank=True, choices=[('1', '10 %'), ('2', '20 %'), ('3', '30 %'), ('4', '40 %'), ('5', '50 %'), ('6', '60 %'), ('7', '70 %'), ('8', '80 %'), ('9', '90 %')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='axis_two_suspension',
            field=models.CharField(blank=True, choices=[('1', 'Parabolica'), ('2', 'Neumática'), ('3', 'Muelles'), ('4', 'Pneumática'), ('5', 'Ballestas'), ('6', 'Eje rígido')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='axis_two_weight',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='brand',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Fabricante'),
        ),
        migrations.AddField(
            model_name='car',
            name='cabin',
            field=models.CharField(blank=True, choices=[('1', 'Cabina Normal'), ('2', 'Cabina con Litera'), ('3', 'Cabina Alta'), ('4', 'Cabina Baja'), ('5', 'Cabina Extra-Ancha'), ('6', 'Cabina Confort'), ('7', 'Cabina Dormitorio'), ('8', 'Cabina Doble'), ('9', 'Cabina Corta'), ('10', 'Cabina Modular')], max_length=100, null=True, verbose_name='Tipo de cabina'),
        ),
        migrations.AddField(
            model_name='car',
            name='color_int',
            field=models.CharField(blank=True, choices=[('1', 'Blanco'), ('2', 'Negro'), ('3', 'Gris'), ('4', 'Rojo'), ('5', 'Amarillo'), ('6', 'Verde'), ('7', 'Azul'), ('8', 'Naranja'), ('9', 'Rosa'), ('10', 'Marrón'), ('11', 'Plata')], max_length=100, null=True, verbose_name='Color interno'),
        ),
        migrations.AddField(
            model_name='car',
            name='delivery',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Entrega'),
        ),
        migrations.AddField(
            model_name='car',
            name='documents',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Documentos'),
        ),
        migrations.AddField(
            model_name='car',
            name='drive_train',
            field=models.CharField(blank=True, choices=[('1', 'hidráulico'), ('2', 'eléctrico'), ('3', 'hidrodinámico'), ('4', 'electromagnético'), ('5', 'neumático')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='driver_side',
            field=models.CharField(blank=True, choices=[('1', 'Izquierda'), ('12', 'Derecha')], max_length=100, null=True, verbose_name='Lado del conductor'),
        ),
        migrations.AddField(
            model_name='car',
            name='engine_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='fifth_wheel_height',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='first_registration',
            field=models.DateField(blank=True, null=True, verbose_name='Primera matricula'),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel_capacity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='guarantee',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tiempo de garantia'),
        ),
        migrations.AddField(
            model_name='car',
            name='height',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='kilometrage',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='length',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='obs',
            field=models.TextField(blank=True, null=True, verbose_name='Observaciones'),
        ),
        migrations.AddField(
            model_name='car',
            name='qty_of_deposits',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='qty_of_gears',
            field=models.IntegerField(blank=True, choices=[(5, '5'), (6, '6'), (8, '8'), (10, '10'), (12, '12')], null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='ref',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Referencia'),
        ),
        migrations.AddField(
            model_name='car',
            name='tacho',
            field=models.CharField(blank=True, choices=[('1', 'Digital'), ('2', 'Disco')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='warranty',
            field=models.BooleanField(blank=True, choices=[(False, 'No'), (True, 'Si')], null=True, verbose_name='Tiene garantia'),
        ),
        migrations.AddField(
            model_name='car',
            name='width',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='car',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Umbicación'),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(blank=True, choices=[('1', 'Blanco'), ('2', 'Negro'), ('3', 'Gris'), ('4', 'Rojo'), ('5', 'Amarillo'), ('6', 'Verde'), ('7', 'Azul'), ('8', 'Naranja'), ('9', 'Rosa'), ('10', 'Marrón'), ('11', 'Plata')], max_length=100, null=True, verbose_name='Color externo'),
        ),
        migrations.AlterField(
            model_name='car',
            name='condition',
            field=models.CharField(blank=True, choices=[('1', 'Nuevo'), ('2', 'Usado'), ('3', 'Usado, como nuevo')], max_length=100, null=True, verbose_name='Condición'),
        ),
        migrations.AlterField(
            model_name='car',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Fecha de cadastro'),
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(blank=True, choices=[('1', 'Diesel'), ('2', 'Gasolina'), ('3', 'Gas'), ('4', 'Hibrido'), ('5', 'Electrico'), ('6', 'Bio')], max_length=50, null=True, verbose_name='Combustible'),
        ),
        migrations.AlterField(
            model_name='car',
            name='is_featured',
            field=models.BooleanField(blank=True, choices=[(False, 'No'), (True, 'Si')], default=False, null=True, verbose_name='Favorito'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='no_of_owners',
            field=models.IntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5 +')], null=True, verbose_name='Proprietarios'),
        ),
        migrations.AlterField(
            model_name='car',
            name='passengers',
            field=models.IntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], null=True, verbose_name='Passageros'),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(blank=True, choices=[('1', 'Automatico'), ('2', 'Manual'), ('3', 'Semi-automatico'), ('4', 'Semi-manual'), ('5', 'Mecanico'), ('6', 'Semi-mecanico'), ('7', 'Mecanico-automatico'), ('8', 'Mecanico-semi-automatico'), ('9', 'Mecanico-semi-manual')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(blank=True, choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], null=True, verbose_name='Año'),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube_link', models.CharField(blank=True, max_length=200, null=True, validators=[django.core.validators.URLValidator()])),
                ('truck', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='truck_videos', to='cars.Car')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truck_photos', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('is_main', models.BooleanField(default=False)),
                ('truck', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='truck_photos', to='cars.Car')),
            ],
        ),
        migrations.CreateModel(
            name='Intern_cabin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intern_extras', models.ManyToManyField(blank=True, to='cars.Accessory')),
            ],
        ),
        migrations.CreateModel(
            name='Extras_security',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extras_security', models.ManyToManyField(blank=True, to='cars.Accessory')),
            ],
        ),
        migrations.CreateModel(
            name='Ext_extras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ext_extras', models.ManyToManyField(blank=True, to='cars.Accessory')),
            ],
        ),
    ]
