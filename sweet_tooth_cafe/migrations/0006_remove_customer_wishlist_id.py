# Generated by Django 4.2.7 on 2023-11-17 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_tooth_cafe', '0005_alter_customer_wishlist_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='wishlist_id',
        ),
    ]
