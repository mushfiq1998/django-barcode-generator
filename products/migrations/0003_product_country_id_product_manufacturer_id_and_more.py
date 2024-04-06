# Generated by Django 4.2.11 on 2024-04-06 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_barcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='country_id',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer_id',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='number_id',
            field=models.CharField(max_length=5, null=True),
        ),
    ]