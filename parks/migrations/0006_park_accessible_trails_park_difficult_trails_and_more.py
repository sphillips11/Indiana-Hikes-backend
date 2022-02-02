# Generated by Django 4.0.1 on 2022-02-02 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parks', '0005_remove_park_trail_ratings_park_easy_trails_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='park',
            name='accessible_trails',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='park',
            name='difficult_trails',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='park',
            name='moderately_rugged',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='park',
            name='more_difficult_trails',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='park',
            name='note',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='park',
            name='phone',
            field=models.CharField(default=92, max_length=14),
        ),
    ]
