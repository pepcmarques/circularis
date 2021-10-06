# Generated by Django 3.2 on 2021-10-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_auto_20211005_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(choices=[('RQ', 'Request'), ('RJ', 'Reject'), ('AC', 'Accept')], default='RQ',
                                          max_length=2, unique=True)),
                ('status', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'bookstatus',
                'ordering': ['status'],
            },
        ),
    ]