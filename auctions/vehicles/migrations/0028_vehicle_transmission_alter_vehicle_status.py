# Generated by Django 5.0.7 on 2024-08-07 09:50

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
        migrations.AlterField(
            model_name='vehicle',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('On_auction', 'On_auction'), ('On_bid', 'On_bid')], default='available', max_length=10),
        ),
    ]