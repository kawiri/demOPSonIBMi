# Generated by Django 3.2 on 2021-04-21 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='phone_numer',
            new_name='phone_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='borrar',
        ),
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(max_length=500, null=True, upload_to='users/picture'),
        ),
    ]
