# Generated by Django 4.0.1 on 2022-01-31 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parks', '0002_rename_parks_park'),
    ]

    operations = [
        migrations.AddField(
            model_name='park',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
