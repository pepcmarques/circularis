# Generated by Django 3.0.8 on 2020-09-15 22:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0004_delete_bookstatus'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(choices=[('NCL', '-----------------------'),
                                                   ('ANT', 'ANTIQUES & COLLECTIBLES'), ('ARC', 'ARCHITECTURE'),
                                                   ('ART', 'ART'), ('BIB', 'BIBLES'),
                                                   ('BIO', 'BIOGRAPHY & AUTOBIOGRAPHY'), ('BOD', 'BODY, MIND & SPIRIT'),
                                                   ('BUS', 'BUSINESS & ECONOMICS'), ('COM', 'COMICS & GRAPHIC NOVELS'),
                                                   ('CMP', 'COMPUTERS'), ('COO', 'COOKING'),
                                                   ('CRA', 'CRAFTS & HOBBIES'), ('DES', 'DESIGN'), ('DRA', 'DRAMA'),
                                                   ('EDU', 'EDUCATION'), ('FAM', 'FAMILY & RELATIONSHIPS'),
                                                   ('FIC', 'FICTION'), ('FOR', 'FOREIGN LANGUAGE STUDY'),
                                                   ('GAM', 'GAMES & ACTIVITIES'), ('GAR', 'GARDENING'),
                                                   ('HEA', 'HEALTH & FITNESS'), ('HIS', 'HISTORY'),
                                                   ('HOU', 'HOUSE & HOME'), ('HUM', 'HUMOR'),
                                                   ('JUV', 'JUVENILE FICTION'), ('JUN', 'JUVENILE NONFICTION'),
                                                   ('LAN', 'LANGUAGE ARTS & DISCIPLINES'), ('LAW', 'LAW'),
                                                   ('LIT', 'LITERARY COLLECTIONS'), ('LIC', 'LITERARY CRITICISM'),
                                                   ('MAT', 'MATHEMATICS'), ('MED', 'MEDICAL'), ('MUS', 'MUSIC'),
                                                   ('NAT', 'NATURE'), ('PER', 'PERFORMING ARTS'), ('PET', 'PETS'),
                                                   ('PHI', 'PHILOSOPHY'), ('PHO', 'PHOTOGRAPHY'), ('POE', 'POETRY'),
                                                   ('POL', 'POLITICAL SCIENCE'), ('PSY', 'PSYCHOLOGY'),
                                                   ('REF', 'REFERENCE'), ('REL', 'RELIGION'), ('SCI', 'SCIENCE'),
                                                   ('SEL', 'SELF-HELP'), ('SOC', 'SOCIAL SCIENCE'),
                                                   ('SPO', 'SPORTS & RECREATION'), ('STU', 'STUDY AIDS'),
                                                   ('TEC', 'TECHNOLOGY & ENGINEERING'), ('TRA', 'TRANSPORTATION'),
                                                   ('TRV', 'TRAVEL'), ('TRU', 'TRUE CRIME'),
                                                   ('YOU', 'YOUNG ADULT FICTION'),
                                                   ('YOA', 'YOUNG ADULT NONFICTION')],
                                          default='NCL', max_length=3, unique=True)),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'categories',
                'ordering': ['status'],
            },
        ),
        migrations.CreateModel(
            name='BookStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(choices=[('AV', 'Available'), ('RE', 'I am reading'),
                                                   ('LO', 'Locked'), ('RM', 'Removed')],
                                          default='AV', max_length=2, unique=True)),
                ('status', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'bookstatus',
                'ordering': ['status'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('subtitle', models.CharField(blank=True, max_length=60, null=True)),
                ('author_1', models.CharField(max_length=60)),
                ('author_2', models.CharField(blank=True, max_length=60, null=True)),
                ('author_3', models.CharField(blank=True, max_length=60, null=True)),
                ('publisher', models.CharField(blank=True, max_length=60, null=True)),
                ('publishedDate', models.CharField(blank=True, max_length=4, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('isbn_10', models.CharField(blank=True, max_length=10, null=True)),
                ('isbn_13', models.CharField(blank=True, max_length=13, null=True)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('thumbnail', models.BinaryField(blank=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.Address')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING,
                                               to='books.BookCategory')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING,
                                             to='books.BookStatus', to_field='code')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING,
                                           to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
