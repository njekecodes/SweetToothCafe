# Generated by Django 4.2.7 on 2023-11-20 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_tooth_cafe', '0011_customer_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='1234567', max_length=50),
        ),
    ]
