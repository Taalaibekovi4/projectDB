# Generated by Django 5.1.3 on 2024-12-21 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_media_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='media_url',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to=''),
        ),
    ]
