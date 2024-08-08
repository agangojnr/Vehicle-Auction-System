# Generated by Django 5.0.7 on 2024-07-25 13:32

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0013_alter_bidding_vehicle_alter_vehicleimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('vehicles', models.ManyToManyField(related_name='auctions', to='vehicles.vehicle')),
            ],
        ),
    ]
