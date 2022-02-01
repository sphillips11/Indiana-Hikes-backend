# Generated by Django 4.0.1 on 2022-01-31 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parks', '0004_alter_park_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='park',
            name='trail_ratings',
        ),
        migrations.AddField(
            model_name='park',
            name='easy_trails',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='park',
            name='moderate_trails',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='park',
            name='rugged_trails',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='park',
            name='very_rugged_trails',
            field=models.BooleanField(default=False),
        ),
    ]
