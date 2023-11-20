# Generated by Django 4.2.7 on 2023-11-20 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_tooth_cafe', '0014_alter_customer_profile_pic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='candy',
            name='category',
            field=models.CharField(default='Chocolate', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='candy',
            name='category_type',
            field=models.CharField(default='Milk', max_length=50, null=True),
        ),
    ]
