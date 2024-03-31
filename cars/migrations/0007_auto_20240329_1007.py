# Generated by Django 3.0.7 on 2024-03-29 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_auto_20240329_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='slug',
            field=models.SlugField(default=1, max_length=1024),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='truck_photos',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]