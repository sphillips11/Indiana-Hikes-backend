# Generated by Django 4.0.1 on 2022-01-28 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parks', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Parks',
            new_name='Park',
        ),
    ]
