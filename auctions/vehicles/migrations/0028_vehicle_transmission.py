# Generated by Django 5.0.6 on 2024-08-07 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0027_rename_sold_auctionhistory_on_bid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='transmission',
            field=models.CharField(blank=True, choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')], max_length=255),
        ),
    ]