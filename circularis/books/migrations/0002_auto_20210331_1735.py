# Generated by Django 3.0.8 on 2021-03-31 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author_2',
        ),
        migrations.RemoveField(
            model_name='book',
            name='author_3',
        ),
        migrations.RemoveField(
            model_name='book',
            name='description',
        ),
        migrations.RemoveField(
            model_name='book',
            name='isbn_10',
        ),
        migrations.RemoveField(
            model_name='book',
            name='isbn_13',
        ),
        migrations.RemoveField(
            model_name='book',
            name='pages',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publishedDate',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='book',
            name='subtitle',
        ),
    ]
