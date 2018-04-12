# Generated by Django 2.0.3 on 2018-04-12 02:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0001_initial'),
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='travel_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.TravelInformation'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='travel_Schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.TravelSchedule', verbose_name='travel_schedule'),
        ),
        migrations.AddField(
            model_name='recentvisitpage',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recentvisitpage',
            name='travel_Schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.TravelInformation'),
        ),
    ]
