# Generated by Django 5.0.2 on 2024-03-24 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snc_python_api', '0008_alter_product_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
    ]
