# Generated by Django 5.0.2 on 2024-03-24 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snc_python_api', '0002_remove_product_cost_product_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
