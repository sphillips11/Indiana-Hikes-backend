# Generated by Django 4.0.1 on 2022-02-02 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parks', '0006_park_accessible_trails_park_difficult_trails_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='park',
            name='trail_map',
            field=models.URLField(),
        ),
    ]
