# Generated by Django 5.0.7 on 2024-07-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_item_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='caption',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
