# Generated by Django 2.0.3 on 2018-04-12 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
        ('reservation', '0001_initial'),
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='wish_products',
            field=models.ManyToManyField(blank=True, related_name='wish_users', through='reservation.WishList', to='travel.TravelInformation'),
        ),
    ]