# Generated by Django 5.0.2 on 2024-03-24 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snc_python_api', '0009_remove_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(default="для всех типов волос", max_length=100),
            preserve_default=False,
        ),
    ]
