# Generated by Django 5.0.2 on 2024-03-24 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snc_python_api', '0007_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(max_length=2000),
        ),
    ]