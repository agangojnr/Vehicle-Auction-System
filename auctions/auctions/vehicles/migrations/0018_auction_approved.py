# Generated by Django 5.0.7 on 2024-07-30 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0017_auctionhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
