# Generated by Django 3.2 on 2021-05-07 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_username_user_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='emali',
            new_name='email',
        ),
    ]
