# Generated by Django 2.0.3 on 2018-04-02 08:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('travel_Schedule', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='travel.Travel_Schedule')),
                ('title', models.CharField(max_length=100, verbose_name='후기제목')),
                ('Contents', models.TextField(blank=True, null=True, verbose_name='내용')),
                ('img_blog', models.ImageField(upload_to='blog', verbose_name='후기이미지')),
                ('score', models.IntegerField(default=5, verbose_name='평점')),
                ('isusable', models.BooleanField(default=True, verbose_name='사용여부')),
                ('creationdatetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성시간')),
                ('modifydatetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
            ],
            options={
                'ordering': ['-modifydatetime'],
            },
        ),
    ]
