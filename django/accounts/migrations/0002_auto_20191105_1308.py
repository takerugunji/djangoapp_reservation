# Generated by Django 2.1.7 on 2019-11-05 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gendar',
            field=models.CharField(blank=True, choices=[('女性', '女性'), ('男性', '男性')], max_length=2, verbose_name='性別'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=255, verbose_name='電話番号'),
        ),
    ]
