# Generated by Django 5.1.1 on 2024-09-13 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_product_image1_alter_product_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, help_text="O'lcham:  149x118 px", unique=True, upload_to='media/products/detail/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, help_text="O'lcham:  149x118 px", unique=True, upload_to='media/products/detail/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, help_text="O'lcham:  149x118 px", unique=True, upload_to='media/products/detail/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, help_text="O'lcham:  149x118 px", unique=True, upload_to='media/products/detail/'),
        ),
    ]
