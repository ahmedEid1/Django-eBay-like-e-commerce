# Generated by Django 3.1.7 on 2021-02-20 15:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_listing_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watchers',
            field=models.ManyToManyField(related_name='watch_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
