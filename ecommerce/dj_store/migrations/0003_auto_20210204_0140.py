# Generated by Django 3.1.5 on 2021-02-03 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_store', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
