# Generated by Django 2.1.7 on 2019-11-16 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20191114_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='address3',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='建物名'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='address1',
            field=models.CharField(max_length=40, null=True, verbose_name='都道府県'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='address2',
            field=models.CharField(max_length=40, null=True, verbose_name='市区町村番地'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_in',
            field=models.DateField(null=True, verbose_name='チェックイン'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='check_out',
            field=models.DateField(null=True, verbose_name='チェックアウト'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='zip_code',
            field=models.CharField(max_length=8, null=True, verbose_name='郵便番号'),
        ),
    ]
