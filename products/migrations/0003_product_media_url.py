# Generated by Django 5.1.3 on 2024-12-21 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_media_urls_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='media_url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
