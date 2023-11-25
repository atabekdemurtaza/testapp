# Generated by Django 4.2.7 on 2023-11-23 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['pub_year'], 'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_year',
            field=models.DateTimeField(verbose_name='publication year'),
        ),
    ]