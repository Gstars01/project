# Generated by Django 3.2 on 2021-06-14 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'verbose_name': 'DOGE게시물', 'verbose_name_plural': 'DOGE게시물'},
        ),
        migrations.AlterModelTable(
            name='board',
            table='DOGE_board',
        ),
    ]
