# Generated by Django 5.0.2 on 2024-03-24 17:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('snc_python_api', '0012_rename_type_product_typeproblem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='typeProblem',
            field=models.CharField(default="", max_length=1500),
        ),
    ]