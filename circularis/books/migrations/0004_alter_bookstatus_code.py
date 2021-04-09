# Generated by Django 3.2 on 2021-04-08 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstatus',
            name='code',
            field=models.CharField(choices=[('AV', 'Available'), ('CO', 'Checked out'), ('LO', 'Locked'),
                                            ('RE', 'Requested'), ('RM', 'Removed')],
                                   default='AV', max_length=2, unique=True),
        ),
    ]
