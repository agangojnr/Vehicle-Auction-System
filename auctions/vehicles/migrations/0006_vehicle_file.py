# Generated by Django 5.0.6 on 2024-07-14 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0005_alter_vehicle_bid_status_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='file',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]
