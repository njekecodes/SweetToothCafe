# Generated by Django 4.2.7 on 2023-11-20 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweet_tooth_cafe', '0008_alter_candy_cost_alter_candy_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='candy',
            name='image',
            field=models.FileField(default='candies/sweets.png', upload_to='candies'),
        ),
    ]
