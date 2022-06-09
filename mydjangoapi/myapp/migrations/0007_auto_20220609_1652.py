# Generated by Django 3.2 on 2022-06-09 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AlterField(
            model_name='product',
            name='imagePath',
            field=models.ImageField(blank=True, null=True, upload_to='medias'),
        ),
    ]
