# Generated by Django 2.1.7 on 2019-11-16 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_auto_20191116_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='address3',
            field=models.CharField(max_length=40, null=True, verbose_name='建物名'),
        ),
    ]
