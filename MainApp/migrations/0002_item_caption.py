# Generated by Django 5.0.7 on 2024-07-23 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='caption',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
