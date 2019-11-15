# Generated by Django 2.1.7 on 2019-11-14 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20191111_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='address1',
            field=models.CharField(blank=True, max_length=40, verbose_name='都道府県'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='address2',
            field=models.CharField(blank=True, max_length=40, verbose_name='市区町村番地'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='zip_code',
            field=models.CharField(blank=True, max_length=8, verbose_name='郵便番号'),
        ),
    ]