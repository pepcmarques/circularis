# Generated by Django 3.0.8 on 2020-07-27 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20200724_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='unit',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]