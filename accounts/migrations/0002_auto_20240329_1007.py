# Generated by Django 3.0.7 on 2024-03-29 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorites',
            name='car',
        ),
        migrations.RemoveField(
            model_name='favorites',
            name='user',
        ),
        migrations.RemoveField(
            model_name='last_viwed',
            name='car',
        ),
        migrations.RemoveField(
            model_name='last_viwed',
            name='user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.DeleteModel(
            name='answer',
        ),
        migrations.DeleteModel(
            name='Favorites',
        ),
        migrations.DeleteModel(
            name='Last_viwed',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
