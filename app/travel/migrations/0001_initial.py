# Generated by Django 2.0.3 on 2018-04-02 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City_Hotplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='핫플레이스')),
                ('isusable', models.BooleanField(verbose_name='사용여부')),
                ('creationdatetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성시간')),
                ('modifydatetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
            ],
        ),
        migrations.CreateModel(
            name='City_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='나라명')),
                ('continent', models.CharField(max_length=20, verbose_name='대륙')),
                ('nationality', models.CharField(max_length=20, verbose_name='나라')),
                ('isusable', models.BooleanField(verbose_name='사용여부')),
                ('creationdatetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성시간')),
                ('modifydatetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
            ],
        ),
        migrations.CreateModel(
            name='Company_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='회사명')),
                ('info', models.TextField(verbose_name='회사설명')),
                ('isusable', models.BooleanField(verbose_name='사용여부')),
                ('creationdatetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성시간')),
                ('modifydatetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
            ],
        ),
        migrations.CreateModel(
            name='Travel_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='상품명')),
                ('category', models.CharField(blank=True, choices=[('교통/티켓', '교통/티켓'), ('여행편의', '여행편의'), ('가이드투어', '가이드투어'), ('식당', '식당'), ('액티비티', '액티비티'), ('숙박/민박', '숙박/민박'), ('즐길거리', '즐길거리')], max_length=10, verbose_name='카테고리')),
                ('theme', models.CharField(blank=True, max_length=100, verbose_name='테마')),
                ('productType', models.CharField(blank=True, max_length=100, verbose_name='상품타입')),
                ('language', models.CharField(max_length=3, verbose_name='언어')),
                ('time', models.IntegerField(verbose_name='소요시간')),
                ('images', models.ImageField(upload_to='', verbose_name='이미지')),
                ('description', models.TextField(verbose_name='상품설명')),
                ('isusable', models.BooleanField(default=True, verbose_name='사용여부')),
                ('creationdatetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성시간')),
                ('modifydatetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.City_Information', verbose_name='city')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Company_Information', verbose_name='company')),
            ],
        ),
        migrations.CreateModel(
            name='Travel_Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='여행시작날짜')),
                ('end_date', models.DateField(auto_now_add=True, verbose_name='여행마끝날짜')),
                ('price', models.IntegerField(default=0, verbose_name='상품금액')),
                ('price_descrption', models.TextField(verbose_name='상품금액 포함사항')),
                ('meetingTime', models.CharField(max_length=100, verbose_name='만남시간')),
                ('mettingPlace', models.CharField(max_length=100, verbose_name='만남장소')),
                ('isusable', models.BooleanField(default=True, verbose_name='사용여부')),
                ('creationdatetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성시간')),
                ('modifydatetime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='수정시간')),
                ('member', models.ManyToManyField(related_name='reserved_member', to=settings.AUTH_USER_MODEL)),
                ('travel_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Travel_Information', verbose_name='travelinfo')),
            ],
            options={
                'ordering': ['-creationdatetime'],
            },
        ),
        migrations.AddField(
            model_name='city_hotplace',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.City_Information', verbose_name='city'),
        ),
    ]
