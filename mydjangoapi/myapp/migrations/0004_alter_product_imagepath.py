# Generated by Django 3.2 on 2022-05-28 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_products_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imagePath',
            field=models.ImageField(blank=True, null=True, upload_to='medias'),
        ),
    ]