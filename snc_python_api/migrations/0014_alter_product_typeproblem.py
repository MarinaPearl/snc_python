# Generated by Django 5.0.2 on 2024-03-24 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snc_python_api', '0013_alter_product_typeproblem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='typeProblem',
            field=models.CharField(max_length=1500),
        ),
    ]
