# Generated by Django 4.0.1 on 2022-02-13 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parks', '0009_alter_park_park_type_alter_park_state_trail'),
        ('hikers', '0002_visit_visit_unique_trip'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Visit',
            new_name='Hike',
        ),
        migrations.RemoveConstraint(
            model_name='hike',
            name='unique_trip',
        ),
        migrations.AddConstraint(
            model_name='hike',
            constraint=models.UniqueConstraint(fields=('hiker_id', 'park_id', 'date'), name='unique_hike'),
        ),
    ]