# Generated by Django 3.1 on 2020-12-04 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20201204_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]