# Generated by Django 5.0.7 on 2024-07-26 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0016_alter_vehicle_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='id',
            new_name='v_id',
        ),
    ]
